import streamlit as st

from services.document_service import get_document_list
from services.vector_store_service import get_vector_count

APP_NAME = "Enterprise AI Knowledge Assistant"
APP_VERSION = "v1.0.0"
LLM_MODEL = "llama3.2:3b"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

def show_sidebar():
    documents = st.session_state.get("documents",[])
    document_count = len(documents)

    chunks = len(st.session_state.get("chunks", []))
    try:
        vectors = get_vector_count()
    except Exception:
        vectors = 0

    knowledge_ready = st.session_state.get("knowledge_ready", False)

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
            🧩 **Chunks:** {chunks}  
            🧠 **Vectors:** {vectors}  
            ⚡ **Status:** {"🟢 Ready" if knowledge_ready else "🟡 Pending"}
            """
        )
        st.markdown("---")

        st.markdown("#### 📁 Supported Files")
        st.markdown(
            """
            - PDF · DOCX · XLSX  
            - PPTX · TXT · CSV  
            - Email · Images
            """
        )
        st.markdown("---")

        st.caption(APP_NAME)
        st.caption("© 2026 Mautik Patel")