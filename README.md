# fastapi-docker

## Developer Setup
# Prerequisities
- Python
- pip
- Docker

source venv/bin/activate

# add a package
pip install < package >
pip freeze > requirements.txt
 
# run application
pip install -r requirements.txt
python app/main.py --reload

# swagger api documentation
visit: http://localhost:8000/docs after running the application locally