import sys
sys.path.append("C:\\advanced_rag")
from pprint import pprint
from ingestion import retriever
from graph.chains.retrieve_grader import GradeDocuments, retrieval_grader
from graph.chains.generation import generation_chain
from dotenv import load_dotenv

load_dotenv()


def test_retrival_grader_answer_yes() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": question, "document": doc_txt}
    )

    assert res.binary_score == "yes"

def test_retrival_grader_answer_no() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": "How to make a cake?", "document": doc_txt}
    )

    assert res.binary_score == "no"