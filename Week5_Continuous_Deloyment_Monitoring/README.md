# 📅 Week 5 | Continuous Deployment & Monitoring (Advanced)

## 🎯 Internship Objectives
- Automate **CI/CD pipelines** for Dockerized applications.
- Implement **GitHub Actions** for continuous integration and deployment.
- Automate Docker image building, testing, and deployment on every push.
- Set up **Prometheus** and **Grafana** for monitoring containers and system metrics.
- Research and document **DevSecOps practices and tools**.

---

## ✔️ Tasks Completed

1. **CI/CD Pipeline Setup**
   - Configured **GitHub Actions workflow** (`.github/workflows/ci-cd.yml`) for the Dockerized Flask app.
   - Pipeline includes:
     - Code checkout
     - Python dependencies installation
     - Running tests with **pytest**
     - Docker image build and Trivy scan
     - Push Docker image to **Docker Hub**
   - Workflow triggers on **push or pull request** to the `main` branch, but only for changes in `Week5_Continuous_Deployment_Monitoring/**`.

2. **Automated Docker Deployment**
   - Created `Dockerfile` inside `app/`.
   - Automated building and running containers through CI/CD.
   - Verified container deployment locally and via GitHub Actions.

3. **Prometheus & Grafana Monitoring**
   - Configured monitoring stack in `monitoring/` folder:
     - `docker-compose.monitoring.yml` to run Prometheus and Grafana
     - `prometheus.yml` for scraping container metrics
     - Grafana folder contains dashboards and datasource configuration
   - Monitored **CPU, Memory, and Disk usage** of containers in Grafana dashboards.

4. **System Metrics Visualization**
   - Visualized real-time container and system metrics.
   - Created Grafana dashboards with graphs for:
     - CPU usage
     - Memory usage
     - Disk utilization

5. **DevSecOps Research**
   - Documented **security practices for CI/CD pipelines and containers** in `docs/devsecops.md`.
   - Included tools and practices such as:
     - **Trivy** vulnerability scanning
     - Secure Docker image practices
     - CI/CD security best practices

---

## 📁 Folder Contents Overview

| Filename / Folder                                          | Description |
|------------------------------------------------------------|-------------|
| `Week5_Continuous_Deployment_Monitoring/`                 | Main project folder for Week 5                  |
| ├─ `app/`                                                 | Flask app with Dockerfile, tests, and templates |
| ├─ `.github/workflows/ci-cd.yml`                          | GitHub Actions CI/CD workflow                   |
| ├─ `monitoring/`                                          | Prometheus & Grafana monitoring stack           |
| ├─ `docs/`                                                | Architecture and DevSecOps documentation        |
| ├─ `screenshots/`                                         | Evidence of pipeline runs, Docker containers & Grafana dashboards |
| `README.md`                                               | This file                                       |

---

## 🖼️ Documentation & Evidence
- **CI/CD Pipeline:** Screenshots of GitHub Actions runs and Docker image push.
- **Docker Deployment:** Evidence of running containers and local app access.
- **Prometheus & Grafana:** Dashboards monitoring system metrics.
- **DevSecOps Documentation:** Attached in `docs/devsecops.md`.

---

## 🙋‍♂️ Submitted by  
**Arsh-e-Noor**  
DevOps Internship | Week 5 | @CosmiCode
