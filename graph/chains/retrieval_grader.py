from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel , Field
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=api_key, 
    temperature=0.0
)


class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""

    binary_score: str = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )
    
parser = JsonOutputParser(pydantic_object=GradeDocuments)    



system = """You are a grader assessing relevance of a retrieved document to a user question. \n 
    If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant. \n
    Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""
grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Retrieved document: \n\n {document} \n\n User question: {question} \n\n {format_instructions}"),
    ]
).partial(format_instructions=parser.get_format_instructions())
    
    


retrieval_grader = grade_prompt | llm | parser



if __name__ == "__main__":
    res= retrieval_grader.invoke({
        "question":"What is the main character in the novel 'Pride and Prejudice'?",
        "document":"Pride and Prejudice is a romantic novel by Jane Austen, published in 1813. The novel follows the story of Mr. Darcy and Mrs. Bennet, two married couples who fall in love during the 18th century."
    }
    )
    
    print("this is our result : " ,res)
    
    