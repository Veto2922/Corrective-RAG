from typing import Any, Dict

from langchain.schema import Document
# from langchain_community.tools import TavilySearchResults
from langchain_community.retrievers import TavilySearchAPIRetriever

import sys
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


from state import GraphState

TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")


web_search_tool = TavilySearchAPIRetriever(k=3,
                                           api_key=TAVILY_API_KEY)

search_client = TavilyClient(api_key=TAVILY_API_KEY )

def web_search(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")
    question = state["question"]
    documents = state["documents"]

    docs = search_client.search(question , max_results = 3)
    web_results = "\n".join([d['content'] for d in docs['results']])
    web_results = Document(page_content=web_results)
    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
    return {"documents": documents, "question": question}


if __name__ == "__main__":
    # state = GraphState({"question": "What is the capital of France?"})
    res =  search_client.search("What is the capital of France?" ,max_results = 3)
    print(res)
    web_results = "\n".join([d['content'] for d in res['results']])
    print(web_results)