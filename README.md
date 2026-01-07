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


## Running the API Locally

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

## Running the API with Docker

Build the Docker Image: From inside the api/ directory (where the Dockerfile is located), run:

docker build -t diabetes-api .

Run the Docker Container:

docker run -p 8000:8000 diabetes-api


