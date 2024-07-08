#!/bin/bash
# Entrypoint script to run the FastAPI application

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI application
uvicorn main:app --host 0.0.0.0 --port 8000

# Run the frontend
npm start