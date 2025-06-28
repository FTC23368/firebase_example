# Engineering Design Document (EDD)

## Feature: Policy Documents Page

### Overview
This page filters and displays only files with `doc_category` containing "Policy". The logic and UI will reuse the pattern from File_Show for consistency and maintainability.

### Design
- **Data Retrieval:** Use the existing `list_files()` function to get all files and filter in Python for those where `"Policy" in doc_category`.
- **UI Structure:**
    - Use Streamlit's `st.tabs` to create three tabs:
        1. **Table Tab:** Display all Policy documents and their metadata in a table using `st.dataframe` or similar. Columns: file name, doc_category, doc_name, file type, upload date, etc.
        2. **Download Tab:** Allow users to select a Policy document from a dropdown and download it. Use `st.download_button`.
        3. **View Tab:** Allow users to select a Policy document from a dropdown and view its text content. Use `st.text_area`.
- **Error Handling:**
    - If no policy documents are found, display an informative message in all tabs.
    - All file operations (download, show text) are wrapped in try/except blocks with errors shown via Streamlit and logged.
- **Logging:**
    - Use Streamlit's logging configuration for all error/info messages.
    - Logging level and destination are configurable via app settings.
- **Extensibility:**
    - The filtering logic can be easily adapted for other categories if needed.
- **Documentation:**
    - Update PRD, EDD, Deployment Guide, and User Guide for this new page.

### Risks & Mitigations
- **Risk:** doc_category may be missing or not a list.
    - **Mitigation:** Use `.get("doc_category", [])` and handle gracefully.
