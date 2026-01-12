FROM python:3.12-slim
WORKDIR /parking
COPY . .
CMD ["python","parking.py"]
