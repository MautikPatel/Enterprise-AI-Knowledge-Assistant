import streamlit as st

from services.document_loader import get_loaded_documents
from services.chunk_service import create_chunks


def show_document_inventory():
    """
    Display all indexed enterprise documents.
    """

    documents = get_loaded_documents()

    if not documents:
        st.info("No enterprise documents found.")
        return

    chunks = create_chunks(documents)

    chunk_lookup = {}

    for chunk in chunks:

        filename = chunk["filename"]

        chunk_lookup[filename] = (
            chunk_lookup.get(filename, 0) + 1
        )

    st.subheader("📂 Enterprise Document Inventory")

    st.caption(
        f"{len(documents)} document(s) available."
    )

    header = st.columns([5, 1.2, 1, 1, 1.5])

    header[0].markdown("**Document**")
    header[1].markdown("**Type**")
    header[2].markdown("**Pages**")
    header[3].markdown("**Chunks**")
    header[4].markdown("**Status**")

    st.divider()

    for document in documents:

        filename = document["filename"]

        row = st.columns([5, 1.2, 1, 1, 1.5])

        row[0].markdown(f"📄 {filename}")

        row[1].markdown(
            document["document_type"]
        )

        row[2].markdown(
            str(document["pages"])
        )

        row[3].markdown(
            str(
                chunk_lookup.get(
                    filename,
                    0
                )
            )
        )

        row[4].success("Indexed")