# DevSecOps Practices and Tools

## 1. Introduction
DevSecOps integrates security into the DevOps lifecycle, ensuring that applications are not only delivered quickly but also remain secure at every stage. Unlike traditional DevOps, DevSecOps emphasizes security automation, continuous monitoring, and vulnerability management.

---

## 2. Key Practices

1. **Shift-Left Security**
   - Security checks are implemented early in the development process.
   - Example: Static code analysis, unit tests with security checks.

2. **Automated Vulnerability Scanning**
   - Continuous scanning of code, dependencies, and Docker images.
   - Example tools: **Trivy**, **Snyk**, **Clair**.

3. **Secrets Management**
   - Sensitive information (API keys, passwords) is never hard-coded.
   - Example: Using **GitHub Secrets**, **HashiCorp Vault**, or **AWS Secrets Manager**.

4. **Continuous Monitoring**
   - Monitoring runtime environments and infrastructure for security issues.
   - Tools: **Prometheus**, **Grafana**, **Falco**.

5. **Compliance and Policy as Code**
   - Automating compliance checks (e.g., PCI, GDPR) using code.
   - Example tools: **Open Policy Agent (OPA)**, **Chef InSpec**.

---

## 3. Tools Used in This Project

| Tool           | Purpose in Project                                |
|----------------|---------------------------------------------------|
| Docker         | Containerization for consistent app deployment    |
| Test file      | Tests the app before building image               |
| GitHub Actions | CI/CD pipeline automation                         |
| Trivy          | Docker image vulnerability scanning               |
| Prometheus     | Monitoring application and system metrics         |
| Grafana        | Visualizing metrics collected by Prometheus       | 
| GitHub Secrets | Storing sensitive credentials securely            |

---

## 4. Benefits of DevSecOps

- Early detection of vulnerabilities
- Continuous security enforcement without slowing development
- Automated and repeatable security processes
- Reduced risk of breaches in production
- Stronger trust and compliance

---

## 5. Summary
This project demonstrates DevSecOps by integrating security in the CI/CD pipeline, performing automated image scans using Trivy, and monitoring application metrics via Prometheus and Grafana. Secrets are safely managed using GitHub Secrets, creating a secure and professional deployment workflow.
