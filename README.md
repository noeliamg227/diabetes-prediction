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
Follow these steps to run the diabetes prediction API locally using Docker.

1. Download the project from GitHub

Unzip the file on your computer.
For the rest of the steps, replace the path with wherever you unzipped the folder.

2. Open a terminal in the project folder.​
   
Change directory into the unzipped project folder, then into diabetes-prediction if needed, and then into the root of the project:

cd /path/to/diabetes-prediction-main/diabetes-prediction
Adjust /path/to/... to your actual path.

You should see folders like api, artifacts, data, notebooks when you run:

ls

3. Make sure artifacts are available to the API
The API expects the model and scaler files inside api/artifacts.

From the project root folder:

cp -r artifacts api/

After this, the structure is:

text
api/
  app.py
  schema.py
  requirements.txt
  Dockerfile
  artifacts/
    diabetes_lr_model.joblib
    standard_scaler.joblib
    
4. Build the Docker image
Move into the api folder:

cd api

Build the image:

docker build -t diabetes-api .
This uses the provided Dockerfile and requirements.txt to create an image called diabetes-api.
​

5. Run the Docker container
Still in the api folder, run:

docker run -p 8000:8000 --name diabetes-api diabetes-api
The API runs with Uvicorn on port 8000 inside the container.

The -p 8000:8000 flag maps container port 8000 to port 8000 on your machine.
​

While this command is running and you see Uvicorn logs, open your browser at:

http://127.0.0.1:8000/docs

You will see the interactive FastAPI documentation (Swagger UI) and can test the prediction endpoint.
​

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

