FROM python:3.10-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code/api
COPY . /code/api/
COPY requirements.txt /code/api/
RUN pip install -r requirements.txt
