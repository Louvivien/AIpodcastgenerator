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
from langchain.schema import Document
from typing import List
import logging
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

logger = logging.getLogger()

CHUNK_SIZE = 1000

#Snippet of Code from DataChad, the mate in DeepLake
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
            msg = f"No Loader found for your data source. Thanks to DataChad"
        # Dispara el mensaje de error directamente aquí
        print(f"Error while loading data: {msg}")
        # O realiza alguna otra acción en caso de error, si es necesario
        return []
