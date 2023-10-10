FROM python:3.10
ENV VIRTUAL_ENV=/opt/venv
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="#$VIRTUAL_ENV/bin:$PATH"

WORKDIR /server

COPY ./app ./app
COPY ./scripts ./scripts
COPY ./alembic.ini ./
COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000 

CMD [ "python3", "-m", "app.api.main" ]
