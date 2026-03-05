import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib as store
data=pd.read_csv("dataset/Resume_screening.csv")
X=data["Skills"]
y=data["Job Role"]
vector=TfidfVectorizer()
X_vector=vector.fit_transform(X)# fit imp words and transformtext to numbers conversion
model=MultinomialNB()
model.fit(X_vector,y)
store.dump(model, "trained_model/model.pkl")
store.dump(vector, "trained_model/vectorizer.pkl")
print("Model trained successfully!")