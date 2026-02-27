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

## ✅ System Status

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

## 🏗 Architecture

banana-api (Orchestrator + MCP Client)  
        ↓  
banana-social (MCP Tool Server)  

---

## 🔁 Execution Flow

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

## 🛠 Prerequisites

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
