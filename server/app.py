from flask import Flask, render_template, request, jsonify
from elevenlabs import generate
import datetime
import os  
from flask_cors import CORS
from dotenv import load_dotenv
from urllib.parse import urlparse
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
import openai
from langchain.chat_models import ChatOpenAI
import pinecone
from langchain.vectorstores.pinecone import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from typing import List
import langchain
import logging
from langchain.schema import Document
from langchain.callbacks import get_openai_callback
from langchain.document_loaders import (
    CSVLoader,
    DirectoryLoader,
    GitLoader,
    NotebookLoader,
    OnlinePDFLoader,
    PythonLoader,
    TextLoader,
    UnstructuredFileLoader,
    UnstructuredHTMLLoader,
    UnstructuredPDFLoader,
    UnstructuredWordDocumentLoader,
    WebBaseLoader,
)

langchain.debug

load_dotenv()
app = Flask(__name__)
CORS(app)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

AUDIO_FORMAT = "audio/mp3"
# Environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
db_password = os.getenv('DB_PASSWORD')
eleven_api_key = os.getenv('ELEVEN_API_KEY')

CHUNK_SIZE = 1000

#PineCone Utils
def init_pinecone():
    pinecone_api_key = os.environ["PINECONE_API_KEY"]
    pinecone_env = os.environ["PINECONE_ENV"]

    pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)


def create_pinecone_vector(pages, index_name):
    embeddings = OpenAIEmbeddings()
    vectordb = Pinecone.from_documents(
        pages,
        embeddings,
        index_name=index_name
        )

    logger.info('Pinecone vector created!')

    return vectordb


def create_pinecone_vector_extra(texts, index_name):
    embeddings = OpenAIEmbeddings()
    vectordb = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)

    logger.info('Pinecone vector created!')

    return vectordb
# Ruta para la página de inicio
@app.route('/')
#def home():
#    return 'Welcome! This is the homepage of the Elevenlabs Hackathon podcast.'
def home():
    # Renderiza la plantilla "podcast.html" también para la ruta raíz
    return render_template('podcast.html', episode_text='')

def read_episode_text():
    try:
        with open("episode_text.txt", "r") as episode_file:
            return episode_file.read()
    except FileNotFoundError:
        print("El archivo 'episode_text.txt' no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
    return None

@app.route('/podcast')
def podcast():
    # Leer el texto del episodio desde el archivo
    episode_text = read_episode_text()

    # Renderizar la plantilla "podcast.html" y pasar el texto del episodio como parámetro
    return render_template('podcast.html', episode_text=episode_text)

def valid_url(url):
    """valid_url
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
    
# Transcribe audio using OpenAI Whisper API
def transcribe_audio(audio_file_path):
    try:
        with open(audio_file_path, "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)
        return response["text"]
    except Exception as e:
        print(f"Error calling Whisper API: {str(e)}")
        return None


   
def generate_audio(selected_text):
    # Voice using Eleven API 
    voice= "Bella" 

    # Get current timestamp 
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S") 

    # File name with timestamp 
    nombre_archivo = f"audio{timestamp}.mp3" 

    try: 
        # Generate audio using Eleven API 
        audio = generate(text=selected_text, voice=voice, api_key=eleven_api_key) 

        # Save the audio to a file 
        with open(nombre_archivo, "wb") as file: 
            file.write(audio) 

        with open(nombre_archivo, "rb") as file: 
            audio_data = file.read() 

        # Ensure to delete the audio file after sending it to the client 
        #os.remove("audio.mp3") 

        # Return the audio as a response 
        return audio_data, 200, {'Content-Type': 'audio/mpeg'} 

    except Exception as e: 
        print(str(e))
        return jsonify(message='Error retrieving the audio from ElevenLabs'), 500


# llm = OpenAI(temperature=0.9)

# texto = "Cual seria un buen nombre para una empresa de Chrochet en Chile?"
# print(texto)

# with get_openai_callback() as cb:
#     print(llm(texto))
#     print(f"Total Tokens: {cb.total_tokens}")
#     print(f"Prompt Tokens: {cb.prompt_tokens}")
#     print(f"Completion Tokens: {cb.completion_tokens}")
#     print(f"Total Cost (USD): ${cb.total_cost}")

#Snippet of code from DataChad
def load_any_data_source(data_source: str, chunk_size: int = CHUNK_SIZE
) -> List[Document]:
    # Ugly thing that decides how to load data
    # It aint much, but it's honest work
    is_text = data_source.endswith(".txt")
    is_web = data_source.startswith("http")
    is_pdf = data_source.endswith(".pdf")
    is_csv = data_source.endswith("csv")
    is_html = data_source.endswith(".html")
    is_git = data_source.endswith(".git")
    is_notebook = data_source.endswith(".ipynb")
    is_doc = data_source.endswith(".doc")
    is_py = data_source.endswith(".py")
    is_dir = os.path.isdir(data_source)
    is_file = os.path.isfile(data_source)

    loader = None
    if is_dir:
        loader = DirectoryLoader(data_source, recursive=True, silent_errors=True)
    elif is_web:
        if is_pdf:
            loader = OnlinePDFLoader(data_source)
        else:
            loader = WebBaseLoader(data_source)
    elif is_file:
        if is_text:
            loader = TextLoader(data_source, encoding="utf-8")
        elif is_notebook:
            loader = NotebookLoader(data_source)
        elif is_pdf:
            loader = UnstructuredPDFLoader(data_source)
        elif is_html:
            loader = UnstructuredHTMLLoader(data_source)
        elif is_doc:
            loader = UnstructuredWordDocumentLoader(data_source)
        elif is_csv:
            loader = CSVLoader(data_source, encoding="utf-8")
        elif is_py:
            loader = PythonLoader(data_source)
        else:
            loader = UnstructuredFileLoader(data_source)
    try:
        # Chunk size is a major trade-off parameter to control result accuracy over computaion
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=0
        )
        docs = loader.load_and_split(text_splitter)
        logger.info(f"Loaded: {len(docs)} document chucks")
        return docs
    except Exception as e:
        if loader:
            msg = str(e)
        else:
            msg = f"No Loader found for your data source. Consider contributing: {REPO_URL}!"
        # Dispara el mensaje de error directamente aquí
        print(f"Error while loading data: {msg}")
        # O realiza alguna otra acción en caso de error, si es necesario
        return []







if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

