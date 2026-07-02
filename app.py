import streamlit as st
import ollama

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Enterprise AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("🤖 Enterprise AI Knowledge Assistant")

st.markdown(
    "Ask anything. Responses are generated **locally** using **Llama 3.2** via **Ollama**."
)

st.divider()

# --------------------------------------------------
# User Input
# --------------------------------------------------
prompt = st.text_area(
    "Enter your question",
    height=150,
    placeholder="Example: Explain what Business Intelligence is..."
)

# --------------------------------------------------
# Ask AI
# --------------------------------------------------
if st.button("Ask AI", use_container_width=True):

    if prompt.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Thinking..."):

            response = ollama.chat(
                model="llama3.2:3b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.success("Response")

        st.write(response["message"]["content"])