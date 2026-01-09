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


## Running the API

From the project root directory, start the API server with:

uvicorn api.app:app --reload

Once running, the API will be available at:

http://127.0.0.1:8000


## Deploying the API with Docker

1. Go to the project folder
Open Terminal.

Move into the unzipped project root (adjust the path to where you saved it):

cd /path/to/diabetes-prediction-main/diabetes-prediction

2. Make the model files visible to the API
The API expects the model and scaler under api/artifacts.

From the project root:

cp -r artifacts api/

Then:

cd api
ls

You should now see:

Dockerfile  app.py  requirements.txt  __init__.py  artifacts  schema.py
and:

cd artifacts
ls

should show:

diabetes_lr_model.joblib  standard_scaler.joblib

Go back to api:

bash
cd ..
cd api
​

3. Build the Docker image
From the api folder:

docker build -t diabetes-api .

Wait until it finishes without errors.
​

4. Run the API
Still in api:

docker run -p 8000:8000 --name diabetes-api diabetes-api

If it starts correctly, you will see:

INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
While this text is visible and the command is still running, open a browser and go to:

http://127.0.0.1:8000/docs

You should see the FastAPI interactive docs.
​

## API documentation

FastAPI automatically generates interactive documentation.
Open the following URL in a browser:

http://127.0.0.1:8000/docs

The documentation allows users to:
- View all available endpoints
- Inspect input and output schemas
- Send test requests directly from the browser

