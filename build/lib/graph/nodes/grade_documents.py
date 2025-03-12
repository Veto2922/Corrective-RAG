from typing import Any , Dict
from chains.retrieval_grader import retrieval_grader

from state import GraphState


def grade_documents(state: GraphState) -> Dict[str, Any]:
    print('----CHECK DOCUMANT RELEVANCE TO QUETION')
    question = state['question']
    documents = state['documents']
    
    filtered_docs = []
    web_search = False
    
    for d in documents:
        score = retrieval_grader.invoke({'document': documents, 'question': question})

        grade = score['binary_score']
        
        if grade.lower() == 'yes':
            print('----GRADE: DOCUMENT RELEVANT')
            filtered_docs.append(d)
        else:
            print('----GRADE: DOCUMENT NOT RELEVANT')
            web_search = True
            continue
        
    return {"documents": filtered_docs , 'question': question , 'web_search': web_search}