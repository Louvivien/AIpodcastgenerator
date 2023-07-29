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
import langchain
import logging

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
# Ruta para la página del podcast
@app.route('/podcast')
def podcast():
    # Simulación del texto del episodio
    episode_text = """
Title: The Hilarious Quest for the Quantum Cupcake

[Introduction Music]

Host (H): Welcome, everyone, to another exciting episode of "Science Shenanigans"! I'm your host, Dr. Chuckles, and today, we have two brilliant guests joining us to delve into the mind-bending world of quantum physics. First up, we have Dr. Sparkle, a quantum physicist with a flair for humor.

Dr. Sparkle (S): Thanks for having me, Dr. Chuckles! I promise we won't get too entangled in our discussions today.

H: [Laughs] I'm already entangled with laughter! And our second guest is Dr. Witty, a theoretical physicist known for her witty remarks and out-of-this-world theories.

Dr. Witty (W): Oh, you flatter me, Dr. Chuckles! I've been theorizing about the quantum origins of dad jokes lately.

H: [Laughs] That sounds both enlightening and entertaining! So, let's dive right into it - quantum physics and cupcakes. Dr. Sparkle, is there any connection between the two?

S: Well, you see, in the quantum world, things can be in multiple states at once - like a cupcake being both chocolate and vanilla simultaneously!

W: Ah, the elusive "chocanilla" cupcake! I've been trying to find that flavor all my life.

H: [Laughs] Quantum cupcake cravings aside, can you explain superposition for our listeners?

S: Absolutely! Superposition is like Schrödinger's cat being both alive and dead until you open the box. But with cupcakes, it's like having all the flavors in the bakery display until you pick one.

W: So, in theory, I can have all the cupcakes and none of the guilt? Sign me up!

H: [Laughs] The dream of every dessert enthusiast! Now, let's talk about quantum entanglement. Is it like getting your headphones tangled, but on a subatomic level?

S: That's a perfect analogy! Imagine two entangled particles behaving like your earphones, except when you untangle them, their states remain correlated, no matter the distance.

W: It's like the universe's way of saying, "No matter how far apart you are, you're stuck together!"

H: [Laughs] Quantum entanglement - the ultimate cosmic relationship status! And what about quantum computing?

S: Ah, quantum computing is like having an army of cupcake-hungry ants exploring all the flavors at the same time, hoping to find the tastiest one!

W: And when they finally find it, it's like the Eureka moment of having that "Aha!" after a perfect punchline!

H: [Laughs] Brilliant! A cupcake-loving ant army exploring flavors - I'd pay to see that! Now, let's talk about the many-worlds interpretation.

S: Ah, the multiverse of cupcakes! In one universe, the cupcake is devoured in one bite, while in another, it's savored in infinite nibbles.

W: And in yet another universe, someone's on a perpetual diet, forever denied the joy of cupcakes.

H: [Laughs] Poor them! I'd never want to live in that universe. And finally, the big question - can you quantum teleport a cupcake?

S: In theory, you could, but I'm afraid you might end up with a cupcake splattered across the lab walls.

W: But what a tasty mess that would be!

H: [Laughs] Indeed! It's like a baking disaster of cosmic proportions. Now, before we wrap up, any final thoughts?

S: Remember, folks, science doesn't have to be all serious. Embrace the humor, and you'll find the universe has a great sense of humor too.

W: And never stop asking questions, even if they seem as absurd as searching for a quantum cupcake.

H: [Laughs] Wise words from two quantum jesters! Thank you, Dr. Sparkle and Dr. Witty, for an enlightening and amusing discussion.

S: Thank you for having us, Dr. Chuckles. It was a quantum delight!

W: Indeed, an experience worth superimposing on! Keep exploring, everyone!

[Outro Music]

H: And that's a wrap, folks! Join us next time for more "Science Shenanigans." Until then, stay curious and keep laughing!
    """

    # Renderiza la plantilla "podcast.html" y pasa el texto del episodio como parámetro
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



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

