from flask import Flask, render_template , jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import logging
import requests
import json
from utils.openai_utils import askGPT
import openai
import os
import youtube_transcript_api
from youtube_transcript_api.formatters import TextFormatter



# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

## Routes for frontend
@app.route('/')
def welcome():
    return render_template('home.html')



@app.route('/send_content', methods=['POST'])
def send_content():

    content = request.get_json().get('content')
    
    if 'youtu.be' in content or 'youtube.com' in content:
      video_id = content[content.find('.be/')+4:] if 'youtu.be' in content else content[content.find('?v=')+3:]
      srt = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_id)
      formatter = TextFormatter()
      text_formatted = (formatter.format_transcript(srt)).replace("\n"," ").split()
      text_formatted = text_formatted[:15000]
      text_formatted = ' '.join(text_formatted)
      prompt = f"Make a dialogue between two people (give them names) for a podcast based on the following content, make this fun and entertaining, less robotic and more natural, here is the content : {text_formatted}"
      result = askGPT(prompt)
      print(result)
      # Return the result from the askGPT function
      return jsonify({'status': 'success', 'result': result})

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
      prompt = f"Make a dialogue between two people (give them names) for a podcast about the content of the following article, make this fun and entertaining, here is the article content : {article}"
      result = askGPT(prompt)

      print(result)

      # Return the result from the askGPT function
      return jsonify({'status': 'success', 'result': result})



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


