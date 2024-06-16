from typing import Dict, Any
from graph.chains.generation import generation_chain
from langchain.schema import Document
from graph.state import GraphState

def generate(state: GraphState) -> Dict[str, Any]:
    question = state["question"]
    documents = state["documents"]

    generation = generation_chain.invoke({"question": question, "context": documents})

    return {"documents": documents, "question": question, "generation": generation}

if __name__ == "__main__":

    documents = ["""Good luck with your AI projects and don’t hesitate to reach out if you need help at your company!\n--\n--\nWritten by Alex Honchar\nTowards Data Science\nCo-founder @ Neurons Lab\nHelp\nStatus\nAbout\nCareers\nBlog\nPrivacy\nTerms\nText to speech\nTeams Notice, how we can easily decompose and define separately:\nThe final definition of the agent will look as simple as this:\nAs you can see in the outputs of the script (or you can run it yourself), it solves the issue in the previous part related to tools. For example, while building the tree of thoughts prompts, I save my sub-prompts in the prompts repository and load them:\nYou can see in this notebook the result of such reasoning, the point I want to make here is the right process for defining your reasoning steps and versioning them in such an LLMOps system like Langsmith. If you prefer a narrative walkthrough, you can find the YouTube video here:\nAs always, you can find the code on GitHub, and here are separate Colab Notebooks:\nIntroduction to the agents\nLet’s begin the lecture by exploring various examples of LLM agents. Also, you can see other examples of popular reasoning techniques in public repositories like ReAct or Self-ask with search:\nOther notable approaches are:\nStep 2: Memory\nStep 3: Tools\nChatGPT Plugins and OpenAI API function calling are good examples of LLMs augmented with tool use capability working in practice.\n\nThe agent's memory has two categories: short-term and long-term memories. Short-term Memory: In context memory allows the agent to utilize the short-term memory of the large language model to operate the original problem from the beginning. This capability allows the agent to hold temporarily the information and process it when it is ...\nDownload the latest SupportAssist .msp (SupportAssistx64-4..3.61632.msp) from the Dell Downloads Catalog. Create a folder in the C drive and name it SA. Copy the downloaded .msi and .msp files to the SA folder in the C drive. Open Command Prompt as Administrator. Type msiexec /i C:\\SA\\SupportAssistx64-4...61632.msi /qb /l*v and press Enter."""]


    print(generate(state={"question": "What is a memory agent?", "documents": documents}))