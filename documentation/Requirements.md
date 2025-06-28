# Requirements Document

## Overview
The application allows users to upload PDF or text files to Firebase Storage, with metadata stored in Firestore. Each file has associated metadata fields including `doc_category` and `doc_name`, which must be displayed on the File_Show page.

## Requirements
- Users can upload PDF or text files.
- Each upload must capture and store:
    - File name
    - File type
    - File size
    - Upload timestamp
    - `doc_category` (list of categories)
    - `doc_name` (string)
- The File_Show page must display all files, including their `doc_category` and `doc_name` fields.
- The application must provide robust error handling and logging, configurable by level and destination.
- Documentation must be kept in sync with all code changes.
