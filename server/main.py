from flask import Flask, render_template , jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from pinecone_utils import init_pinecone
from helpers import home, podcast
import logging
from audio_transcription import transcribe_audio
from CAMELAgent import run_conversation

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

@app.route('/conversation', methods=['POST'])
def conversation():
    data = request.get_json()
    assistant_role_name = data.get('assistant_role_name', "AI expert")
    user_role_name = data.get('user_role_name', "podcast host")
    task = data.get('task', "Make a dialogue for a podcast between 2 people about the latest AI news")
    chat_turn_limit = data.get('chat_turn_limit', 10)

    conversation, cost_data = run_conversation(assistant_role_name, user_role_name, task, chat_turn_limit)
    return jsonify({"conversation": conversation, "cost_data": cost_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


