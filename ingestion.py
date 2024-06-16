from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250,
    chunk_overlap=0
)

docs_split = text_splitter.split_documents(docs_list)

# vectorstores = Chroma.from_documents(
#     documents=docs_split, 
#     collection_name="advanced-rag",
#     embedding=OpenAIEmbeddings(),
#     persist_directory="./.chroma" 
#     )

retriever = Chroma(
    collection_name="advanced-rag",
    embedding_function=OpenAIEmbeddings(),
    persist_directory="./.chroma"
).as_retriever()