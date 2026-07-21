FROM python:3.13-slim

WORKDIR /app

COPY app.py .

ENV PORT=8080
ENV ENVIRONMENT=local
ENV APP_VERSION=1.0.0

EXPOSE 8080

CMD ["python", "app.py"]