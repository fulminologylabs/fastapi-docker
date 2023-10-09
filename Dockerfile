FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /server

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY ./scripts ./scripts
COPY ./alembic.ini ./

# create log directory
RUN mkdir -p /var/log/hub
RUN touch /var/log/hub/general.log

VOLUME [ "/var/log/hub" ]

EXPOSE 8000 

CMD [ "uvicorn", "app.api.main:app", "--host=0.0.0.0", "--port=8000" ]
