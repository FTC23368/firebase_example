import streamlit as st
from firebase_app import list_files, get_file_content, get_text_content
import pandas as pd

st.title("Policy Documents")

files = list_files()
policy_files = [f for f in files if "Policy" in (f.get("doc_category") or [])]

if not policy_files:
    st.info("No Policy documents found.")
else:
    tabs = st.tabs(["Table", "Download", "View"])

    # Tab 1: Table
    with tabs[0]:
        try:
            df = pd.DataFrame(policy_files)
            # Only show key columns if present
            columns = [c for c in ["file_name", "doc_category", "doc_name", "file_type", "uploaded_at", "file_size"] if c in df.columns]
            st.dataframe(df[columns])
        except Exception as e:
            st.error(f"Failed to display table: {e}")

    # Tab 2: Download
    with tabs[1]:
        try:
            names = [f.get("file_name", "") for f in policy_files]
            selected = st.selectbox("Select a file to download", names)
            if selected:
                file = next((f for f in policy_files if f.get("file_name") == selected), None)
                if file:
                    data = get_file_content(file.get("file_name", ""))
                    st.download_button(
                        label="Download",
                        data=data,
                        file_name=file.get("file_name", "file"),
                        mime=file.get("file_type", "application/octet-stream"),
                    )
        except Exception as e:
            st.error(f"Download failed: {e}")

    # Tab 3: View
    with tabs[2]:
        try:
            names = [f.get("file_name", "") for f in policy_files]
            selected = st.selectbox("Select a file to view", names, key="view_select")
            if selected:
                file = next((f for f in policy_files if f.get("file_name") == selected), None)
                if file:
                    text = get_text_content(file.get("file_name", ""))
                    st.text_area("File Text", text, height=300)
        except Exception as e:
            st.error(f"Failed to load text: {e}")
