# Use an official Python runtime as a parent image
FROM python:latest
#FROM python:3.11-bookworm

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]
