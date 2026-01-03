from fastapi import FastAPI
import joblib
import os
import numpy as np
from api.schema import DiabetesInput


# -------------------------------------------------------------------
# Initialize FastAPI application with metadata for automatic docs
# -------------------------------------------------------------------
app = FastAPI(
    title="Diabetes Prediction API",
    description="Predicts diabetes outcome using a trained Logistic Regression model",
    version="1.0.0"
)

# -------------------------------------------------------------------
# Resolve paths to model and scaler artifacts
# -------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "..", "artifacts", "diabetes_lr_model.joblib")
SCALER_PATH = os.path.join(BASE_DIR, "..", "artifacts", "standard_scaler.joblib")

# -------------------------------------------------------------------
# Load trained model and fitted scaler
# -------------------------------------------------------------------
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# -------------------------------------------------------------------
# Health check endpoint
# -------------------------------------------------------------------
@app.get("/")
def health_check():
    return {"status": "API is running"}

# -------------------------------------------------------------------
# Prediction endpoint
# -------------------------------------------------------------------
@app.post("/predict")
def predict(input_data: DiabetesInput):
    """
    Generate diabetes prediction based on patient input markers.

    Parameters
    ----------
    input_data : DiabetesInput
        Validated input schema containing patient health markers.

    Returns
    -------
    dict
        Dictionary containing predicted class and probability.
    """

    # Convert input data to NumPy array (raw values)
    X = np.array([[
        input_data.pregnancies,
        input_data.glucose,
        input_data.blood_pressure,
        input_data.skin_thickness,
        input_data.insulin,
        input_data.bmi,
        input_data.diabetes_pedigree,
        input_data.age
    ]])

    # Apply the SAME scaler used during training
    X_scaled = scaler.transform(X)

    # Generate prediction and probability
    prediction = model.predict(X_scaled)[0]
    probability = model.predict_proba(X_scaled)[0][1]

    return {
        "prediction": int(prediction),
        "probability": round(float(probability), 4)
    }

