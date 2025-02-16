FROM python:3.12-slim

RUN apt update && apt install -y libgl1 libglib2.0-0 && rm -rf /var/lib/apt/lists/*

COPY adminka_fast_api/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app
WORKDIR /app

CMD ["uvicorn", "admin_main:app", "--host", "0.0.0.0", "--port", "5000"]
