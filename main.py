from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

def main():

    information = """
    Avul Pakir Jainulabdeen Abdul Kalam (15 October 1931 – 27 July 2015) was an Indian aerospace scientist and statesman who served as the president of India from 2002 to 2007.
    """

    summary_template = """
Given the {information} about a person I want to create:

1. A short summary
2. Two interesting facts about them
"""

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    # llm = ChatOpenAI(
    #     temperature=0,
    #     model="gpt-5"
    # )

    llm = ChatOllama(
        temperature=0,
        model="gemma3:270m"
    )

    chain = summary_prompt_template | llm

    response = chain.invoke(
        {"information": information}
    )

    print(response.content)


if __name__ == "__main__":
    main()