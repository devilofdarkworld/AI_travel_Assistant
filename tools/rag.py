from langchain.tools import tool
# from rag import load_vector_store
from rag import create_vector_store

@tool
def search_destinations(query: str) -> str:
    """
    Search for destinations using FAISS based on user query.
    """
    db = create_vector_store()
    results = db.similarity_search(query, k=10)
    if results:
        return results[0].page_content
    return "No matching destination found."
