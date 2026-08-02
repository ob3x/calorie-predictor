import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Predykcja spalonych kalorii podczas treningu",
    description="System generujący predykcje z modelu drzewa decyzyjnego",
    version="1.1"
)

model = joblib.load("model_drzewa.pkl")

class PredictionInput(BaseModel):
    duration_s: float
    hr_avg: float
    training_load: float
    cardio_load: float
    recovery_time_s: float
    age: int

@app.get("/", response_model=dict)
def root() -> dict[str, str]:
    return {
        "status" : "API działa"
    }

@app.post("/predict", response_model=dict)
def predict(data: PredictionInput) -> dict[str, str | float]:
    try:
        df = pd.DataFrame([data.model_dump()])
        prediction = model.predict(df)
        
        return {
            "status": "success",
            "prediction": f"{float(prediction[0]):.2f}"
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)