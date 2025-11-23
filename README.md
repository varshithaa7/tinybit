

---

# 🌀 TinyBit — Cloud-Native URL Shortener

*A simple yet impressive cloud project built using Flask, Redis, Docker, and Kubernetes.*

TinyBit is a lightweight microservice that shortens long URLs into tiny, shareable links.
This project demonstrates real-world cloud concepts such as containerized services, environment configuration, caching, and Kubernetes orchestration.


---

## 🚀 Features

* 🔗 Generate short URLs quickly
* ⚡ Fast redirection using Redis in-memory cache
* 🐳 Fully containerized backend using Docker
* ☸️ Kubernetes-ready with Deployments, Services, ConfigMaps
* 🧩 Works seamlessly with Minikube for local K8s
* 🔧 Clean, modular cloud-native architecture

---

## 🧱 Tech Stack

| Component          | Technology                   |
| ------------------ | ---------------------------- |
| Backend            | Python (Flask)               |
| Cache / Data Store | Redis                        |
| Containerization   | Docker                       |
| Orchestration      | Kubernetes (Minikube)        |
| Routing            | Kubernetes Service / Ingress |
| IDE                | VSCode                       |

---

## 📂 Project Structure

```
tinybit/
│── app.py
│── Dockerfile
│── requirements.txt
│── k8s/
│   ├── tinybit-deployment.yaml
│   ├── tinybit-service.yaml
│   ├── redis-deployment.yaml
│   ├── tinybit-configmap.yaml
│   └── tinybit-ingress.yaml
│── README.md
```

---

# 🐳 Run Locally with Docker

### 1️⃣ Build the backend image

```bash
docker build -t tinybit-backend:local .
```

### 2️⃣ Start Redis container

```bash
docker run -d --name tiny-redis -p 6379:6379 redis:7
```

### 3️⃣ Run TinyBit backend

```bash
docker run -d --name tinybit \
  -p 5000:5000 \
  -e REDIS_HOST=host.docker.internal \
  -e REDIS_PORT=6379 \
  tinybit-backend:local
```

Now open:

👉 [http://localhost:5000](http://localhost:5000)

---

# ☸️ Deploy on Kubernetes (Minikube)

### 1️⃣ Start Minikube

```bash
minikube start
```

### 2️⃣ Apply Kubernetes manifests

```bash
kubectl apply -f k8s/
```

### 3️⃣ Verify the deployment

```bash
kubectl get pods -n tinybit
kubectl get svc -n tinybit
```

### 4️⃣ Access the service

#### Option A: NodePort

```bash
minikube service tinybit-service -n tinybit
```

#### Option B: Ingress (if enabled)

Start Minikube tunnel:

```bash
minikube tunnel
```

Then visit:

👉 [http://tinybit.local/](http://tinybit.local/)

---

# 🔍 API Endpoints

### **POST /shorten**

Creates a short URL.

**Example Request**

```json
{
  "url": "https://example.com"
}
```

**Example Response**

```json
{
  "short_url": "http://localhost:5000/xyz123"
}
```

---

### **GET /<short_id>**

Redirects the user to the original URL.

---

# 🗑 Cleanup

Remove Kubernetes resources:

```bash
kubectl delete namespace tinybit
```

Stop Docker containers:

```bash
docker stop tinybit tiny-redis
docker rm tinybit tiny-redis
```

Stop Minikube:

```bash
minikube stop
```

---

# 📌 What You Learn from This Project

* Building a microservice in Python
* Using Redis as an in-memory cache
* Containerization using Docker
* Fundamentals of Kubernetes deployments
* Kubernetes Services & ConfigMaps
* Ingress routing for HTTP services
* Running production-style architecture locally

--
