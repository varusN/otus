FROM python:3.11.3-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY blog .

CMD ["uvicorn","main:app","--host", "0.0.0.0","--port", "8000"]

EXPOSE 8000