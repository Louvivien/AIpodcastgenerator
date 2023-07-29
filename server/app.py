from flask import Flask, render_template , jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import logging
import requests
import json
from utils.openai_utils import askGPT



# Load environment variables
load_dotenv()

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


