#!/usr/bin/env bash
set -x
set -eo pipefail
# check dependencies
if ! [ -x "$(command -v psql)" ]; then
    echo >&2 "Error: psql is not install."
    exit 1
fi

if ! [ -x "$(command -v alembic)" ]; then
    echo >&2 "Error alembic is not installed."
    echo >&2 "Use:"

    echo >&2 "   pip install alembic"
    echo >&2 "to install it."
    exit 1
fi

# check if a custom user has been set if not, default
DB_USER="${POSTGRES_USER:=postgres}"

DB_PASSWORD="${POSTGRES_PASSWORD:=password}"
DB_NAME="${POSTGRES_DB:=new_db}"
TEST_DB_NAME="${TEST_DB:=test_db}"
DB_PORT="${POSTGRES_PORT:=5432}"
DB_HOST="${POSTGRES_HOST:=localhost}"

# launching postgres using docker...
# allow to skip docker if a dockerized postgres
# db is already running
if [[ -z "${SKIP_DOCKER}" ]]
then
    docker run \
        -e POSTGRES_USER=${DB_USER} \
        -e POSTGRES_PASSWORD=${DB_PASSWORD} \
        -e POSTGRES_DB=${DB_NAME} \
        -p "${DB_PORT}":5432 \
        -d postgres \
        postgres -N 1000
        #           ^ increases max # connections for testing purposes
fi
# ping postgres until it is ready to accept connections
export PGPASSWORD="${DB_PASSWORD}"
until psql -h "${DB_HOST}" -U "${DB_USER}" -p "${DB_PORT}" -d "postgres" -c '\q'; do 
    >&2 echo "Postgres is still unavailable - Sleeping..."
    sleep 1
done
# postgres is ready
>&2 echo "Postgres is up and running on port ${DB_PORT}..."
# create
psql -h "${DB_HOST}" -U "${DB_USER}" -tc "SELECT 1 FROM pg_database WHERE datname = '${DB_NAME}'" |
    grep -q 1 || \
    psql -U "${DB_USER}" -p "${DB_PORT}" -c "CREATE DATABASE '${DB_NAME}'"
# run migrations
>&2 echo "Running migrations."
alembic upgrade head
>&2 echo "Postgres has been migrated... Ready to go."
