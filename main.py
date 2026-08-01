import joblib
import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Predykcja spalonych kalorii podczas treningu",
    description="System generujący predykcje z modelu drzewa decyzyjnego",
    version="1.0"
)

model = joblib.load("model_drzewa.pkl")
scaler = joblib.load("scaler.pkl")
model_columns = joblib.load("model_columns.pkl")

class PredictionInput(BaseModel):
    sport_name: str
    duration_s: float
    hr_avg: float
    training_load: float
    cardio_load: float
    recovery_time_s: float
    carbo_pct: float
    fat_pct: float
    weight_kg: float
    vo2_max: float
    resting_hr: float
    aerobic_threshold_hr: float
    anaerobic_threshold_hr: float
    age: float

@app.get("/", response_model=dict)
def root() -> dict[str, str]:
    return {
        "status" : "API działa"
    }

@app.post("/predict", response_model=dict)
def predict(data: PredictionInput) -> dict[str, str | float]:
    try:
        input_dict = data.model_dump()
        df_single = pd.DataFrame([input_dict])
        df_encoded = pd.get_dummies(df_single)
        df_aligned = df_encoded.reindex(
            columns=model_columns, 
            fill_value=0
            )
        scaled_data = scaler.transform(df_aligned)
        prediction = model.predict(scaled_data)
        
        return {
            "status": "success",
            "prediction": float(prediction[0])
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )