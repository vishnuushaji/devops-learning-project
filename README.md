# DevOps Learning Project

A small Flask app that we progressively package, test, ship, deploy and monitor
using only free tools.

## Roadmap

- [x] **Phase 1: App + tests** (Flask, pytest, venv)
- [x] **Phase 2: Containerize** (Docker)
- [ ] Phase 3: CI/CD (Git + GitHub Actions)
- [ ] Phase 4: Kubernetes + Helm (kind)
- [ ] Phase 5: Monitoring (Prometheus + Grafana)
- [ ] Phase 6: Security scanning + GitOps (Trivy, Argo CD)
- [ ] Phase 7 (optional): Infrastructure as Code (Terraform)

## Run locally (Phase 1)

```powershell
cd app
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest        # run tests
.\.venv\Scripts\python.exe app.py           # start server on http://localhost:5000
```

Endpoints: `GET /` (greeting + hostname + version), `GET /health` (liveness check).

## Run in Docker (Phase 2)

```powershell
cd app
docker build -t devops-demo-app:1.0.0 .
docker run -d --name demo-app -p 8080:5000 -e APP_VERSION=2.0.0 devops-demo-app:1.0.0
curl http://localhost:8080/health
docker stop demo-app; docker rm demo-app
```

Key ideas: image vs. container, layer caching (dependencies copied before code),
non-root user, slim base image, production server (gunicorn), HEALTHCHECK.
