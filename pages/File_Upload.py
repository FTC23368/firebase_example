import streamlit as st

from firebase_app import upload_file

st.title("Upload a File")

uploaded = st.file_uploader("Choose a PDF or text file", type=["pdf", "txt"])

if uploaded is not None:
    file_bytes = uploaded.read()
    file_type = uploaded.type
    filename = uploaded.name

    if st.button("Upload to Firebase"):
        try:
            upload_file(file_bytes, filename, file_type)
            st.success(f"Uploaded {filename} to Firebase Storage")
        except Exception as e:
            st.error(f"Failed to upload: {e}")
