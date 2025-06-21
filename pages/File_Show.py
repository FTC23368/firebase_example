import streamlit as st

from firebase_app import list_files, get_file_content, get_text_content

st.title("Uploaded Files")

files = list_files()

if not files:
    st.info("No files uploaded yet.")
else:
    for file in files:
        st.subheader(file["file_name"])
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Download {file['file_name']}"):
                data = get_file_content(file["file_name"])
                st.download_button(
                    label="Download",
                    data=data,
                    file_name=file["file_name"],
                    mime=file["file_type"],
                )
        with col2:
            if st.button(f"Show text for {file['file_name']}"):
                text = get_text_content(file["file_name"])
                st.text_area("File Text", text, height=200)

