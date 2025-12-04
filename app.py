from fastapi import FastAPI
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

app = FastAPI()

# Load model from HF repo
model_path = hf_hub_download(repo_id="danialsiddiqui/task6-model", filename="model.joblib")
model_data = joblib.load(model_path)
model = model_data["model"]
columns = model_data["columns"]

@app.get("/")
def home():
    return {"status": "API is running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)
    prediction = model.predict(df)[0]
    return {"prediction": float(prediction)}
