🌀 TinyBit — Cloud-Native URL Shortener

A simple yet impressive cloud project built using Flask, Redis, Docker, and Kubernetes.

TinyBit is a lightweight, production-style microservice that shortens long URLs into tiny, shareable links.
It demonstrates real-world cloud concepts including containerization, service discovery, in-memory caching, and Kubernetes orchestration.

Ideal for cloud, DevOps, platform engineering, and backend roles.

🚀 Features

🔗 Generate short URLs quickly

⚡ Ultra-fast redirection using Redis cache

🐳 Fully containerized (Docker)

☸️ Kubernetes-ready with Deployments, Services, ConfigMaps

📦 Easy local development using Minikube

🔧 Clean separation of concerns (backend + cache layer)

🧱 Tech Stack
Component	Technology
Backend	Python (Flask)
Cache / Database	Redis
Containerization	Docker
Orchestration	Kubernetes (Minikube)
API Routing	Kubernetes Service / Ingress
Dev Environment	VSCode
📂 Project Structure
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

🐳 Run the App with Docker
1. Build the backend image
docker build -t tinybit-backend:local .

2. Start Redis
docker run -d --name tiny-redis -p 6379:6379 redis:7

3. Run the backend
docker run -d --name tinybit \
  -p 5000:5000 \
  -e REDIS_HOST=host.docker.internal \
  -e REDIS_PORT=6379 \
  tinybit-backend:local


Access backend at:

➡ http://localhost:5000

☸️ Deploy on Kubernetes (Minikube)
1. Start Minikube
minikube start

2. Apply all manifests
kubectl apply -f k8s/

3. Check deployments
kubectl get pods -n tinybit
kubectl get svc -n tinybit

4. Access service
If using NodePort:
minikube service tinybit-service -n tinybit

If using Ingress:
minikube tunnel


Then visit:

➡ http://tinybit.local

🔍 API Endpoints
POST /shorten

Shortens a long URL.

Request

{
  "url": "https://example.com"
}


Response

{
  "short_url": "http://localhost:5000/abc123"
}

GET /<short_id>

Redirects to original long URL.

🗑 Cleanup
kubectl delete namespace tinybit
docker stop tinybit tiny-redis
docker rm tinybit tiny-redis
minikube stop

📌 What You Learn from This Project

How microservices work

Containerization using Docker

Using Redis for real-time, in-memory caching

Kubernetes Deployments, Services, ConfigMaps

Ingress-based routing

Real-world cloud-native application structure
