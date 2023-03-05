FROM python:3.7-slim

COPY . .

WORKDIR /app

RUN pip3 install -r api_yamdb/requirements.txt --no-cache-dir

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]