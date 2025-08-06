# Dockerfile for the authentication microservice.  This image
# clones the original POS_BACKEND repository, installs its
# dependencies and copies a lightweight entrypoint that registers
# only the authentication blueprint.  PYTHONPATH is set so that
# modules inside flask_app can be imported directly from app.py.

FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN git clone --depth=1 https://github.com/mitpatel131999/POS_BACKEND.git repo
RUN pip install --no-cache-dir -r repo/flask_app/requirements.txt
RUN cp -r repo/flask_app ./flask_app && rm -rf repo

# Copy the service entrypoint into the image.
COPY app.py /app/app.py

# Ensure modules within flask_app are importable.
ENV PYTHONPATH=/app/flask_app

EXPOSE 5000

CMD ["python", "app.py"]
