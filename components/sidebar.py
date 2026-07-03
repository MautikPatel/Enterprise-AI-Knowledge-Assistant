import streamlit as st

from services.document_loader import get_loaded_documents
from services.chunk_service import create_chunks

from services.vector_store_service import (
    get_vector_count,
    knowledge_base_ready,
)

APP_NAME = "Enterprise AI Knowledge Assistant"
APP_VERSION = "v1.0.0"

LLM_MODEL = "qwen2.5:3b"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

def show_sidebar():

    # -----------------------------------------
    # Load current Knowledge Base information
    # -----------------------------------------

    documents = get_loaded_documents()

    document_count = len(documents)

    chunks = create_chunks(documents)

    chunk_count = len(chunks)

    try:
        vectors = get_vector_count()
    except Exception:
        vectors = 0

    knowledge_ready = knowledge_base_ready()

    # -----------------------------------------
    # Sidebar UI
    # -----------------------------------------

    with st.sidebar:

        st.markdown("## 🤖 Enterprise AI")

        st.caption(APP_VERSION)

        st.markdown("---")

        st.markdown("#### 📊 Knowledge Base")

        if knowledge_ready:
            st.success("🟢 Ready")
        else:
            st.warning("🟡 Not Built")

        st.markdown("---")

        st.markdown("#### 🧠 Models")

        st.markdown(
            f"""
**LLM**

`{LLM_MODEL}`

**Embedding**

`{EMBEDDING_MODEL}`

**Mode**

`Local (Offline)`
"""
        )

        st.markdown("---")

        st.markdown("#### 📈 Statistics")

        st.markdown(
            f"""
📄 **Documents:** {document_count}

🧩 **Chunks:** {chunk_count}

🧠 **Vectors:** {vectors}

⚡ **Status:** {"🟢 Ready" if knowledge_ready else "🟡 Pending"}
"""
        )

        st.markdown("---")

        st.markdown("#### 📁 Supported Files")

        st.markdown(
            """
- PDF
- DOCX
- XLSX
- PPTX
- TXT
- CSV
- EML
- Images
"""
        )

        st.markdown("---")

        st.caption(APP_NAME)

        st.caption("© 2026 Mautik Patel")