import os
import json
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

# ✅ Load environment variables
load_dotenv()

# ✅ Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_store(json_path="data/destination.json", save_path="vectorstore/"):
    """
    Load travel destination data from a JSON file, convert to LangChain Document objects,
    split into chunks, embed using HuggingFace, and save FAISS vector store to disk.
    
    Args:
        json_path (str): Path to the input JSON file.
        save_path (str): Directory path where the FAISS index will be saved.
    
    Returns:
        FAISS: A FAISS vector store instance.
    """
    print("🔍 Loading JSON manually...")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # ✅ Convert each JSON object to a Document
    docs = [
        Document(
            page_content=json.dumps(item, ensure_ascii=False),  # Store as readable string
            metadata={
                "name": item.get("name"),
                "country": item.get("country"),
                "type": item.get("type"),
                "tags": item.get("tags", [])
            }
        )
        for item in data
    ]

    print("✂️ Splitting documents...")
    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=20)
    chunks = splitter.split_documents(docs)

    print("💡 Embedding with Hugging Face...")
    vectorstore = FAISS.from_documents(chunks, embedding_model)

    print(f"💾 Saving FAISS index to '{save_path}'...")
    vectorstore.save_local(save_path)
    print("✅ FAISS vector store created.")
    return vectorstore

def load_vector_store(load_path="vectorstore/"):
    """
    Load an existing FAISS vector store from disk with safe deserialization.
    Only do this if you're sure the FAISS index is from a trusted source.
    """
    print(f"📥 Loading FAISS store from '{load_path}'...")
    return FAISS.load_local(
        load_path,
        embeddings=embedding_model,
        allow_dangerous_deserialization=True  # ✅ Add this flag
    )


# -------------------------
# Example usage (Uncomment to run)
# -------------------------
