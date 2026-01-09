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

## How to run the API with Docker
docker build -t diabetes-api api/
docker run -p 8000:8000 diabetes-api

The API will be available at http://127.0.0.1:8000 with the web interface at / and interactive API docs at /docs.​

To run the container in the background (optional), use:

docker run -d -p 8000:8000 --name diabetes-api diabetes-api

Then manage it with:

bash
docker ps         # see running containers
docker stop diabetes-api   # stop
docker rm diabetes-api     # remove

## API documentation

FastAPI automatically generates interactive documentation.
Open the following URL in a browser:

http://127.0.0.1:8000/docs

The documentation allows users to:
- View all available endpoints
- Inspect input and output schemas
- Send test requests directly from the browser

