from pathlib import Path
import streamlit as st

from services.document_service import (
    save_uploaded_files,
    get_document_list,
)

from services.document_loader import load_all_documents
from services.chunk_service import create_chunks
from services.embedding_service import generate_embeddings

from services.vector_store_service import (
    store_embeddings,
    get_vector_count,
)


# --------------------------------------------------
# Build Knowledge Base
# --------------------------------------------------

def build_knowledge_base():

    with st.spinner("📖 Reading enterprise documents..."):

        documents = load_all_documents(
            Path("data/documents")
        )

    with st.spinner("✂️ Creating semantic chunks..."):

        chunks = create_chunks(documents)

    with st.spinner("🧠 Generating embeddings..."):

        embeddings = generate_embeddings(chunks)

    with st.spinner("💾 Updating ChromaDB..."):

        vector_count = store_embeddings(
            chunks,
            embeddings
        )

    st.session_state.documents = documents
    st.session_state.chunks = chunks
    st.session_state.knowledge_ready = True

    return (
        documents,
        chunks,
        vector_count,
    )


# --------------------------------------------------
# Administrator Dashboard
# --------------------------------------------------

def show_admin_dashboard():

    st.header("⚙️ Administrator Dashboard")

    st.caption(
        "Manage enterprise documents and maintain the Knowledge Base."
    )

    st.divider()

    documents = st.session_state.get(
        "documents",
        []
    )

    chunks = st.session_state.get(
        "chunks",
        []
    )

    try:

        vectors = get_vector_count()

    except Exception:

        vectors = 0

    total_pages = sum(
        doc.get("pages", 0)
        for doc in documents
    )

    file_types = len(
        set(
            doc.get(
                "document_type",
                "Unknown"
            )
            for doc in documents
        )
    )

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    row1 = st.columns(3)

    row1[0].metric(
    "📄 Documents",
    len(documents)
)

    row1[1].metric(
        "📚 Pages",
        total_pages
    )

    row1[2].metric(
        "🧩 Chunks",
        len(chunks)
    )

    row2 = st.columns(3)

    row2[0].metric(
        "🧠 Vectors",
        vectors
    )

    row2[1].metric(
        "📂 File Types",
        file_types
    )

    with row2[2]:

        if st.session_state.get(
            "knowledge_ready",
            False
        ):

            st.success("🟢 Ready")

        else:

            st.warning("🟡 Build Required")

    st.divider()

    # --------------------------------------------------
    # Upload Documents
    # --------------------------------------------------

    st.subheader("📤 Upload Documents")

    uploaded_files = st.file_uploader(

        "Upload enterprise documents",

        type=[
            "pdf",
            "docx",
            "pptx",
            "xlsx",
            "txt",
            "csv",
            "png",
            "jpg",
            "jpeg",
            "eml",
        ],

        accept_multiple_files=True,
    )

    upload_col1, upload_col2 = st.columns(2)

    with upload_col1:

        if st.button(
            "💾 Save Documents",
            use_container_width=True,
        ):

            if uploaded_files:

                saved = save_uploaded_files(
                    uploaded_files
                )

                st.success(
                    f"{len(saved)} document(s) uploaded successfully."
                )

            else:

                st.info(
                    "Please select one or more documents."
                )

    with upload_col2:

        if st.button(
            "🔄 Refresh",
            use_container_width=True,
        ):

            st.rerun()

    st.divider()

    # --------------------------------------------------
    # Knowledge Base
    # --------------------------------------------------

    st.subheader("🧠 Knowledge Base")

    kb_col1, kb_col2 = st.columns(2)

    with kb_col1:

        if st.button(
            "📚 Build Knowledge Base",
            use_container_width=True,
        ):

            docs, chks, vecs = build_knowledge_base()

            st.success(
                f"""
Knowledge Base Built Successfully

Documents : {len(docs)}

Chunks : {len(chks)}

Vectors : {vecs}
"""
            )

            st.rerun()

    with kb_col2:

        if st.button(
            "♻️ Rebuild Knowledge Base",
            use_container_width=True,
        ):

            docs, chks, vecs = build_knowledge_base()

            st.success(
                f"""
Knowledge Base Rebuilt Successfully

Documents : {len(docs)}

Chunks : {len(chks)}

Vectors : {vecs}
"""
            )

            st.rerun()

    st.divider()

    # --------------------------------------------------
    # Enterprise Documents
    # --------------------------------------------------

    st.subheader("📂 Enterprise Documents")

    if not documents:

        st.info(
            "No documents loaded."
        )

        return

    for document in documents:

        with st.expander(

            f"{document['document_type']} | {document['filename']}"

        ):

            col1, col2 = st.columns(2)

            with col1:

                st.write(
                    f"**Pages:** {document['pages']}"
                )

            with col2:

                st.write(
                    f"**Characters:** {len(document['text'])}"
                )

            st.text(
                document["text"][:1500]
            )