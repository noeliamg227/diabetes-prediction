# API Deployment and Testing

## Overview

This document describes the deployment and testing of the FastAPI service developed for the Diabetes Prediction project. The goal is to validate that the API is correctly deployed, exposes its endpoints, and produces meaningful predictions using the trained machine learning model.

------------------------------------------------------------------------

## API Description

-   **Framework:** FastAPI
-   **Entry point:** `api/app.py`
-   **Exposed endpoint:** `POST /predict`
-   **Model artifacts:**
    -   `artifacts/diabetes_lr_model.joblib`
    -   `artifacts/standard_scaler.joblib`

The API performs binary classification to predict the presence or absence of diabetes and returns both the predicted class and an associated probability.

------------------------------------------------------------------------

## Deployment

### Local Deployment (Validated)

Due to network restrictions that may affect Docker image builds in certain environments, the API deployment was validated using a local Python virtual environment.

The service was executed locally using Uvicorn, which acts as the application server for the FastAPI application.

The following steps were used to deploy the API locally:

```bash
cd api 
python -m venv .venv 
source .venv/bin/activate 
pip install -r requirements.txt 
uvicorn app:app --host 0.0.0.0 --port 8000 
```

Once running, the API becomes available at:

-   **Swagger UI:** <http://localhost:8000/docs>
-   **OpenAPI schema:** <http://localhost:8000/openapi.json>

------------------------------------------------------------------------

## API Testing

### Smoke Test

The availability of the deployed API was verified using the Swagger UI and the OpenAPI specification:

```bash
curl -i <http://localhost:8000/docs> 
curl -i <http://localhost:8000/openapi.json> 
```

**Observed result:**
 - HTTP status: 200 OK

This confirms that the service is running and correctly exposes its documentation and schema.

------------------------------------------------------------------------

### Schema Validation Test (Negative Test)

To verify input validation, an invalid request with an empty JSON body was sent to the prediction endpoint:

```bash
curl -i -X POST http://localhost:8000/predict 
  -H "Content-Type: application/json" 
  -d '{}'
```

**Observed response:**

-   HTTP status: 422 Unprocessable Entity

The response returned detailed validation errors indicating that all required input fields were missing.  
This confirms that the API correctly enforces input schema validation before model inference.

------------------------------------------------------------------------
### Functional Test (Happy Path)

A valid request including all required features was sent to the prediction endpoint:

```bash
curl -i -X POST http://localhost:8000/predict 
  -H "Content-Type: application/json"
  -d '{
    "pregnancies": 2,
    "glucose": 130,
    "blood_pressure": 70,
    "skin_thickness": 20,
    "insulin": 80,
    "bmi": 28.5,
    "diabetes_pedigree": 0.35,
    "age": 35
  }'
```

**Observed response:**

``` json
{
  "result": "No Diabetes",
  "probability": 0.3774
}
```

This confirms that the API successfully processes valid input data and returns a meaningful prediction.

------------------------------------------------------------------------

## Notes and Limitations

-   A warning may appear during model loading due to differences between the scikit-learn version used during model training and the version used at inference time.
-   While inference remains functional, full reproducibility would require pinning dependency versions consistently across training and deployment environments.

------------------------------------------------------------------------

## Observed Results

The API was executed locally and tested using HTTP requests.

-   The service successfully started using Uvicorn and exposed the Swagger UI.
-   The `/docs` and `/openapi.json` endpoints returned HTTP 200 responses.
-   An invalid request to `/predict` returned HTTP 422 with detailed schema validation errors.
-   A valid request to `/predict` returned HTTP 200 and produced a prediction result and associated probability (e.g., `{"result":"No Diabetes","probability":0.3774}`).

These results confirm that the deployed API is operational, correctly enforces input validation, and performs inference as expected.
