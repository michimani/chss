FROM python:3.8.3
COPY . /app
ENTRYPOINT [ "python", "/app/src/change_status.py" ]