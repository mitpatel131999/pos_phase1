# Dockerfile for the admin panel.  The admin panel is implemented
# as a simple Flask application that serves a basic dashboard and
# could be extended to manage users, products, orders and other
# resources by consuming the microservice APIs via the gateway.

FROM python:3.11-slim

WORKDIR /app

# Install Flask.  Additional frontend libraries can be added as
# the admin panel evolves (e.g. React, Vue, Bootstrap).
RUN pip install --no-cache-dir flask flask-cors requests

COPY app.py /app/app.py

EXPOSE 3000

CMD ["python", "app.py"]
