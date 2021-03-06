FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app
RUN pip --no-cache-dir install flask
CMD ["python3", "app.py"]
