# Project Architecture

## 1. Overview
This project is a **Weather App** with automated CI/CD and monitoring. It demonstrates modern DevOps practices including containerization, automated testing, deployment, and monitoring.

## 2. Components

### 2.1 Flask App (`app/`)
- Handles frontend and backend logic.
- Dockerized for consistent deployment.
- Includes tests (`tests/test_app.py`) to ensure functionality.

### 2.2 CI/CD Pipeline (`.github/workflows/ci-cd.yml`)
- Automated via **GitHub Actions**.
- Steps:
  1. Checkout repo.
  2. Install dependencies.
  3. Run tests.
  4. Build Docker image.
  5. Scan image with **Trivy**.
  6. Push image to Docker Hub.

### 2.3 Monitoring (`monitoring/`)
- **Prometheus:** Collects metrics from the Flask app container.
- **Grafana:** Visualizes metrics via dashboards.
- Docker Compose file orchestrates Prometheus and Grafana.

### 2.4 Documentation (`docs/`)
- `architecture.md` → Project structure & workflow.
- `devsecops.md` → Security practices & tools used.

### 2.5 Screenshots
- `screenshots/` → CI/CD run, Prometheus/Grafana dashboard screenshots.

## 3. Workflow Diagram

[Developer] 
     │
     ▼
[GitHub Repo] --> triggers --> [GitHub Actions CI/CD]
                                    │
                                    ▼
                         [Docker Image (Flask App)]
                                    │
                                    ▼
                      [App Container running on host]
                                    │
                     ┌──────────────┴─────────────┐
                     ▼                            ▼
             [Prometheus Container]        [Grafana Container]
                     │                            │
             Scrapes metrics                Visualizes metrics


## 4. Summary
- The project is fully **containerized**.
- CI/CD automates testing, building, scanning, and deployment.
- Monitoring is separate but linked via Docker networking.
- Documentation and reports provide clarity on architecture and security practices.

