from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load your trained model
model = joblib.load("model.joblib")

# Initialize FastAPI app
app = FastAPI(title="Supermarket Sales Forecast API")

# Define input schema (replace with actual model features)
class SalesInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
def predict(data: SalesInput):
    # Convert input to array for prediction
    input_data = np.array([[data.feature1, data.feature2, data.feature3]])
    prediction = model.predict(input_data)
    return {"prediction": prediction.tolist()}
