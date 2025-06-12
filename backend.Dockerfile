# backend.Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY backend/karma/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project
COPY backend/karma/ .

EXPOSE 8000

CMD sh -c "python manage.py makemigrations && \
           python manage.py migrate && \
           python manage.py runserver 0.0.0.0:8000"
