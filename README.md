# lead-crm-integrator

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
touch .env

- Contact an administrator to populate the environment variables.

pip install -r requirements.txt
python app/main.py --reload

# swagger api documentation
visit: http://localhost:8000/docs after running the application locally

# build with Docker
docker build -t lead-crm-integrator .

# run with docker
docker run -p 8000:8000 lead-crm-integrator

# run with docker in detached mode
docker run -d -p 8000:8000 lead-crm-integrator

# remove pycache
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

find . | grep -E "(.pytest_cache|\*)" | xargs rm -rf

## Begin to White label
Navigate to app.api.main and edit the params of the
FastAPI app object. Then, copy to the code to a repository they own and create a branch to continue
with their project.