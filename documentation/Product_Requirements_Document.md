# Product Requirements Document (PRD)

## Feature: Policy Documents Page

### Overview
Create a new Streamlit page that displays only files categorized as "Policy" documents. This page helps users quickly find and interact with all policy-related files.

### Requirements
- The page lists all files where the `doc_category` field contains the value "Policy".
- The UI uses a multi-tab layout:
    1. **Table Tab:** Displays all Policy documents and their metadata (file name, doc_category, doc_name, file type, upload date, etc.) in a table.
    2. **Download Tab:** Allows users to select and download Policy documents.
    3. **View Tab:** Allows users to select and view the text content of Policy documents.
- Robust, configurable logging and error handling are required.
- Documentation must be kept in sync with all code changes.

### Success Criteria
- Only Policy files are shown.
- All actions (download, show text) work as expected.
- Errors are clearly displayed and logged.
