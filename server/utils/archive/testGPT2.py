from gpt4_openai import GPT4OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Get the OPENAI_API_AUTHORIZATION from .env file
OPENAI_API_AUTHORIZATION = os.getenv('OPENAI_API_AUTHORIZATION')

# accessToken from https://chat.openai.com/api/auth/session
llm = GPT4OpenAI(token=OPENAI_API_AUTHORIZATION, model='gpt-4-plugins')
# ChatGPT will first browse the web for the name/age of her boyfriend, then return the answer
response = llm('What is the age difference between Dua Lipa and her boyfriend?')
print(response)


# find token here
# https://chat.openai.com/api/auth/session