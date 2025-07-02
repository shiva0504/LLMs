from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2" ]="true"


prompt=ChatPromptTemplate.from_messages(
    [
        ("Give answer whne i asked a question"),
        ("user","Question:{question}")
    ]
)

st.title('Langchain with Local LLama using OLlam - Gemma 3')
input_text=st.text_input("Enter the topic")

# Local model
llm=Ollama(model="Gemma:latest")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

