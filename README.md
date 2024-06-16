# advance_rag

Implemented Advanced RAG to provide answer based on user query.

Flow Diagram:

![Flow Diagram graph](https://github.com/gokulsabari22/advance_rag/assets/57941940/e022d475-420d-4447-8a1d-9f5ad071b6bc)


The provided workflow diagram outlines the sequential process for handling document retrieval, grading, and content generation with optional web searching. Below is a detailed description of each step:

1) Start: The process begins with the initialization step.

2) Retrieve: In this step, the required documents or data are retrieved from a specified source.

3) Grade Document: The retrieved documents are then graded or evaluated based on predefined criteria.

4) Websearch (Optional): If additional information is needed, a web search is performed. This step is conditional and may not occur in every workflow execution.

5) Generate: Based on the graded documents and any additional information gathered from the web search, new content or results are generated.

6) End: The process concludes with the completion of content generation, marking the end of the workflow.

This flow ensures a systematic approach to document handling, allowing for optional information enhancement through web searches before final content generation.


Environment Variables

1) OPENAI_API_KEY
2) TAVILY_API_KEY
3) LANGCHAIN_API_KEY

Vector Database Used

Chroma DB

Output

Question asked:

What is agent memory?

Generated answer:
![Screenshot 2024-06-16 223002](https://github.com/gokulsabari22/advance_rag/assets/57941940/ef830e6b-0382-4150-b72a-19929e434107)
