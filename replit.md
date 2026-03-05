# Resume Screening App

## Overview
A Flask-based ML web application that screens resumes, predicts job categories, extracts skills, and stores results in a PostgreSQL database.

## Architecture
- **Backend**: Python / Flask (single-server app)
- **ML Models**: scikit-learn (pre-trained model + vectorizer in `trained_model/`)
- **Database**: Supabase PostgreSQL (via psycopg2)
- **Templates**: Jinja2 HTML templates in `templates/`
- **Static files**: CSS and JS in `static/`

## Key Files
- `app.py` — Main Flask application, routes: `/`, `/predict`, `/dashboard`
- `database.py` — PostgreSQL connection and CRUD (uses hardcoded Supabase URL)
- `process.py` — Text cleaning utilities
- `skills.py` — Skill extraction from resume text
- `utils/extract.py` — PDF/DOCX text extraction
- `model.py` / `retrain.py` — ML model training helpers
- `trained_model/` — Pre-trained `model.pkl` and `vectorizer.pkl`
- `uploads/` — Uploaded resume files (runtime)
- `dataset/` — Training data CSV

## Running the App
- **Workflow**: "Start application" → `python app.py`
- **Port**: 5000 (host: 0.0.0.0)
- **Deployment**: gunicorn via `gunicorn --bind=0.0.0.0:5000 --reuse-port app:app`

## Dependencies
Managed via `requirements.txt`:
- flask, pandas, scikit-learn, joblib, PyPDF2, python-docx, psycopg2-binary, gunicorn

## Database
External Supabase PostgreSQL — connection string hardcoded in `database.py`.
Table: `resumes` (id, resume_text, prediction, confidence, skills, upload_time)
