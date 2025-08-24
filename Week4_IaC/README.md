# 📅 Week 4 | Infrastructure as Code (Intermediate to Advanced)

## 🎯 Internship Objectives
- Understand the concept of **Infrastructure as Code (IaC)**.
- Learn and implement **Terraform** for infrastructure provisioning.
- Learn **Ansible basics** for configuration management.
- Automate service deployment (Apache and Docker) using Ansible playbooks.
- Compare major IaC and configuration management tools: **Ansible, Puppet, Chef, and Terraform**.
- Document the complete workflow with screenshots and explanations.

---

## ✔️ Tasks Completed

1. **Terraform Installation and Configuration**  
   - Installed **Terraform** on the system.
   - Configured **AWS CLI** for authentication.
   - Verified setup using `terraform -v` and `aws configure`.

2. **EC2 Instance Deployment with Terraform**  
   - Wrote **Terraform scripts** to launch an EC2 instance on AWS.
   - Configured provider and resource blocks.
   - Used the following files:
     - `main.tf` → EC2 instance definition.
   - Executed commands:
     ```bash
     terraform init
     terraform plan
     terraform apply
     ```
   - Verified EC2 instance on AWS console.

3. **Ansible Playbook for Apache Installation**  
   - Learned **Ansible basics** (inventory, YAML syntax, modules).
   - Wrote a playbook to:
     - Install **Apache web server** on a Linux machine.
     - Ensure the service is started and enabled.
   - Verified by accessing Apache default page in the browser.

4. **Docker Deployment Automation using Ansible**  
   - Wrote an Ansible playbook to:
     - Install **Docker** on the target system.
     - Pull and run a Docker container.
   - Verified container deployment and application access.

5. **Comparison of Ansible, Puppet, Chef, and Terraform**  
   - Created a detailed **document** explaining:
     - Each tool’s overview and primary use case.
     - Key differences between **IaC** and **Configuration Management**.
     - Comparison table for better understanding.
   - **File:** `docs/Ansible_Puppet_Chef_Terraform_Comparison.docx`

---

## 📁 Folder Contents Overview

| Filename / Folder                                 | Description |
|---------------------------------------------------|-------------|
| `terraform/`                                      | Terraform scripts to launch EC2 instance |
| ├── `main.tf`                                     | Core Terraform configuration files |
| `ansible/`                                        | Ansible playbooks for Apache and Docker |
| ├── `install_apache_playbook.yml`                 | Installs Apache on a server |
| ├── `docker_deploy_playbook.yml`                  | Installs Docker and deploys a container |
| `Ansible_Puppet_Chef_Terraform_Comparison.docx`   | Detailed comparison of IaC tools |
| `screenshots/`                                    | Proof of Terraform execution, EC2 instance, and Ansible tasks |
| `README.md`                                       | Overview of Week 4 tasks and learnings |


---

## 🖼️ Documentation & Evidence
- **Terraform:** Screenshots of `terraform version` and AWS EC2 instance.
- **Ansible Apache:** Screenshots of successful playbook execution and Apache default page.
- **Ansible Docker:** Screenshot of running container and app access.
- **Comparison Document:** Attached in `docs/`.

---

## 🙋‍♂️ Submitted by  
**Arsh-e-Noor**  
DevOps Internship | Week 4 | @CosmiCode

