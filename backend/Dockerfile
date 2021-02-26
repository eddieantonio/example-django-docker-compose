FROM python:3.9-slim-buster

WORKDIR /opt/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["gunicorn", "--bind=0.0.0.0:8000", "sigh.wsgi:application"]
