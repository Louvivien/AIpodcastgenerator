from revChatGPT.V1 import Chatbot
chatbot = Chatbot(config={
  "access_token": "token",
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