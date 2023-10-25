FROM python:3.10
ENV VIRTUAL_ENV=/opt/venv
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="#$VIRTUAL_ENV/bin:$PATH"

WORKDIR /server

COPY ./app ./app
COPY .env ./
COPY ./scripts ./scripts
COPY ./alembic.ini ./
COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000 

CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
