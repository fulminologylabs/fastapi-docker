#!/bin/bash
# dependencies
pip install -r requirements.txt
# migrations
#alembic upgrade head
# run
python -m app.api.main