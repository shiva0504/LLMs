from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv
load_dotenv()


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2" ]="true"

print ("sadas", os.getenv("OPENAI_API_KEY"))
app=FastAPI(
   title="Langcahin Server",
   version="1.0",
   description="Api server"
)
add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model=ChatOpenAI(model="gpt-4o-mini")
# Ollama gemma:3b
llm=Ollama(model="gemma:3b")

promtp1=ChatPromptTemplate.from_template("write an essay on {topic} in 100 words")
promtp2=ChatPromptTemplate.from_template("write a song on {topic} in 100 words")  

add_routes(
    app,
    promtp1|model,
    path="/essay"
)
add_routes(
    app,
    promtp2|model,
    path="/song"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)