from flask import Flask, render_template, request
from utils.extract import extract
from process import clean_text
from skills import extract_skills
from database import init_db, save_resume, all_resumes
import os
import joblib
model=joblib.load("trained_model/model.pkl")
vectorizer=joblib.load("trained_model/vectorizer.pkl")
app=Flask(__name__)
init_db()
base_dir=os.path.dirname(os.path.abspath(__file__))
upload_folder=os.path.join(base_dir, "uploads")
app.config["upload_folder"]=upload_folder
os.makedirs(upload_folder, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    
    if "resume" not in request.files:
        return "no file uploaded"
    
    file=request.files["resume"]
    if file.filename=="":
        return "no file selected"
    
    allowed_ext = {".pdf", ".doc", ".docx"}
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in allowed_ext:
        return "Only PDF and Word documents are allowed!"
    
    file_path=os.path.join(app.config["upload_folder"], file.filename)
    file.save(file_path)

    text=extract(file_path)
    cleaned_text=clean_text(text)

    # Perform prediction using the loaded model
    text_vector=vectorizer.transform([cleaned_text])
    prediction=model.predict(text_vector)[0]
    #confidence checker
    probability=model.predict_proba(text_vector)
    confidence= float(round(max(probability[0])*100, 2))
    #skills
    skills = extract_skills(cleaned_text)
    #database save
    save_resume(text, prediction, confidence, ", ".join(skills))
    return render_template("result.html", prediction=prediction, confidence=confidence, skills=skills)
#dashboard route
@app.route("/dashboard")
def dashboard():
    resumes = all_resumes()
    return render_template("dashboard.html", resumes=resumes)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)