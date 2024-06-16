from typing import Dict, Any
from graph.state import GraphState
from ingestion import retriever

def retrieve(state: GraphState) -> Dict[str, Any]:
    question = state["question"]
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}

if __name__ == "__main__":
    res = retrieve(state={"question": "What is the use of memory agents?"})
    print(res)