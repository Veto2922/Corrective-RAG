from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

import os

api_key = os.environ.get("GEMINI_API_KEY")


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=api_key,
)

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]


docs =  [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, chunk_overlap=0
)

docs_splits = text_splitter.split_documents(docs_list)

# vectorstore = Chroma.from_documents(
#     documents=docs_splits,
#     collection_name="rag-chroma",
#     embedding=embeddings,
#     persist_directory="./.chroma",
# )

retriever = Chroma(
    collection_name="rag-chroma",
    persist_directory=".chroma",
    embedding_function=embeddings,
).as_retriever()


if __name__ == "__main__":
    query = "What are the main differences between the prompt engineering techniques discussed in the blog posts?"

    res =  retriever.invoke(query)

    print(res)
