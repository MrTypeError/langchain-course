from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import tavily_search


llm = ChatOpenAI()
tools = [tavily_search]
agent = create_agent(model=llm,tools=tools)

def main():
    result = agent.invoke({"messages":HumanMessage(content = "Search for 3 job posting for an AI engineer jobs using langchain in India and list their details")})
    print(result)

if __name__ == "__main__":
    main()