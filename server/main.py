from flask import Flask, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from pinecone_utils import init_pinecone
from helpers import home, podcast
import logging
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

@app.route('/')
def index():
    return home()

@app.route('/podcast')
def get_podcast():
    return podcast()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


