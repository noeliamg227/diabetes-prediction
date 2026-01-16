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

1. The API expects the model and scaler under api/artifacts. From the project root:

cp -r artifacts api/

2. From the api folder, start the API server with:

uvicorn app:app --reload

3. Once running, the API will be available at:

http://127.0.0.1:8000


## Deploying the API with Docker

1. The API expects the model and scaler under api/artifacts. From the project root:

cp -r artifacts api/

​
  2. Build the Docker image. From the api folder:

docker build -t diabetes-api .

3. Run the API. From the api folder:

docker run -p 8000:8000 --name diabetes-api diabetes-api

4. Open a browser and go to:

http://127.0.0.1:8000/

You should see the FastAPI interface.
​

## API documentation

FastAPI automatically generates interactive documentation.
Open the following URL in a browser:

http://127.0.0.1:8000/docs

The documentation allows users to:
- View all available endpoints
- Inspect input and output schemas
- Send test requests directly from the browser

