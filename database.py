import psycopg2
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "resume_data.db")
DATABASE_URL = "postgresql://postgres.ahpbzivlujftjpopnebt:25%40MCI10146@aws-1-ap-south-1.pooler.supabase.com:5432/postgres"
def get_connection():
    conn=psycopg2.connect(DATABASE_URL)
    return conn
def init_db():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    create table if not exists resumes (
        id SERIAL PRIMARY KEY,
        resume_text text,
        prediction text,
        confidence real,
        skills text,
        upload_time timestamp default current_timestamp
    )
    """)
    conn.commit()
    conn.close()

def save_resume(text, prediction, confidence, skills):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    insert into resumes (resume_text, prediction, confidence, skills)
    values (%s, %s, %s, %s)
    """, (text, prediction, confidence, skills))
    conn.commit()
    conn.close()

def all_resumes():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from resumes order by id asc")
    data=cursor.fetchall()
    conn.close()
    return data