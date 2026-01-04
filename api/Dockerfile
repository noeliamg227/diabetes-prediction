# 1. Base image
FROM python:3.12-slim

# 2. Work directory inside container
WORKDIR /app

# 3. Install system deps (optional)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the code
COPY . .

# 6. Expose API port
EXPOSE 8000

# 7. Start the API (FastAPI example; change to your entrypoint)
# If your main file is main.py and app is "app"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
