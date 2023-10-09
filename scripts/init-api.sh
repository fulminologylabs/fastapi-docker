#!/bin/bash
# dependencies
pip install -r requirements.txt
# migrations
#alembic upgrade head
# run
uvicorn app.api.main:app --host=0.0.0.0 --port=8000 --reload