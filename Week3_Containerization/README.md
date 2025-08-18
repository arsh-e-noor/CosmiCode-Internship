# 📅 Week 3 | Containerization & Orchestration Basics (Intermediate)

## 🎯 Internship Objectives
- Understand container orchestration and networking concepts.  
- Run multiple containers using Docker Compose (e.g., Flask web app + MySQL database).  
- Learn Kubernetes basics and create a deployment YAML file for a sample app.  
- Set up a local Kubernetes cluster using Minikube or Docker Desktop.  
- Deploy a containerized application to the local Kubernetes cluster.  
- Implement Docker volumes and networking in Docker Compose.  

---

## ✔️ Tasks Completed

1. **Docker Compose Multi-Container Setup**  
   - Created a Flask-based ToDo app with MySQL database.  
   - Wrote a `docker-compose.yml` file to define and run both containers together.  
   - Verified container networking and volume persistence.  

2. **Docker Image Management**  
   - Built Docker image locally: `flask-app:latest`.  
   - Pushed Docker image to Docker Hub: `arshen00r/internship:latest`.  

3. **Kubernetes Deployment**  
   - Wrote deployment YAML files for Flask app and MySQL database.  
   - Created services (ClusterIP for MySQL, NodePort for Flask) for inter-container communication.  
   - Deployed both containers to Minikube cluster.  

4. **Volume & Network Management in Kubernetes**  
   - Implemented PersistentVolume and PersistentVolumeClaim for MySQL database storage.  
   - Configured network communication between Flask pod and MySQL pod.  

5. **Testing & Verification**  
   - Verified Flask app working via Minikube NodePort URL.  
   - Checked pod status using `kubectl get pods`.  
   - Ensured services are accessible and stable.  

6. **Documentation & Evidence**  
   - Captured screenshots of Docker build, push, and running containers.  
   - Captured screenshots of Kubernetes pods, services, and Flask app working.  

---

## 📁 Folder Contents Overview

| Filename / Folder               | Description |
|--------------------------------|-------------|
| `app.py`                        | Flask-based ToDo app code |
| `Dockerfile`                    | Instructions to build Flask Docker image |
| `requirements.txt`              | Python dependencies for Flask app |
| `docker-compose.yml`            | Docker Compose setup for Flask + MySQL containers |
| `k8s/`                          | Kubernetes manifests (deployments, services, PV/PVC) |
| `screenshots/`                  | Screenshots showing Docker & Kubernetes setup, running pods, and app access |
| `README.md`                     | Overview of Week 3 tasks and learnings |

---

## 🙋‍♂️ Submitted by  
**Arsh-e-Noor**  
DevOps Internship | Week 3
