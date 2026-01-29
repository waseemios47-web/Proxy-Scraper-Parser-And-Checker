import streamlit as st
import subprocess
import sys

st.set_page_config(
    page_title="Proxy Scraper & Checker",
    layout="centered"
)

st.title("🕵️ Proxy Scraper, Parser & Checker")
st.write("Run the proxy tool from a web interface.")

st.warning(
    "⚠️ This process may take some time depending on proxy sources."
)

if st.button("🚀 Run Proxy Tool"):
    with st.spinner("Running proxy scraper..."):
        result = subprocess.run(
            [sys.executable, "main.py"],
            capture_output=True,
            text=True
        )

    st.success("Process finished!")

    if result.stdout:
        st.subheader("📤 Output")
        st.code(result.stdout)

    if result.stderr:
        st.subheader("❌ Errors")
        st.code(result.stderr)
