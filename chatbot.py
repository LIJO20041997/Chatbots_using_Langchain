from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
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
st.title("Langchain Demo with Gemini")
input_text = st.text_input("Search the topic u want")
# genai
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))