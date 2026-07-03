import streamlit as st

def show_footer():
    st.markdown(
        """
        <div class="footer">
            Enterprise AI Knowledge Assistant &nbsp;·&nbsp; Version 1.0.0 &nbsp;·&nbsp; © 2026 Mautik Patel
        </div>
        """,
        unsafe_allow_html=True
    )