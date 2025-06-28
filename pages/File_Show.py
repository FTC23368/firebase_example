import streamlit as st

from firebase_app import list_files, get_file_content, get_text_content

st.title("Uploaded Files")

files = list_files()

if not files:
    st.info("No files uploaded yet.")
else:
    for file in files:
        st.subheader(file.get("file_name", "Unnamed File"))
        doc_category = file.get("doc_category", [])
        doc_name = file.get("doc_name", "")
        st.markdown(f"**Category:** {', '.join(doc_category) if doc_category else 'None'}")
        st.markdown(f"**Document Name:** {doc_name if doc_name else 'None'}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Download {file.get('file_name', 'file')}"):
                try:
                    data = get_file_content(file.get("file_name", ""))
                    st.download_button(
                        label="Download",
                        data=data,
                        file_name=file.get("file_name", "file"),
                        mime=file.get("file_type", "application/octet-stream"),
                    )
                except Exception as e:
                    st.error(f"Download failed: {e}")
        with col2:
            if st.button(f"Show text for {file.get('file_name', 'file')}"):
                try:
                    text = get_text_content(file.get("file_name", ""))
                    st.text_area("File Text", text, height=200)
                except Exception as e:
                    st.error(f"Failed to load text: {e}")
