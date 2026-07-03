import streamlit as st

from components.sidebar import show_sidebar
from components.chat_ui import show_chat
from components.admin_dashboard import show_admin_dashboard
from components.footer import show_footer

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Enterprise AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# Global UI Styling (Light Theme, Compact Layout)
# --------------------------------------------------
st.markdown("""
<style>
    /* ----- Global ----- */
    html, body, .stApp {
        background-color: #f8f9fa;
        color: #1e1e1e;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* ----- Headings ----- */
    h1, h2, h3, h4, h5, h6 {
        font-weight: 500;
        letter-spacing: -0.02em;
        color: #1a1a1a;
    }
    h1 { font-size: 2.2rem; }
    h2 { font-size: 1.8rem; }
    h3 { font-size: 1.4rem; }
    h4 { font-size: 1.1rem; }

    /* Reduce spacing around main title */
    .stMarkdown h1 {
        margin-bottom: 0.2rem !important;
    }
    .stMarkdown .stCaption {
        margin-top: -0.2rem !important;
        margin-bottom: 0.2rem !important;
    }

    /* ----- Captions ----- */
    .stCaption, .stCaption p {
        color: #6c757d;
        font-size: 0.85rem;
    }

    /* ----- Sidebar ----- */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e9ecef;
    }
    section[data-testid="stSidebar"] .block-container {
        padding: 1rem 1rem 0.5rem 1rem !important;  /* reduced top/bottom */
    }
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] h4 {
        color: #1a1a1a;
        margin-top: 0.1rem !important;
        margin-bottom: 0.1rem !important;
    }
    section[data-testid="stSidebar"] p {
        color: #495057;
        margin-bottom: 0.05rem !important;
    }
    /* Sidebar horizontal rules */
    section[data-testid="stSidebar"] hr {
        border-color: #e9ecef;
        margin: 0.4rem 0 !important;   /* reduced spacing */
    }
    section[data-testid="stSidebar"] .stAlert {
        padding: 0.3rem 0.8rem;
        border-radius: 8px;
        background-color: #f1f3f5;
        border: 1px solid #dee2e6;
        color: #212529;
        margin-top: 0.1rem !important;
        margin-bottom: 0.1rem !important;
    }
    section[data-testid="stSidebar"] .stMetric {
        background-color: #f8f9fa;
        padding: 0.4rem;
        border-radius: 8px;
        border: 1px solid #e9ecef;
        margin-bottom: 0.2rem !important;
    }
    section[data-testid="stSidebar"] .stMetric label {
        color: #6c757d;
    }
    section[data-testid="stSidebar"] .stMetric div {
        color: #212529;
    }
    /* Sidebar captions (footer) */
    section[data-testid="stSidebar"] .stCaption {
        margin-top: 0.1rem !important;
        margin-bottom: 0.1rem !important;
    }

    /* ----- Main Content Area ----- */
    .block-container {
        padding: 1rem 2rem 1rem 2rem !important;  /* reduced top/bottom */
        max-width: 1200px;
        background-color: #f8f9fa;
    }

    /* ----- Tabs ----- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background-color: transparent;
        border-bottom: 1px solid #dee2e6;
    }
    .stTabs [data-baseweb="tab"] {
        height: 2.8rem;  /* slightly shorter */
        border-radius: 8px 8px 0 0;
        background-color: transparent;
        color: #495057;
        font-weight: 500;
        padding: 0 1.2rem;
        border: none;
        transition: all 0.2s;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #e9ecef;
        color: #212529;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        color: #0d6efd !important;
        border-bottom: 2px solid #0d6efd;
    }

    /* ----- Buttons ----- */
    .stButton button {
        background: linear-gradient(135deg, #0d6efd, #0a58ca);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 500;
        padding: 0.4rem 1.2rem;  /* reduced padding */
        transition: all 0.2s ease;
        box-shadow: 0 2px 4px rgba(13, 110, 253, 0.2);
    }
    .stButton button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(13, 110, 253, 0.3);
        background: linear-gradient(135deg, #0a58ca, #084298);
    }
    .stButton button:active {
        transform: translateY(0);
    }
    .stButton button:focus {
        outline: none;
        box-shadow: 0 0 0 3px rgba(13, 110, 253, 0.4);
    }
    .stButton button[kind="secondary"] {
        background: #f8f9fa;
        color: #212529;
        box-shadow: none;
        border: 1px solid #dee2e6;
    }
    .stButton button[kind="secondary"]:hover {
        background: #e9ecef;
        box-shadow: none;
    }

    /* ----- Chat Input ----- */
    .stChatInput input {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        border-radius: 20px;
        padding: 0.6rem 1.2rem;  /* reduced padding */
        color: #1e1e1e;
        font-size: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .stChatInput input:focus {
        border-color: #0d6efd;
        box-shadow: 0 0 0 3px rgba(13, 110, 253, 0.2);
    }

    /* ----- Chat Messages ----- */
    .stChatMessage {
        padding: 0.3rem 0 !important;  /* reduced vertical padding */
    }
    .stChatMessage [data-testid="stChatMessageContent"] {
        background-color: transparent;
        color: #1e1e1e;
    }
    /* User message */
    .stChatMessage[data-testid="user"] [data-testid="stChatMessageContent"] {
        background-color: #e7f3ff;
        border-radius: 18px 18px 4px 18px;
        padding: 0.6rem 1.2rem;  /* reduced */
        max-width: 80%;
        margin-left: auto;
        border: 1px solid #cfe2ff;
    }
    /* Assistant message */
    .stChatMessage[data-testid="assistant"] [data-testid="stChatMessageContent"] {
        background-color: #ffffff;
        border-radius: 18px 18px 18px 4px;
        padding: 0.6rem 1.2rem;
        max-width: 80%;
        margin-right: auto;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    /* Avatars */
    .stChatMessage [data-testid="stChatMessageAvatar"] {
        width: 28px;
        height: 28px;
        border-radius: 50%;
        background-color: #e9ecef;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.9rem;
    }

    /* ----- Metrics (Admin) ----- */
    .stMetric {
        background-color: #ffffff;
        border: 1px solid #e9ecef;
        border-radius: 12px;
        padding: 0.8rem 0.5rem;  /* reduced */
        text-align: center;
        transition: all 0.2s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .stMetric:hover {
        border-color: #0d6efd;
        box-shadow: 0 4px 12px rgba(13, 110, 253, 0.08);
    }
    .stMetric label {
        color: #6c757d;
        font-weight: 400;
        font-size: 0.9rem;
    }
    .stMetric div[data-testid="stMetricValue"] {
        color: #212529;
        font-size: 1.8rem;
        font-weight: 600;
    }

    /* ----- Expanders (Admin doc browser) ----- */
    .streamlit-expanderHeader {
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #dee2e6;
        color: #212529;
        font-weight: 500;
        padding: 0.4rem 1rem;  /* reduced */
    }
    .streamlit-expanderHeader:hover {
        background-color: #f8f9fa;
        border-color: #0d6efd;
    }
    .streamlit-expanderContent {
        background-color: #ffffff;
        border-radius: 0 0 8px 8px;
        border-left: 1px solid #dee2e6;
        border-right: 1px solid #dee2e6;
        border-bottom: 1px solid #dee2e6;
        padding: 0.8rem;  /* reduced */
    }

    /* ----- Source Cards ----- */
    div[data-testid="stContainer"] {
        background-color: #ffffff;
        border: 1px solid #e9ecef;
        border-radius: 12px;
        padding: 0.8rem;  /* reduced */
        margin-bottom: 0.6rem;  /* reduced */
        transition: all 0.2s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    div[data-testid="stContainer"]:hover {
        border-color: #0d6efd;
        box-shadow: 0 2px 12px rgba(13, 110, 253, 0.06);
    }

    /* ----- Dividers (main content) ----- */
    hr {
        border-color: #e9ecef;
        margin: 1rem 0 !important;  /* reduced */
    }

    /* ----- Status indicators (Admin) ----- */
    .stAlert {
        border-radius: 8px;
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        color: #212529;
        padding: 0.4rem 0.8rem !important;
        margin: 0.2rem 0 !important;
    }
    .stAlert svg {
        fill: #0d6efd;
    }

    /* ----- Footer ----- */
    .footer {
        color: #00000;
        font-size: 0.8rem;
        text-align: center;
        margin-top: 1.5rem;
        border-top: 1px solid #e9ecef;
        padding-top: 0.8rem;
    }

    /* ----- Scrollbar ----- */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #f8f9fa;
    }
    ::-webkit-scrollbar-thumb {
        background: #ced4da;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #adb5bd;
    }

    /* ----- Misc tweaks ----- */
    .stTextInput > div > div > input {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        color: #1e1e1e;
        border-radius: 8px;
    }
    .stSelectbox > div > div {
        background-color: #ffffff;
        color: #1e1e1e;
    }
    .stFileUploader > div > button {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        color: #212529;
    }
    .stFileUploader > div > button:hover {
        background-color: #e9ecef;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Session State
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "documents" not in st.session_state:
    st.session_state.documents = []
if "chunks" not in st.session_state:
    st.session_state.chunks = []
from services.vector_store_service import get_vector_count

if "knowledge_ready" not in st.session_state:
    try:
        st.session_state.knowledge_ready = get_vector_count() > 0
    except Exception:
        st.session_state.knowledge_ready = False

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
show_sidebar()

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🤖 Enterprise AI Knowledge Assistant")
st.caption("Private • Secure • Local Retrieval-Augmented Generation (RAG)")
st.divider()

# --------------------------------------------------
# Main Tabs
# --------------------------------------------------
tab_chat, tab_admin = st.tabs(["👤 End User", "⚙️ Administrator"])

with tab_chat:
    show_chat()

with tab_admin:
    show_admin_dashboard()

# --------------------------------------------------
# Footer
# --------------------------------------------------
show_footer()