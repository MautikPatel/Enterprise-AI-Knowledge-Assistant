from sentence_transformers import SentenceTransformer
import chromadb
import time
from chromadb.config import Settings

# --------------------------------------------------
# Load Embedding Model
# --------------------------------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# --------------------------------------------------
# Connect ChromaDB
# --------------------------------------------------

client = chromadb.PersistentClient(
    path="chroma_db",
    settings=Settings(
        anonymized_telemetry=False
    )
)

collection = client.get_collection(
    name="enterprise_documents"
)


def retrieve_chunks(question, top_k=8):
    """
    Retrieve the most relevant document chunks.
    """

    # -----------------------------
    # Clean question
    # -----------------------------

    question = question.strip()

    question_embedding = model.encode(
        question,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # -----------------------------
    # Semantic Search
    # -----------------------------

  

    start = time.perf_counter()

    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=top_k,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    end = time.perf_counter()

    print("=" * 60)
    print(f"Retriever Time : {end - start:.2f} seconds")
    print("=" * 60)

    return results