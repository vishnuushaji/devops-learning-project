# Base image: official Python on a minimal Debian ("slim" = no extra tools, smaller + fewer vulnerabilities).
# Pin the version: "python:latest" would silently change under us.
FROM python:3.13-slim

# PYTHONDONTWRITEBYTECODE: don't write .pyc files (useless in a container).
# PYTHONUNBUFFERED: print logs immediately so `docker logs` shows them live.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# LAYER-CACHING TRICK: copy ONLY the dependency list first and install.
# This layer is rebuilt only when requirements.txt changes. Editing app.py
# later won't re-download Flask, so rebuilds take seconds instead of minutes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App code changes most often, so it goes last.
COPY app.py .

# Security: create and switch to an unprivileged user. A numeric UID lets
# Kubernetes later verify "runAsNonRoot" (it can't resolve names to IDs).
RUN useradd --create-home --uid 10001 appuser
USER 10001

# Documentation only: tells humans/tools which port the app listens on.
EXPOSE 5000

# Docker itself polls this to mark the container "healthy" / "unhealthy".
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health', timeout=2)"

# Production server instead of Flask's dev server.
# Exec form (JSON array) so gunicorn is PID 1 and receives stop signals properly.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
