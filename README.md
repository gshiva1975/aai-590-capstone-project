# 🍌 Banana Enterprise System  
### AAI-940 Capstone Project  

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green.svg)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-blue.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Orchestration-purple.svg)
![MCP](https://img.shields.io/badge/Open%20MCP-JSON--RPC%202.0-orange.svg)
![FAISS](https://img.shields.io/badge/Vector%20Store-FAISS-lightgrey.svg)
![FinBERT](https://img.shields.io/badge/Sentiment-FinBERT-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Overview

**Banana Enterprise System** is a distributed, agentic financial analysis platform built using:

- FastAPI — API layer  
- LangGraph — Agent orchestration  
- FAISS — Vector storage & retrieval  
- FinBERT — Financial sentiment scoring  
- Open MCP — Model Context Protocol (JSON-RPC 2.0 tool invocation)  
- Kubernetes (Minikube) — Distributed microservices deployment  

This system demonstrates distributed agentic reasoning using structured MCP tool calls within a Kubernetes architecture.

---

##  System Status

✔ banana-api successfully called banana-social  
✔ MCP JSON-RPC client operational  
✔ Social MCP server responding correctly  
✔ Response parsing validated (result field)  
✔ MCP-returned documents embedded dynamically  
✔ FAISS vector store updated  
✔ LangGraph pipeline executed successfully  
✔ FinBERT sentiment scoring applied  
✔ Threshold-based decision logic active  
✔ Fully distributed Kubernetes deployment running  

---

##  Architecture

banana-api (Orchestrator + MCP Client)  
        ↓  
banana-social (MCP Tool Server)  

---

##  Execution Flow

Client  
↓  
FastAPI (/analyze)  
↓  
BananaService  
↓  
LangGraph Orchestrator  
↓  
MCP Client (JSON-RPC 2.0)  
↓  
banana-social MCP Server  
↓  
Tool Execution  

---

##  Prerequisites

Ensure the following are installed and running:

- Python 3.10+
- Docker Desktop
- Minikube
- kubectl
- Git

### Verify Setup

```bash
docker info
minikube status
kubectl get nodes

Installation & Deployment Guide
1️⃣ Clone Repository
git clone https://github.com/gshiva1975/aai-590-capstone-project.git
cd aai-590-capstone-project/aai-590-capstone-banana_enterprise_system

2️⃣ Start Minikube
minikube start --driver=docker
kubectl get nodes

Expected output:

minikube   Ready
3️⃣ Build Docker Images (Inside Minikube)

Switch Docker context:

eval $(minikube docker-env)

Build Banana API:

docker build -t banana-api:v4 .

Build Social MCP Server:

docker build -t banana-social-mcp:v2 -f mcp_servers/Dockerfile.social .

Exit Minikube Docker context:

eval $(minikube docker-env -u)
4️⃣ Deploy to Kubernetes

Deploy Social MCP:

kubectl apply -f banana-social-deployment.yaml
kubectl apply -f banana-social-service.yaml

Deploy Banana API:

kubectl apply -f banana-api-deployment.yaml
kubectl apply -f banana-api-service.yaml

Verify:

kubectl get pods

Expected:

banana-api-xxxxx      1/1 Running
banana-social-xxxxx   1/1 Running

5️⃣ Expose API Locally
kubectl port-forward deployment/banana-api 8000:8000

Keep this terminal running.

6️⃣ Run Test Queries

In a new terminal:

python3 test_queries.py

Expected:

Dynamic MCP tool invocation

Sentiment scoring results

JSON responses

HTTP 200 status codes

🔍 Optional: Verify MCP Connectivity

Run test pod:

kubectl run test-pod --rm -it --image=curlimages/curl -- sh

Inside pod:

curl -X POST http://banana-social:8003/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc":"2.0",
    "method":"tools/call",
    "params":{
      "name":"fetch_social_sentiment",
      "arguments":{"ticker":"AAPL"}
    },
    "id":"1"
  }'

Expected:

{
  "jsonrpc": "2.0",
  "result": ["AAPL trending positively on investor forums"],
  "id": "1"
}
🔄 Updating After Code Changes

Rebuild image:

eval $(minikube docker-env)
docker build -t banana-api:v4 .
eval $(minikube docker-env -u)

Restart deployment:

kubectl rollout restart deployment banana-api
🧹 Cleanup

Stop port-forward:

Ctrl + C

Delete cluster:

minikube delete


🧠 Key Capabilities

Distributed MCP-based tool invocation

JSON-RPC 2.0 compliant

FAISS semantic vector retrieval

FinBERT financial sentiment scoring

Kubernetes-native microservice deployment

Vendor-neutral Open MCP architecture

Agentic orchestration via LangGraph


📌 Important Notes

Port-forward must be re-run after pod restarts

Docker must be running before Minikube

Minikube must be started before deployment

MCP services communicate via Kubernetes DNS


📊 Project Type

Distributed Agentic AI System
Enterprise-ready Kubernetes Architecture
MCP-based Tool-Orchestrated Financial Analysis
