import streamlit as st
import requests

def get_openapi_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={"input":{"topic":input_text}})
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/song/invoke",
    json={"input":{"topic":input_text}})
    return response.json()['output']['content']

st.title("Langchain openai and ollam")
input_text_openai=st.text_input("write essay topic")
input_text_ollama=st.text_input("write song topic")

if input_text_openai:
    st.write(get_openapi_response(input_text_openai))
if input_text_ollama:
    st.write(get_ollama_response(input_text_ollama))