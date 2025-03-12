from typing import Any , Dict

from graph.state import GraphState
from ingestion import retriever



def retrieve(state: GraphState) -> Dict[str, Any]:
    """
    Retrieve documents from the retriever
    """
    question = state["question"]
    documents = retriever.invoke(question)
    
    return {"documents": documents , 'question': question}