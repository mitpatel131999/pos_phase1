# Dockerfile for the POS backend service.  This image builds the
# existing Flask application from the public GitHub repository and
# installs its dependencies.  By cloning the repository at build
# time we avoid the need to have the source code present on the
# host machine when running docker-compose.  If you have a private
# fork or want to build from a specific commit, adjust the Git URL
# and checkout commands accordingly.

FROM python:3.11-slim

# Install git so that we can clone the repository in the build
# context.  Git is removed after use to keep the final image small.
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Clone the POS_BACKEND repository.  The `--depth=1` option
# downloads only the latest commit.  If you need the full history
# remove this option.
RUN git clone --depth=1 https://github.com/mitpatel131999/POS_BACKEND.git repo

# Install Python dependencies.  The repository contains a
# requirements.txt file inside the flask_app folder which lists
# the runtime dependencies.  Install these requirements directly
# from the cloned repository before removing it.  Using this
# approach avoids the need to copy any local files into the image.
RUN pip install --no-cache-dir -r repo/flask_app/requirements.txt

# Copy the Flask application from the cloned repository into
# /app/flask_app.  Once the copy is complete remove the cloned
# repository to reduce the size of the final image.
RUN cp -r repo/flask_app ./flask_app && \
    rm -rf repo

# Expose the port on which the Flask application runs.
EXPOSE 5000

# Set an environment variable for the database URI.  This value
# can be overridden at runtime via docker-compose or other
# orchestrators.
ENV MONGO_URI=""

# Run the application.  We use the built‑in eventlet WSGI server
# provided by Flask-SocketIO if available.  When Flask-SocketIO is
# installed, running app.py directly will start the socketIO server.
CMD ["python", "flask_app/app.py"]
