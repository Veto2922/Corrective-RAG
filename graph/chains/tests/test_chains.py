from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from ingestion import retriever 

from graph.chains.retrieval_grader import retrieval_grader , GradeDocuments
from graph.chains.generation import generation_chain



def test_tetrival_grader_answer_yes():
    """
    Test the retrieval grader with a relevant document
    """
    question = "What are the main differences between the prompt engineering techniques discussed in the blog posts?"
    documents = retriever.invoke(question)
    # print('this is our document' ,  documents)
    doc_text = documents[1].page_content
    # print('this is our filter document' ,  doc_text)
    # Test the retrieval grader with a relevant document
    res : GradeDocuments = retrieval_grader.invoke(
        {
            "document": doc_text,
            "question": question
        }
    )
    # print( "this is the grade res : " ,res)
    assert res['binary_score'] == "yes"
    
    

def test_tetrival_grader_answer_no():
    """
    Test the retrieval grader with a relevant document
    """
    question = "How to make pizza"
    documents = retriever.invoke(question)
    # print('this is our document' ,  documents)
    doc_text = documents[1].page_content
    # print('this is our filter document' ,  doc_text)
    # Test the retrieval grader with a relevant document
    res : GradeDocuments = retrieval_grader.invoke(
        {
            "document": doc_text,
            "question": question
        }
    )
    # print( "this is the grade res : " ,res)
    assert res['binary_score'] == "no"
    
    

def test_generation_chain():
    """
    Test the generation chain
    """
    question = "What are the main differences between the prompt engineering techniques discussed in the blog posts?"
    documents = retriever.invoke(question)
    # doc_text = documents[1].page_content
    res = generation_chain.invoke(
        {
            "context": documents,
            "question": question
        }
    )
    pprint(res)
    