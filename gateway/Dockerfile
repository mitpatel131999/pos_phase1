# Dockerfile for the API gateway.  This image uses the official
# Nginx Alpine distribution and copies a custom configuration file
# into the container.  The configuration defines an upstream
# pointing to the backend service and proxies requests accordingly.

FROM nginx:alpine

# Remove the default Nginx configuration and replace it with our
# gateway configuration.  The configuration file is provided via
# docker-compose in a bind mount so that changes take effect
# without rebuilding the image.  Here we also copy it into the
# image so the container can run stand‑alone if desired.
COPY nginx.conf /etc/nginx/nginx.conf
