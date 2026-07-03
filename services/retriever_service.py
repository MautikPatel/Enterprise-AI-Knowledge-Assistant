from sentence_transformers import SentenceTransformer
import chromadb

from chromadb.config import Settings

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to existing ChromaDB
client = chromadb.PersistentClient(
    path="chroma_db",
    settings=Settings(anonymized_telemetry=False)
)

collection = client.get_collection(
    name="enterprise_documents"
)


def retrieve_chunks(question, top_k=5):
    """
    Retrieve the most relevant chunks for a user's question.
    """

    # Convert question into embedding
    question_embedding = model.encode(
        question,
        convert_to_numpy=True
    )

    # Search ChromaDB
    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=top_k
    )

    return results