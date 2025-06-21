# Streamlit Firebase Example

This repository contains a simple Streamlit application with multiple pages. The app demonstrates how to upload PDF or text files to Firebase Storage and view the uploaded files. Metadata about each upload is stored in Firestore.

## Requirements

- Python 3.9+
- Streamlit
- firebase-admin
- PyPDF2

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running the App

Run the Streamlit application from the project root:

```bash
streamlit run Home.py
```

Streamlit will automatically detect the additional pages in the `pages/` directory.

## Firebase Setup

Provide your Firebase service account details in `.streamlit/secrets.toml`. The
credentials should be placed under the `firebase` section:

```toml
[firebase]
type = "service_account"
project_id = "your-project-id"
private_key_id = "..."
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "..."
client_id = "..."
token_uri = "https://oauth2.googleapis.com/token"
```

Streamlit automatically loads these secrets and the app will use them to
initialize Firebase.

