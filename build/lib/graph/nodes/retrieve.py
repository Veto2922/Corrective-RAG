from typing import Any , Dict



import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from state import GraphState
from ingestion import retriever



def retrieve(state: GraphState) -> Dict[str, Any]:
    """
    Retrieve documents from the retriever
    """
    question = state["question"]
    documents = retriever.invoke(question)
    
    return {"documents": documents , 'question': question}