# Python API Template
## description
```
Basic.
```

## Developer Setup
# Prerequisities
- `Python`
- `pip`
- `Docker`
- `psql`

`source venv/bin/activate` at the root.

# add a package
`pip install < package >`
`pip freeze > requirements.txt`
 
# run application
`touch .env`

- Contact an administrator to populate the environment variables.

`pip install -r requirements.txt`
`python app/main.py --reload` or `./scripts/init-api.sh`

# swagger api documentation
visit: http://localhost:8000/docs after running the application locally

# build with Docker
`docker build -t api .`

# run with docker
`docker run -p 8000:8000 api`

# run with docker in detached mode
`docker run -d -p 8000:8000 api`

# remove pycache
```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```
```
find . | grep -E "(.pytest_cache|\*)" | xargs rm -rf
```
## Database
```
chmod +x ./scripts/init-db.sh
./scripts/init-db.sh
```
Test the connection:
`psql -h localhost -U postgres -p 5432 -d new_db`

# alembic
Generate from SQLAlchemy Table MetaData
`alembic revision --autogenerate -m "< description >"`

Generate manually
`alembic revision -m "< description >"`

`alembic upgrade head`

## Begin to White label
```
Navigate to app.api.main and edit the params of the
FastAPI app object. Then, copy to the code to a repository they own and create a branch to continue
with their project.
```

## TODO
1. `Testing suite`
2. `Advanced environment loading`
3. `Digital Ocean deployment spec`
