# Deploying n8n with Docker Compose – A Complete Guide

**n8n** (pronounced *"n-eight-n"*) is an open-source workflow automation tool that helps you connect APIs, databases, and internal tools to automate tasks — without writing complex code. In this guide, we’ll walk through how to deploy `n8n` using Docker Compose.

---

## 🚀 Why Use Docker Compose?

Docker Compose allows you to define and run multi-container applications. With n8n, Compose makes it easy to set up:
- Persistent storage
- Environment variables
- Auto-starting the service
- Networking with other services (e.g., PostgreSQL, Redis)

---

## 🧰 Prerequisites

- Docker installed: [Install Docker](https://docs.docker.com/engine/install/)
- Docker Compose installed: [Install Compose](https://docs.docker.com/compose/install/)
- A basic understanding of YAML and Docker commands

---

## 📁 Folder Structure

We’ll use the following structure:

```
n8n-docker/
├── docker-compose.yml
└── .env
```

---

## ✍️ .env File

Create a `.env` file to store environment variables:

```env
# Basic
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=securepassword

# External Access
N8N_HOST=localhost
N8N_PORT=5678

# Timezone
GENERIC_TIMEZONE=Asia/Kolkata

# Execution Mode
N8N_EXECUTIONS_MODE=queue
```

---

## ⚙️ docker-compose.yml

```yaml
version: "3.8"

services:
  n8n:
    image: n8nio/n8n:latest
    restart: always
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=${N8N_BASIC_AUTH_ACTIVE}
      - N8N_BASIC_AUTH_USER=${N8N_BASIC_AUTH_USER}
      - N8N_BASIC_AUTH_PASSWORD=${N8N_BASIC_AUTH_PASSWORD}
      - N8N_HOST=${N8N_HOST}
      - N8N_PORT=${N8N_PORT}
      - GENERIC_TIMEZONE=${GENERIC_TIMEZONE}
      - N8N_EXECUTIONS_MODE=${N8N_EXECUTIONS_MODE}
    volumes:
      - ./n8n_data:/home/node/.n8n
```

---

## ▶️ Starting the Service

```bash
docker-compose up -d
```

- The first time it may take a while to pull the Docker image.
- Access your instance at: [http://localhost:5678](http://localhost:5678)

---

## 🔐 Access & Authentication

You’ve enabled **basic auth** in the `.env` file, so use the credentials:

```
Username: admin
Password: securepassword
```

---

## 💾 Persistent Data

The volume `./n8n_data:/home/node/.n8n` ensures that your workflows, credentials, and settings are retained even if the container is removed.

---

## 🧠 Tips & Extras

- You can use a reverse proxy like **NGINX** to expose it securely via HTTPS.
- To use external databases like PostgreSQL or Redis, just add them to the Compose file.
- Back up your volume regularly to avoid data loss.

---

## 🧹 Stopping and Removing

```bash
docker-compose down
```

Add `-v` to remove volumes if needed:
```bash
docker-compose down -v
```

---

## 📚 References

- [n8n Documentation](https://docs.n8n.io)
- [n8n Docker Hub](https://hub.docker.com/r/n8nio/n8n)
- [n8n GitHub](https://github.com/n8n-io/n8n)

---

*Written by Santhosh Murugesan – Simplifying automation one workflow at a time.*

---

## Note
* Based on the Setup you are having, the Environment variable will get varied