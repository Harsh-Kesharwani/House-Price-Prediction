#!/bin/bash

# Load environment variables
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Set defaults if not in .env
API_HOST=${API_HOST:-localhost}
API_PORT=${API_PORT:-8000}
API_PROTOCOL=${API_PROTOCOL:-http}

# Start FastAPI in background
uvicorn src.api.main:app --host $API_HOST --port $API_PORT &
API_PID=$!

# Wait a moment for API to start
sleep 2

# Start Streamlit (corrected path)
streamlit run src/frontend/app.py

# Clean up background process
kill $API_PID