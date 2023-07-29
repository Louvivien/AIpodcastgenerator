from urllib.parse import urlparse
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone
import pinecone
import os
import logging

logger = logging.getLogger()

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

