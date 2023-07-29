from revChatGPT.V1 import Chatbot
import os
from dotenv import load_dotenv



# Get the OPENAI_API_AUTHORIZATION from .env file
OPENAI_API_AUTHORIZATION = os.getenv('OPENAI_API_AUTHORIZATION')



chatbot = Chatbot(config={
  "access_token": OPENAI_API_AUTHORIZATION,
  "model": "gpt-4-plugins",
})
prompt = "how many beaches does portugal have?"
response = ""
for data in chatbot.ask(
  prompt
):
    response = data["message"]
print(response)



# find token here
# https://chat.openai.com/api/auth/session