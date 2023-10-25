#!/bin/bash
# dependencies
pip install -r requirements.txt
# run
uvicorn app.api.main:app --host 0.0.0.0 --port 8080 --workers 1