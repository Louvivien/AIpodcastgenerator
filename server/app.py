from flask import Flask, send_from_directory, request, jsonify, session, send_file
import io
from flask_cors import CORS
from dotenv import load_dotenv
import logging
import requests
import json
from utils.openai_utils import askGPT
from utils.elevenlabs_utils import *
import openai
import os
import youtube_transcript_api
from youtube_transcript_api.formatters import TextFormatter
from elevenlabs import set_api_key
from flask_cors import CORS, cross_origin








# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
set_api_key(os.getenv('ELEVEN_API_KEY'))

app = Flask(__name__, static_folder=os.path.abspath("./client/build"))
cors = CORS(app)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

# ## Routes for frontend
# @app.route('/')
# def welcome():
#     return render_template('home.html')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        print(f"Serving index.html from {app.static_folder}")
        return send_from_directory(app.static_folder, 'index.html')
    




@app.route('/send_content', methods=['POST'])
def send_content():

    data = request.get_json()
    content = data.get('content')
    
    if 'youtu.be' in content or 'youtube.com' in content:
      video_id = content[content.find('.be/')+4:] if 'youtu.be' in content else content[content.find('?v=')+3:]
      srt = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_id)
      formatter = TextFormatter()
      text_formatted = (formatter.format_transcript(srt)).replace("\n"," ").split()
      text_formatted = text_formatted[:15000]
      text_formatted = ' '.join(text_formatted)
      prompt = f"Make a dialogue between two people (give them names {data['speaker1']} and {data['speaker2']} respectively) for a podcast based on the following content, make this fun and entertaining, less robotic and more natural, here is the content : {text_formatted}"
      result = askGPT(prompt)
      print(result)

      response = generate_audio(result, data['speaker1'], data['speaker2'],
                     data.get('speaker1_age'), data.get('speaker2_age'),
                     data.get('speaker1_gender'), data.get('speaker2_gender'),
                     data.get('speaker1_accent'), data.get('speaker2_accent'),
                     data.get('speaker1_voice_name'), data.get('speaker2_voice_name'))

      # Return the result from the askGPT function
      if response:
          return jsonify({'status': 'success', 'result': result})
      else:
          return jsonify({'status': 'error', 'result': 'Failed to generate audio'})

    else:

      # API call
      url = "https://webreader.webpilotai.com/api/visit-web"

      payload = json.dumps({
        "link": content,  # replace hardcoded URL with content
        "lp": True,
        "ur": "",
        "l": "en",
        "rt": False
      })
      headers = {
        'WebPilot-Friend-UID': 'hello',
        'Content-Type': 'application/json'
      }
      response = requests.request("POST", url, headers=headers, data=payload)
      article = response.text
      
      # Call the ChatGPT
      prompt = f"Make a dialogue between two people (give them names {data['speaker1']} and {data['speaker2']} respectively) for a podcast about the content of the following article, make this fun and entertaining, here is the article content : {article}"
      result = askGPT(prompt)

      print(result)

      response = generate_audio(result, data['speaker1'], data['speaker2'],
                     data.get('speaker1_age'), data.get('speaker2_age'),
                     data.get('speaker1_gender'), data.get('speaker2_gender'),
                     data.get('speaker1_accent'), data.get('speaker2_accent'),
                     data.get('speaker1_voice_name'), data.get('speaker2_voice_name'))

      if response:
          return jsonify({'status': 'success', 'result': result})
      else:
          return jsonify({'status': 'error', 'result': 'Failed to generate audio'})

@cross_origin()
@app.route('/download_audio', methods=['GET'])
def download_audio():
    
    audio_file_path = 'podcast.mp3'
    # Set the response content type to 'audio/mpeg'
    headers = {
        'Content-Type': 'audio/mpeg',
        'Content-Disposition': 'attachment; filename=audio_file.mp3'
    }

    # Send the file-like object as a response with appropriate headers
    return send_file(audio_file_path, mimetype='audio/mp3', as_attachment=True)


@cross_origin()
@app.route('/voices', methods=['GET'])
def get_voices():

    data = get_all_voices()
    return jsonify(data.get('voices'))


@app.route('/voices/<voice_id>', methods=['GET'])
def get_voice_by_id(voice_id):

    data = get_voice(voice_id)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
