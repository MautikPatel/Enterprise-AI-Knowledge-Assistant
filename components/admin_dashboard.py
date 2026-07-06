from pathlib import Path
import streamlit as st

from services.document_service import (
    save_uploaded_files,
    get_document_list,
)

from services.document_loader import (
    load_all_documents,
    get_loaded_documents,
)

from services.chunk_service import create_chunks
from services.embedding_service import generate_embeddings

from services.vector_store_service import (
    store_embeddings,
    get_vector_count,
    knowledge_base_ready,
)

from components.document_inventory import show_document_inventory

# --------------------------------------------------
# Enterprise-style CSS (visual only)
# --------------------------------------------------

def _inject_admin_css():
    st.markdown(
        """
        <style>
        .ent-metric-card {
            background: #ffffff;
            border: 1px solid #eef0f4;
            border-radius: 14px;
            padding: 18px 20px;
            box-shadow: 0 1px 3px rgba(16, 24, 40, 0.06);
            height: 100%;
        }
        .ent-metric-label {
            font-size: 13px;
            font-weight: 600;
            color: #6b7280;
            margin-bottom: 6px;
        }
        .ent-metric-value {
            font-size: 30px;
            font-weight: 700;
            color: #111827;
            line-height: 1.1;
        }
        .ent-section-title {
            font-size: 20px;
            font-weight: 700;
            color: #111827;
            margin-bottom: 2px;
        }
        .ent-section-caption {
            color: #6b7280;
            font-size: 13.5px;
            margin-bottom: 10px;
        }
        div[data-testid="stButton"] > button {
            border-radius: 8px;
            font-weight: 600;
            border: 1px solid #e5e7eb;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _metric_card(label, value):
    st.markdown(
        f"""
        <div class="ent-metric-card">
            <div class="ent-metric-label">{label}</div>
            <div class="ent-metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True,
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



    return (
        documents,
        chunks,
        vector_count,
    )


# --------------------------------------------------
# Administrator Dashboard
# --------------------------------------------------

def show_admin_dashboard():

    _inject_admin_css()

    st.markdown(
        '<div class="ent-section-title">⚙️ Administrator Dashboard</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="ent-section-caption">Manage enterprise documents and maintain the Knowledge Base.</div>',
        unsafe_allow_html=True,
    )

    # Always load current documents from disk

    documents = get_loaded_documents()

    # Always regenerate chunks

    chunks = create_chunks(documents)

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

    with row1[0]:
        _metric_card("📄 Documents", len(documents))

    with row1[1]:
        _metric_card("📚 Pages", total_pages)

    with row1[2]:
        _metric_card("🧩 Chunks", len(chunks))

    st.write("")

    row2 = st.columns(3)

    with row2[0]:
        _metric_card("🧠 Vectors", vectors)

    with row2[1]:
        _metric_card("📂 File Types", file_types)

    with row2[2]:

        if knowledge_base_ready():

            st.success("🟢 Ready")

        else:

            st.warning("🟡 Build Required")

    st.divider()

    # --------------------------------------------------
    # Upload Documents
    # --------------------------------------------------

    st.markdown(
        '<div class="ent-section-title" style="font-size:18px;">📤 Upload Documents</div>',
        unsafe_allow_html=True,
    )

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

    st.markdown(
        '<div class="ent-section-title" style="font-size:18px;">🧠 Knowledge Base</div>',
        unsafe_allow_html=True,
    )

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

    show_document_inventory()
