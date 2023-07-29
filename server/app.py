from flask import Flask, render_template , jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import logging
from utils.ChatGPTplugins import extractGPT


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
    # Call the extractGPT function with the content
    result = extractGPT(content)
    print(result)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


