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
# Load trained model artifact
# Path is resolved dynamically to ensure portability
# -------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "artifacts", "diabetes_lr_model.joblib")

model = joblib.load(MODEL_PATH)

# -------------------------------------------------------------------
# Health check endpoint
# Used to verify that the API is running
# -------------------------------------------------------------------
@app.get("/")
def health_check():
    return {"status": "API is running"}

# -------------------------------------------------------------------
# Prediction endpoint
# Accepts structured patient input and returns prediction + probability
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

    # Convert input data to NumPy array in the order expected by the model
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

    # Generate prediction and probability using the trained model
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]

    return {
        "prediction": int(prediction),
        "probability": round(float(probability), 4)
    }
