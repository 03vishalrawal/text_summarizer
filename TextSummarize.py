from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)
from dotenv import load_dotenv


import os

load_dotenv()

print("API Key loaded?", os.getenv("OPEN_API_KEY") is not None)


text = """Text summarization is the process of distilling the most important information 
from a text into a shorter version. In practical terms, this means creating a brief but 
informative summary of long-form content like research papers, podcasts, news articles, 
or even meeting notes."""

chat_messages = [
    SystemMessage(content="You are an expert assistant in technical understandings summarization."),
    HumanMessage(content=f"Please provide me a summary of the document {text}")
]

llm = ChatOpenAI(api_key=os.getenv("OPEN_API_KEY"), model="gpt-4o-mini", temperature=0)

print(llm.get_num_tokens)

# Run the chat model
response = llm.invoke(chat_messages)

print(response.content)