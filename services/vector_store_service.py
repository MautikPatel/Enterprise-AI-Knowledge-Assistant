import chromadb
from chromadb.config import Settings

client = chromadb.PersistentClient(
    path="chroma_db",
    settings=Settings(anonymized_telemetry=False)
)

collection = client.get_or_create_collection(
    name="enterprise_documents"
)


def store_embeddings(chunks, embeddings):
    """
    Store document chunks and embeddings in ChromaDB.
    """

    collection.upsert(
        ids=[
            f"{chunk['filename']}_{chunk['chunk_id']}"
            for chunk in chunks
        ],

        documents=[
            chunk["text"]
            for chunk in chunks
        ],

        embeddings=embeddings.tolist(),

        metadatas=[
            {
                "filename": chunk["filename"],
                "chunk_id": chunk["chunk_id"],
                "document_type": chunk.get("document_type", "")
            }
            for chunk in chunks
        ]
    )

    return collection.count()


def get_vector_count():
    """
    Returns total vectors stored in ChromaDB.
    """

    return collection.count()


def clear_vector_database():
    """
    Delete all vectors.
    """

    client.delete_collection("enterprise_documents")

    global collection

    collection = client.get_or_create_collection(
        name="enterprise_documents"
    )