# aai-940-capstone-project

✔ banana-api successfully called banana-social

✔ MCP JSON-RPC client worked

✔ Social MCP server responded correctly

✔ Response parsed correctly (result field)

✔ Researcher embedded MCP-returned docs

✔ Vector store updated dynamically

✔ LangGraph pipeline executed

✔ FinBERT ran

✔ Threshold logic applied

✔ Distributed architecture fully operational


🚀 Banana Enterprise System

Distributed Agentic Financial Analysis using Open MCP + LangGraph + Kubernetes

📌 Overview

Banana is a distributed, agentic financial analysis system built with:

FastAPI

LangGraph (Agent Orchestration)

FAISS Vector Store

FinBERT Sentiment Model

Open MCP (Model Context Protocol)

Kubernetes (Minikube)

Architecture:

banana-api (Orchestrator + MCP Client)
        ↓
banana-social (MCP Tool Server)
🛠 Prerequisites

Make sure you have:

Python 3.10+

Docker Desktop (running)

Minikube

kubectl

Git

Verify:

docker info
minikube status
kubectl get nodes
📥 1️⃣ Clone the Repository
git clone https://github.com/gshiva1975/aai-590-capstone-project.git
cd aai-590-capstone-project/aai-590-capstone-banana_enterprise_system
🚀 2️⃣ Start Minikube
minikube start --driver=docker
kubectl get nodes

You should see:

minikube   Ready
🐳 3️⃣ Build Docker Images (Inside Minikube)

Use Minikube Docker environment:

eval $(minikube docker-env)

Build Banana API:

docker build -t banana-api:v4 .

Build Social MCP Server:

docker build -t banana-social-mcp:v2 -f mcp_servers/Dockerfile.social .

Exit Minikube Docker environment:

eval $(minikube docker-env -u)
☸️ 4️⃣ Deploy to Kubernetes

Apply Social MCP:

kubectl apply -f banana-social-deployment.yaml
kubectl apply -f banana-social-service.yaml

Apply Banana API:

kubectl apply -f banana-api-deployment.yaml
kubectl apply -f banana-api-service.yaml

Verify:

kubectl get pods

You should see:

banana-api-xxxxx      1/1 Running
banana-social-xxxxx   1/1 Running
🌐 5️⃣ Expose API Locally

Use port-forward:

kubectl port-forward deployment/banana-api 8000:8000

Keep this terminal open.

🧪 6️⃣ Run Test Queries

In another terminal:

python3 test_queries.py

You should see:

Dynamic MCP tool calls

Sentiment analysis results

JSON responses

HTTP 200 responses

🔍 7️⃣ Verify MCP Connectivity (Optional)

Test Social MCP directly:

kubectl run test-pod --rm -it --image=curlimages/curl -- sh

Then:

curl -X POST http://banana-social:8003/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"fetch_social_sentiment","arguments":{"ticker":"AAPL"}},"id":"1"}'

Expected output:

{
  "jsonrpc": "2.0",
  "result": ["AAPL trending positively on investor forums"],
  "id": "1"
}
📊 Architecture Diagram
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
🔄 Restart Deployment After Code Changes

Rebuild image:

eval $(minikube docker-env)
docker build -t banana-api:v4 .
eval $(minikube docker-env -u)

Restart:

kubectl rollout restart deployment banana-api
🧹 Cleanup

Stop port-forward:

Ctrl + C

Delete cluster:

minikube delete
🧠 Key Features

Distributed MCP-based tool invocation

JSON-RPC 2.0 compliant

FAISS vector retrieval

FinBERT sentiment scoring

Kubernetes microservice architecture

Vendor-neutral Open MCP

📌 Notes

Port-forward must be re-run after deployment restarts.

Docker must be running.

Minikube must be started before deploying.

MCP services communicate via Kubernetes DNS.
