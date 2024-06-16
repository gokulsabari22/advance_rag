from typing import Dict, Any
from langchain.schema import Document
from langchain_community.tools.tavily_search import TavilySearchResults
from graph.state import GraphState
from dotenv import load_dotenv

websearch_tool = TavilySearchResults(max_results=3)

def web_search(state: GraphState) -> Dict[str, Any]:
    question = state["question"]
    documents = state["documents"]

    tavily_results = websearch_tool.invoke({"query": question})

    joined_tavily_results = "\n".join(
        [tavily_result["content"] for tavily_result in tavily_results]
    )
    web_results = Document(page_content=joined_tavily_results)

    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]

    return {"documents": documents, "question": question}

if __name__ == "__main__":
    print(web_search(state={"question": "What is agent memory", "documents": None}))