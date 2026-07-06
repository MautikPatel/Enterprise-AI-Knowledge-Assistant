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


def _inject_sidebar_css():
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] > div:first-child {
            background-color: #0f1f3d;
        }
        [data-testid="stSidebar"] * {
            color: #ffffff !important;
        }
        /* st.caption() ships its own muted/low-opacity color that has higher
           specificity than the universal rule above, so it needs an explicit
           override to actually turn white (this covers APP_VERSION and
           APP_NAME captions, and any other st.caption() calls in the sidebar). */
        [data-testid="stSidebar"] [data-testid="stCaptionContainer"],
        [data-testid="stSidebar"] [data-testid="stCaptionContainer"] p,
        [data-testid="stSidebar"] small {
            color: #ffffff !important;
            opacity: 1 !important;
        }
        [data-testid="stSidebar"] hr {
            border-color: rgba(255,255,255,0.12);
        }
        .ent-sb-title {
            font-size: 19px;
            font-weight: 700;
            color: #ffffff !important;
        }
        .ent-sb-section {
            font-size: 13.5px;
            font-weight: 700;
            color: #ffffff !important;
            text-transform: uppercase;
            letter-spacing: 0.4px;
            margin-bottom: 4px;
        }
        .ent-sb-code {
            background: rgba(255,255,255,0.08);
            border-radius: 6px;
            padding: 2px 8px;
            font-family: monospace;
            font-size: 13px;
            display: inline-block;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


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

        _inject_sidebar_css()

        st.markdown(
            '<div class="ent-sb-title">🤖 Enterprise AI</div>',
            unsafe_allow_html=True,
        )

        st.caption(APP_VERSION)

        st.markdown("---")

        # st.markdown(
        #     '<div class="ent-sb-section">📊 Knowledge Base</div>',
        #     unsafe_allow_html=True,
        # )

        if knowledge_ready:
            st.success("🟢 Ready")
        else:
            st.warning("🟡 Not Built")

        st.markdown("---")

        st.markdown(
            '<div class="ent-sb-section">🧠 Models</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
**LLM**

<span class="ent-sb-code">{LLM_MODEL}</span>

**Embedding**

<span class="ent-sb-code">{EMBEDDING_MODEL}</span>

**Mode**

<span class="ent-sb-code">Local (Offline)</span>
""",
            unsafe_allow_html=True,
        )

        st.markdown("---")

        st.markdown(
            '<div class="ent-sb-section">📈 Statistics</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
📄 **Documents:** {document_count}

🧩 **Chunks:** {chunk_count}

🧠 **Vectors:** {vectors}

⚡ **Status:** {"🟢 Ready" if knowledge_ready else "🟡 Pending"}
"""
        )

        st.markdown("---")

        st.markdown(
            '<div class="ent-sb-section">📁 Supported Files</div>',
            unsafe_allow_html=True,
        )

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