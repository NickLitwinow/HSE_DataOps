import pickle
from pathlib import Path

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from starlette_exporter import PrometheusMiddleware, handle_metrics

app = FastAPI(title="Diabetes Prediction Service")

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

MODEL_PATH = Path(__file__).parent / "model" / "model.pkl"

model = None


class PatientData(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float


class PredictResponse(BaseModel):
    predict: float


@app.on_event("startup")
def load_model():
    global model
    if MODEL_PATH.exists():
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    else:
        print(f"WARNING: Model not found at {MODEL_PATH}. Using dummy predictions.")


@app.post("/api/v1/predict", response_model=PredictResponse)
def predict(data: PatientData):
    features = np.array(
        [[data.age, data.sex, data.bmi, data.bp,
          data.s1, data.s2, data.s3, data.s4, data.s5, data.s6]]
    )
    if model is not None:
        prediction = model.predict(features)[0]
    else:
        prediction = 154.55
    return PredictResponse(predict=round(float(prediction), 2))
