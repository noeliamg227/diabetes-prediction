# diabetes-prediction

This repository contains a RESTful API that exposes a trained machine learning model for diabetes prediction.  
The API is built using **FastAPI** and serves predictions from a pre-trained **Logistic Regression** model.

---

## Overview

The goal of this component is to **deploy an already trained model** and make it accessible via a clean, documented API interface.

The API:
- Loads a serialized scikit-learn model
- Accepts structured patient health markers as input
- Returns a prediction and probability
- Provides automatic interactive documentation

## Project Structure

diabetes-prediction/
├── api/
│ ├── init.py
│ ├── app.py # FastAPI application
│ └── schema.py # Input validation schema (Pydantic)
├── artifacts/
│ └── diabetes_lr_model.joblib # Trained model artifact
└── README.md


## Running the API

From the project root directory, start the API server with:

uvicorn api.app:app --reload

Once running, the API will be available at:

http://127.0.0.1:8000

## API documentation

FastAPI automatically generates interactive documentation.
Open the following URL in a browser:

http://127.0.0.1:8000/docs

The documentation allows users to:
- View all available endpoints
- Inspect input and output schemas
- Send test requests directly from the browser

