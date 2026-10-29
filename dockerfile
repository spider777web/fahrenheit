FROM python:3.11-slim

WORKDIR /app

COPY fahrenheit.py .

CMD ["python", "fahrenheit.py"]