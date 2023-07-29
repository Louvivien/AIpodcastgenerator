


from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools import AIPluginTool
from langchain.agents.agent_toolkits import NLAToolkit
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


llm = ChatOpenAI(temperature=0)
tools = NLAToolkit.from_llm_and_url(llm, "https://webreader.webpilotai.com/openapi.yaml").get_tools()
memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent_chain = initialize_agent(tools, llm, agent="chat-conversational-react-description", verbose=True, memory=memory)
print(agent_chain.run("What is this: https://en.wikipedia.org/wiki/Marcia_Reale"))



