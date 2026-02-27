# 🍌 Banana Enterprise System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-purple)
![JSON-RPC](https://img.shields.io/badge/JSON--RPC-2.0-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 Distributed Agentic Financial Analysis Platform

Banana is a **distributed, agentic financial analysis system** built with:

- **FastAPI**
- **LangGraph (Agent Orchestration)**
- **FAISS Vector Store**
- **FinBERT Sentiment Model**
- **Open MCP (JSON-RPC 2.0 compliant)**
- **Kubernetes (Minikube)**

It integrates real market data (Alpha Vantage), social sentiment, and SEC filings through distributed MCP microservices.

This is not a demo chatbot — it is a scalable, production-style agentic platform.

---

# 🏗 Architecture Overview

Client
↓
banana-api (LangGraph Orchestrator)
↓
JSON-RPC 2.0 MCP Client
↓
| banana-market (Market MCP) |
| banana-sec (SEC MCP) |
| banana-social (Social MCP) |

↓
External APIs (Alpha Vantage, SEC)
↓
Embedding → FAISS → Retrieval → FinBERT


---

# 📦 Microservices

| Service | Purpose |
|----------|----------|
| banana-api | Agent orchestrator + embedding + RAG |
| banana-market | Market data via Alpha Vantage |
| banana-sec | SEC filings |
| banana-social | Social sentiment tool |

---

# 🔐 Secrets Configuration

Create Kubernetes secret for Alpha Vantage:

```bash
kubectl create secret generic alpha-vantage-secret \
  --from-literal=ALPHA_VANTAGE_API_KEY=YOUR_REAL_KEY

Market MCP injects it via:

env:
  - name: ALPHA_VANTAGE_API_KEY
    valueFrom:
      secretKeyRef:
        name: alpha-vantage-secret
        key: ALPHA_VANTAGE_API_KEY
🛠 Prerequisites

Python 3.12+

Docker Desktop (running)

Minikube

kubectl

Git

Verify:

docker info
minikube status
kubectl get nodes
📥 Clone Repository
git clone https://github.com/gshiva1975/aai-590-capstone-project.git
cd aai-590-capstone-banana_enterprise_system
🚀 Start Minikube
minikube start --driver=docker
kubectl get nodes
🐳 Build Docker Images Inside Minikube
eval $(minikube docker-env)

docker build -t banana-api:v2 .
docker build -t banana-market:v1 -f mcp_servers/Dockerfile.market .
docker build -t banana-sec:v1 -f mcp_servers/Dockerfile.sec .
docker build -t banana-social:v1 -f mcp_servers/Dockerfile.social .

eval $(minikube docker-env -u)
☸️ Deploy to Kubernetes
kubectl apply -f banana-market-deployment.yaml
kubectl apply -f banana-market-service.yaml

kubectl apply -f banana-sec-deployment.yaml
kubectl apply -f banana-sec-service.yaml

kubectl apply -f banana-social-deployment.yaml
kubectl apply -f banana-social-service.yaml

kubectl apply -f banana-api-deployment.yaml
kubectl apply -f banana-api-service.yaml

Verify:

kubectl get pods
kubectl get svc

All pods should show Running.

🌐 Access banana-api

Services are cluster-internal, so port-forward is required:

kubectl port-forward deployment/banana-api 8000:8000

Keep this terminal open.

🧪 Test Full End-to-End Analysis
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"query":"How is AAPL performing?"}'
Expected Flow:

Extract ticker

JSON-RPC tool calls to MCP services

Market + SEC + Social data fetched

Documents embedded into FAISS

Semantic retrieval

FinBERT sentiment scoring

Threshold logic applied

Final structured JSON response returned

🔎 Test Individual MCP (JSON-RPC 2.0)

From inside cluster:

kubectl run test-pod --rm -it --image=curlimages/curl -- sh

Then:

curl -X POST http://banana-market:8003/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc":"2.0",
    "method":"tools/call",
    "params":{
      "name":"fetch_market_data",
      "arguments":{"ticker":"AAPL"}
    },
    "id":"1"
  }'

Expected response:

{
  "jsonrpc": "2.0",
  "result": [
    "AAPL (2026-02-27) — Open: $272.52, High: $272.81, Low: $262.89, Close: $264.18, Volume: 72184563"
  ],
  "id": "1"
}
🧠 Key Features

✔ Distributed MCP microservices
✔ JSON-RPC 2.0 compliant tool calling
✔ Kubernetes-native architecture
✔ Secret-based API key injection
✔ Real market data integration
✔ FAISS vector memory
✔ Agentic orchestration (LangGraph)
✔ FinBERT sentiment scoring

🔄 Restart After Code Changes

Rebuild image:

eval $(minikube docker-env)
docker build -t banana-market:v1 -f mcp_servers/Dockerfile.market .
eval $(minikube docker-env -u)

Restart deployment:

kubectl rollout restart deployment banana-market
