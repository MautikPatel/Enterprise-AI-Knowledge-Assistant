import streamlit as st

from services.retriever_service import retrieve_chunks
from services.llm_service import generate_answer
from components.source_cards import show_source_cards
from services.vector_store_service import knowledge_base_ready


def _inject_chat_css():
    st.markdown(
        """
        <style>
        /* ---------- Centered conversation column (ChatGPT/Claude style) ---------- */
        .main .block-container {
            max-width: 840px;
            padding-top: 1.5rem;
            padding-bottom: 7rem; /* room above the sticky input */
        }

        /* ---------- Header ---------- */
        .ent-chat-title {
            font-size: 22px;
            font-weight: 700;
            color: #111827;
            margin-bottom: 0px;
        }
        .ent-chat-caption {
            color: #6b7280;
            font-size: 13.5px;
        }
        .ent-chat-header-divider {
            border: none;
            border-bottom: 1px solid #e5e7eb;
            margin: 14px 0 22px 0;
        }

        /* Clear-chat button styled as a quiet ghost icon button */
        div[data-testid="stButton"] > button {
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            background: #ffffff;
            color: #6b7280;
        }
        div[data-testid="stButton"] > button:hover {
            border-color: #d1d5db;
            color: #111827;
        }

        /* ---------- Chat message bubbles ---------- */
        div[data-testid="stChatMessage"] {
            background: transparent;
            padding: 10px 0;
            margin-bottom: 2px;
        }

        /* User bubble: right-aligned light card (Claude/ChatGPT user style) */
        div[data-testid="stChatMessage"][aria-label*="user" i] {
            display: flex;
            flex-direction: row-reverse;
        }
        div[data-testid="stChatMessage"][aria-label*="user" i] div[data-testid="stChatMessageContent"] {
            background: #f4f5f7;
            border-radius: 18px;
            padding: 10px 16px;
            max-width: 75%;
            margin-left: auto;
        }
        div[data-testid="stChatMessage"][aria-label*="user" i] div[data-testid="stChatMessageAvatarUser"] {
            background: #111827 !important;
        }

        /* Assistant message: plain, full-width, generous line height (no bubble) */
        div[data-testid="stChatMessage"][aria-label*="assistant" i] div[data-testid="stChatMessageContent"] {
            max-width: 100%;
            padding: 4px 2px;
        }
        div[data-testid="stChatMessage"][aria-label*="assistant" i] div[data-testid="stChatMessageAvatarAssistant"],
        div[data-testid="stChatMessage"][aria-label*="assistant" i] [data-testid^="stChatMessageAvatar"] {
            background: #1E2761 !important;
        }

        /* Message text typography */
        div[data-testid="stChatMessageContent"] p {
            font-size: 15.5px;
            line-height: 1.7;
            color: #1f2430;
            margin-bottom: 0.5em;
        }

        /* ---------- Status / info messages (searching, generating) ---------- */
        div[data-testid="stAlert"] {
            background: #f8f9fb;
            border: 1px solid #eef0f4;
            border-radius: 10px;
            color: #6b7280;
            font-size: 13.5px;
            padding: 8px 14px;
        }

        /* ---------- Sticky bottom bar that docks the chat input ---------- */
        /* This is the floating footer Streamlit renders st.chat_input into.
           By default it spans ~full main-content width; we match it to the
           same narrow column as the messages above, and give it its own
           solid background so it reads as a docked bar (not overlapping text). */
        div[data-testid="stBottom"] > div {
            background: #ffffff;
            border-top: 1px solid #e5e7eb;
        }
        div[data-testid="stBottom"] .block-container {
            max-width: 840px;
            padding-top: 0.75rem;
            padding-bottom: 0.75rem;
        }

        /* ---------- Chat input: pill shape ---------- */
        div[data-testid="stChatInput"] textarea {
            border-radius: 24px !important;
        }
        div[data-testid="stChatInput"] > div {
            border-radius: 24px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 2px 10px rgba(16, 24, 40, 0.06);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_chat():
    _inject_chat_css()

    col1, col2 = st.columns([8, 1])
    with col1:
        st.markdown(
            '<div class="ent-chat-title">💬 Enterprise AI Assistant</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="ent-chat-caption">Ask questions about your enterprise knowledge base.</div>',
            unsafe_allow_html=True,
        )
    with col2:
        if st.button("🗑️", help="Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    st.markdown('<hr class="ent-chat-header-divider">', unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ---- Render full conversation history first ----
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # ---- If the latest message is a user question awaiting a reply,
    #      answer it here — still *before* the input widget below, so the
    #      new question and its "Generating response..." status always
    #      render above the chat box, never below it. ----
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        prompt = st.session_state.messages[-1]["content"]

        if not knowledge_base_ready():
            answer = (
                "⚠️ Knowledge Base has not been built yet.\n\n"
                "Go to the **Administrator** tab and click **Build Knowledge Base**."
            )
            with st.chat_message("assistant"):
                st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        else:
            with st.chat_message("assistant"):
                status = st.empty()
                status.info("🔍 Searching enterprise knowledge base...")
                try:
                    results = retrieve_chunks(prompt)
                except Exception as ex:
                    status.error(str(ex))
                    st.session_state.messages.append(
                        {"role": "assistant", "content": f"Unable to retrieve results.\n\n{str(ex)}"}
                    )
                    results = None

                if results is not None:
                    status.info("🧠 Generating response...")
                    try:
                        answer = generate_answer(prompt, results)
                    except Exception as ex:
                        answer = f"Unable to generate answer.\n\n{str(ex)}"
                    status.empty()

                    st.markdown(answer)
                    show_source_cards(results)

                    st.session_state.messages.append({"role": "assistant", "content": answer})

    # ---- Input box is always the last thing rendered -> stays pinned at the bottom ----
    prompt = st.chat_input("Ask a question about your enterprise documents...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.rerun()