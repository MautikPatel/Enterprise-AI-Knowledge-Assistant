import streamlit as st

def show_footer():
    st.markdown(
        """
        <style>
        .footer {
            background-color: #0f1f3d;
            color: #e5e7eb;
            text-align: center;
            padding: 14px 10px;
            border-radius: 8px;
            font-size: 13.5px;
            font-weight: 500;
            letter-spacing: 0.2px;
            margin-top: 10px;
        }
        </style>
        <div class="footer">
            Enterprise AI Knowledge Assistant &nbsp;·&nbsp; Version 1.0.0 &nbsp;·&nbsp; © 2026 Mautik Patel
        </div>
        """,
        unsafe_allow_html=True
    )
