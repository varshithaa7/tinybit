

---

#  TinyBit — Cloud-Native URL Shortener


TinyBit is a lightweight microservice that shortens long URLs into tiny, shareable links.
This project demonstrates real-world cloud concepts such as containerized services, environment configuration, caching, and Kubernetes orchestration.


---

## Features

*  Generate short URLs quickly
*  Fast redirection using Redis in-memory cache
*  Fully containerized backend using Docker
*  Kubernetes-ready with Deployments, Services, ConfigMaps
*  Works seamlessly with Minikube for local K8s
* 🔧 Clean, modular cloud-native architecture

---

##  Tech Stack

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



# API Endpoints

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


#  What You Learn from This Project

* Building a microservice in Python
* Using Redis as an in-memory cache
* Containerization using Docker
* Fundamentals of Kubernetes deployments
* Kubernetes Services & ConfigMaps
* Ingress routing for HTTP services
* Running production-style architecture locally

--
