import streamlit as st

st.set_page_config(page_title="Firebase Example", page_icon="\U0001f4c2")

st.title("Welcome to the Firebase File Uploader")

st.markdown(
    """
    ## Instructions
    
    - Use **File Upload** page to upload PDF or text files.
    - Uploaded files will be stored in Firebase Storage and referenced from Firestore.
    - A plain text version of the file is also stored in Storage with the extension `.content`.
    - Navigate to **File Show** page to list uploaded files, download them or read their text content.
    
    Ensure you have added your Firebase service account information to
    `st.secrets['firebase']` in `.streamlit/secrets.toml` before running this
    app.
    """
)
