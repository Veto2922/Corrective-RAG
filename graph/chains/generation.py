from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=api_key, 
    temperature=0.0
)


prompt = hub.pull('rlm/rag-prompt')

generation_chain = prompt | llm | StrOutputParser()