# AI-Learning-Path
This is my journey as a DevOps engineer learning AI

## Prompt Engineering

## Vibe Coding

<details><summary>Prompt Engineering</summary>
<p>

- [github.io: Setup Planning and memory-bank](https://github.com/EnzeD/vibe-coding)

</p>
</details>

<details><summary></summary>
<p>

</p>
</details>

## Understanding AI, LLM and MLOps 
**I got help ChatGPT to prepare this learning plan.**
Goal: Be able to clearly explain and practically implement:
- How to deploy an LLM model on Kubernetes
- How to schedule and scale GPU workloads
- How to make LLM inference production-grade (performance, reliability, observability)
- How basic MLOps practices integrate with infrastructure and platform engineering
 
<details><summary>Practical Python</summary>
<p>

 Tooling and Automation
- Basic Syntax
  - [deeplearining.ai: AI Python for Beginners](https://learn.deeplearning.ai/courses/ai-python-for-beginners/lesson/z57gn/introduction)
- request, pandas, asyncio basics
- Scripting, simple CLI
- API Call (Rest APIs, json handling)
- env/ven, virtualenv/poetry

practic: send request to inference endpoint and get latency and send it as log

</p>
</details>


<details><summary>LLM in Practice</summary>
<p>

- What is Inference? (inference vs training)
- What is embedding?
- What is RAG?
- Vector DB concept
- batching
- Quantization basics
- Latency and cost
- Model Serving

practice: a containerized LLM with simple API

</p>
</details>

<details><summary>Kubernetes Deployment</summary>
<p>

- GPU operator
- node pool for GPU
- device plugin
- resource request/limit for GPU
- HPA/KEDA
- model server (triton / vLLM style)

practice: Deployment with GPU + autoscaling

</p>
</details>

<details><summary>MLOPS</summary>
<p>

- Deploy model on Kubernetes
- Model registry concept
- Versioning
- CI/CD for models
- Canary deploy
- Monitoring latency / token/sec
- drift concept
- rollback

practice: mini-platform   LLM -> CI -> deploy -> metrics -> autoscale -> rollback
</p>
</details>
