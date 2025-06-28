import streamlit as st

from firebase_app import upload_file

st.title("Upload a File")

doc_category=st.multiselect("Select all categories that apply", ["Policy", "Product", "Other"])
doc_name=st.text_input("Document Name",value="")

uploaded = st.file_uploader("Choose a PDF or text file", type=["pdf", "txt"])

if uploaded is not None:
    file_bytes = uploaded.read()
    file_type = uploaded.type
    filename = uploaded.name

    if st.button("Upload to Firebase"):
        try:
            upload_file(file_bytes, filename, file_type, doc_category, doc_name)
            st.success(f"Uploaded {filename=}, {file_type=}, {doc_category=}, {doc_name=} to Firebase Storage")
        except Exception as e:
            st.error(f"Failed to upload: {e}")
