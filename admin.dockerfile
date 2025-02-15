FROM python:3.12-slim

COPY admin/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app
WORKDIR /app/admin

ENTRYPOINT python admin.py
