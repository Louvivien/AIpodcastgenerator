import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Get the OPENAI_API_AUTHORIZATION from .env file
OPENAI_API_AUTHORIZATION = os.getenv('OPENAI_API_AUTHORIZATION')

# Replace with your actual prompt
Prompt = "Create a dialogue between two people discussing this topic:"

# Replace with your actual prompt
GPT_SERVER_URL = os.getenv('GPT_SERVER_URL')

def extractGPT(input):
    print('Sending request to ChatGPT...')
    
    headers = {
        'Authorization': OPENAI_API_AUTHORIZATION,
        'Content-Type': 'application/json'
    }
    
    data = {
        "action": "next",
        "messages": [
            {
                "id": "cd465ab7-3ee4-40e7-8e48-ade9926ad68e",
                "role": "user",
                "content": {
                    "content_type": "text",
                    "parts": [
                        Prompt+ '\n\n' + input
                    ]
                }
            }
        ],
        "parent_message_id": "572aca1b-59e5-4262-85b6-b258fa5a38b8",
        "model": "gpt-4-plugins",
        "temperature": 0,
        "stream": "false",
        "plugin_ids": [
            "plugin-8701f253-5910-4d4c-8057-8265b1ec587e",
            "plugin-f4c74dea-7bee-4f77-9717-34668bbd05b9",
            "plugin-ec68cb54-acee-4330-8d94-f97b8347d525"
        ]
    }
    
    response = requests.post(GPT_SERVER_URL + "/api/conversation", headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        response_data = response.json()
        full_message = response_data.get('data', '')
        
        content = full_message.get('content', {})
        parts = content.get('parts', [])
        
        result = '\n'.join(parts)
        print('fullMessage', '\n' + result)
        
        return result
    else:
        print('Request Error: check keys and cookies', response.status_code)
        return None


