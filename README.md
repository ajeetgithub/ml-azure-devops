🚀 Azure DevOps CI/CD Machine Learning API

📌 Project Overview

This project demonstrates a complete DevOps workflow for deploying a Machine Learning prediction API using:

Azure Cloud Shell

GitHub Actions (CI)

Azure Pipelines (CD)

Azure App Service

Azure CLI

Python (Flask)

Makefile automation

The application exposes a REST API endpoint that returns a JSON-based prediction.

🏗 Architecture Diagram
4
Workflow

Developer pushes code to GitHub

GitHub Actions runs lint + tests (CI)

Azure Pipelines builds and deploys (CD)

Azure App Service hosts the Flask ML API

User sends POST request → receives JSON prediction