import streamlit as st
import subprocess
import sys
import os
import time

st.set_page_config(
    page_title="Proxy Scraper & Checker",
    layout="centered"
)

st.title("🕵️ Proxy Scraper, Parser & Checker")
st.write("Live proxy scraping with source updates.")

st.warning("⚠️ This process may take time. Output updates live below.")

# Placeholder for live logs
log_box = st.empty()

if st.button("🚀 Run Proxy Tool"):
    logs = ""

    process = subprocess.Popen(
        [sys.executable, "main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    for line in process.stdout:
        logs += line
        log_box.text(logs)
        time.sleep(0.05)  # helps Streamlit refresh smoothly

    process.wait()

    st.success("Process finished!")

# Download section
st.divider()
st.subheader("⬇️ Download Files")

files_found = False

for file_name in ["proxies.txt", "working_proxies.txt", "output.txt"]:
    if os.path.exists(file_name):
        files_found = True
        with open(file_name, "r") as f:
            st.download_button(
                label=f"Download {file_name}",
                data=f.read(),
                file_name=file_name
            )

if not files_found:
    st.info("No proxy files found yet. Run the tool first.")
