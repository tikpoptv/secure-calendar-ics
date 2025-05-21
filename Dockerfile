FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p data

ENV PYTHONUNBUFFERED=1

EXPOSE 5555

CMD ["python", "app.py"]
