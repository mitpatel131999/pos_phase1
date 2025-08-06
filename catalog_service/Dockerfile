# Dockerfile for the catalog microservice.  This service exposes
# product, supplier and purchase order endpoints via the products
# blueprint from the original POS backend.  It clones the
# repository at build time and installs the same dependencies.

FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN git clone --depth=1 https://github.com/mitpatel131999/POS_BACKEND.git repo
RUN pip install --no-cache-dir -r repo/flask_app/requirements.txt
RUN cp -r repo/flask_app ./flask_app && rm -rf repo

COPY app.py /app/app.py

ENV PYTHONPATH=/app/flask_app

EXPOSE 5000

CMD ["python", "app.py"]
