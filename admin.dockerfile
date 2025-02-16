FROM python:3.12-slim

COPY adminka_fast_api/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app
WORKDIR /app

CMD ["uvicorn", "adminka_fast_api:app", "--host", "0.0.0.0", "--port", "5000"]
