from dotenv import load_dotenv

from langgraph.graph import END, StateGraph

from .consts import GENERATE, GRADE_DOCUMENTS, RETRIEVE, WEBSEARCH
from .nodes.retrieve import retrieve
from .nodes.grade_documents import grade_documents
from .nodes.generate import generate
from .nodes.web_search import web_search
from .state import GraphState

load_dotenv()



def decide_to_generate(state):
    print("---ASSESS GRADED DOCUMENTS---")

    if state["web_search"]:
        print(
            "---DECISION: NOT ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, INCLUDE WEB SEARCH---"
        )
        return WEBSEARCH
    else:
        print("---DECISION: GENERATE---")
        return GENERATE



print("retrieve = " , retrieve)
print("grade_documents = " , grade_documents)
print("generate = " , generate)
print("web_search = " , web_search)
print("decide_to_generate = " , decide_to_generate )

workflow = StateGraph(GraphState)
workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, web_search)

workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)



workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    decide_to_generate,
    {
        WEBSEARCH: WEBSEARCH,
        GENERATE: GENERATE,
    },
)

workflow.add_edge(WEBSEARCH, GENERATE)

workflow.add_edge(GENERATE, END)

app = workflow.compile()

# app.get_graph().draw_mermaid_png(output_file_path="graph.png")
