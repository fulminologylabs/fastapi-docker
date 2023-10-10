FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /server

COPY ./app ./app
COPY ./scripts ./scripts
COPY ./alembic.ini ./
COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000 

CMD [ "./scripts/init-api.sh" ]