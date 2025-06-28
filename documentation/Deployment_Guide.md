# Deployment Guide: Policy Documents Page

## Prerequisites
- Python 3.9+
- Streamlit
- Firebase project with Firestore and Storage enabled
- All dependencies in `requirements.txt` installed
- Firebase credentials in `.streamlit/secrets.toml`

## Adding the Policy Documents Page
1. Ensure the file `pages/Policy_Documents.py` exists in the `pages/` directory.
2. The page will automatically appear in the Streamlit sidebar when running the app.

## Running the App
```bash
streamlit run Home.py
```

## Logging and Error Handling
- Logging level and destination are configurable via Streamlit settings.
- All errors and info messages are shown in the UI for easy debugging.

## Troubleshooting
- If Policy documents do not appear, ensure files are uploaded with `doc_category` including "Policy".
- Check Firebase credentials and network connection if data fails to load.
