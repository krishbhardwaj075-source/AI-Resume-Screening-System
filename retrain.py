import pandas as pd
import sqlite3 as db
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# database path
DB_PATH = os.path.join(BASE_DIR, "resume_data.db")

DATASET_PATH = os.path.join(BASE_DIR, "dataset", "Resume_Screening.csv")

MODEL_PATH = os.path.join(BASE_DIR, "trained_model", "model.pkl")
VEC_PATH = os.path.join(BASE_DIR, "trained_model", "vectorizer.pkl")

data=pd.read_csv(DATASET_PATH)
conn=db.connect(DB_PATH)
db_data = pd.read_sql_query(
    "SELECT resume_text, prediction FROM resumes",
    conn
)
conn.close()
db_data.columns=["Skills","Job Role"]

combine_data=pd.concat([data,db_data], ignore_index=True)

X=combine_data["Skills"]
y=combine_data["Job Role"]

vector=TfidfVectorizer()
X_vector=vector.fit_transform(X)

model=MultinomialNB()
model.fit(X_vector,y)

joblib.dump(model, MODEL_PATH)
joblib.dump(vector, VEC_PATH)
print("Model retrained successfully with new data!")