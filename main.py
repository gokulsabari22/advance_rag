from dotenv import load_dotenv
from graph.graph import app

load_dotenv()

def run_llm(question: str):
    result = app.invoke(input={"question": question})
    return result["generation"]

if __name__ == "__main__":
    print("Hello Advanced RAG\n")
    print(run_llm(question="What is agent memory?"))