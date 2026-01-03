from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import joblib
import os
import numpy as np
from api.schema import DiabetesInput

# --------------------------------------------------
# Crear FastAPI app
# --------------------------------------------------
app = FastAPI(
    title="Diabetes Prediction with Logistic Regression",
    description="Simple diabetes risk checker",
    version="1.0"
)

# --------------------------------------------------
# Rutas a modelo y scaler
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "..", "artifacts", "diabetes_lr_model.joblib")
SCALER_PATH = os.path.join(BASE_DIR, "..", "artifacts", "standard_scaler.joblib")

# --------------------------------------------------
# Cargar modelo y scaler
# --------------------------------------------------
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# --------------------------------------------------
# Interfaz web amigable y moderna
# --------------------------------------------------
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Diabetes Prediction</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #83a4d4, #b6fbff);
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                padding: 20px;
            }
            .card {
                background: white;
                padding: 40px 30px;
                border-radius: 15px;
                width: 100%;
                max-width: 450px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                text-align: center;
                /* padding horizontal interno para que los inputs no lleguen al borde */
                box-sizing: border-box;
            }
            h2 {
                margin-bottom: 25px;
                color: #333;
            }
            input {
                width: 90%;  /* antes era 100%, ahora ocupa un poco menos */
                max-width: 400px; /* opcional para asegurar que no crezca demasiado en pantallas grandes */
                padding: 12px;
                margin: 8px 0;
                border-radius: 8px;
                border: 1px solid #ccc;
                font-size: 16px;
            }
            button {
                width: 90%;  /* igual que los inputs */
                max-width: 400px;
                padding: 14px;
                margin-top: 15px;
                font-size: 18px;
                font-weight: bold;
                color: white;
                background: #007bff;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover {
                background: #0056b3;
            }
            .result {
                margin-top: 20px;
                padding: 15px;
                border-radius: 10px;
                font-size: 20px;
                font-weight: bold;
                display: none;
            }
            .diabetes {
                background: #ffdddd;
                color: #b30000;
            }
            .no-diabetes {
                background: #ddffdd;
                color: #006600;
            }
            @media (max-width: 480px) {
                .card { padding: 30px 20px; }
                input { font-size: 14px; padding: 10px; width: 95%; }
                button { font-size: 16px; padding: 12px; width: 95%; }
                .result { font-size: 18px; padding: 12px; }
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Diabetes Prediction</h2>

            <input id="pregnancies" type="number" placeholder="Pregnancies">
            <input id="glucose" type="number" placeholder="Glucose">
            <input id="blood_pressure" type="number" placeholder="Blood Pressure">
            <input id="skin_thickness" type="number" placeholder="Skin Thickness">
            <input id="insulin" type="number" placeholder="Insulin">
            <input id="bmi" type="number" step="0.1" placeholder="BMI">
            <input id="diabetes_pedigree" type="number" step="0.01" placeholder="Diabetes Pedigree">
            <input id="age" type="number" placeholder="Age">

            <button onclick="predict()">Check Diabetes Risk</button>

            <div class="result" id="result"></div>
        </div>

        <script>
            async function predict() {
                const data = {
                    pregnancies: Number(document.getElementById("pregnancies").value),
                    glucose: Number(document.getElementById("glucose").value),
                    blood_pressure: Number(document.getElementById("blood_pressure").value),
                    skin_thickness: Number(document.getElementById("skin_thickness").value),
                    insulin: Number(document.getElementById("insulin").value),
                    bmi: Number(document.getElementById("bmi").value),
                    diabetes_pedigree: Number(document.getElementById("diabetes_pedigree").value),
                    age: Number(document.getElementById("age").value)
                };

                const response = await fetch("/predict", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                const box = document.getElementById("result");
                box.style.display = "block";

                if (result.result === "Diabetes") {
                    box.className = "result diabetes";
                } else {
                    box.className = "result no-diabetes";
                }

                box.innerHTML = result.result + "<br>Probability: " + (result.probability * 100).toFixed(1) + "%";
            }
        </script>
    </body>
    </html>
    """

# --------------------------------------------------
# Endpoint de predicción
# --------------------------------------------------
@app.post("/predict")
def predict(input_data: DiabetesInput):

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

    X_scaled = scaler.transform(X)

    prediction = model.predict(X_scaled)[0]
    probability = model.predict_proba(X_scaled)[0][1]

    result = "Diabetes" if prediction == 1 else "No Diabetes"

    return {
        "result": result,
        "probability": round(float(probability), 4)
    }
