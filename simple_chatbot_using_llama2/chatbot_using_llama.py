from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

### Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpfull assistant. Please respond to the user queries"),
        ("user", 'Question:{question}')
    ]
)

# Streamlit 
st.title("Langchain Demo with llama2")
input_text = st.text_input("Search the topic u want")
# genai
llm = Ollama(model='llama2')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))

