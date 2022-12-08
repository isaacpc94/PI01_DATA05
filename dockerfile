FROM tiangolo/uvicorn-gunicorn:python3.10.5

LABEL maintainer="isaac junior peña cueva  <isaacpc_94@gmail.com>"

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./app /app