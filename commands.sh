#!/bin/bash

RESOURCE_GROUP="ml-devops-rg"
LOCATION="eastus"
PLAN="ml-devops-plan"
APP_NAME="<your-unique-app-name>"

az login

az group create \
  --name $RESOURCE_GROUP \
  --location $LOCATION

az appservice plan create \
  --name $PLAN \
  --resource-group $RESOURCE_GROUP \
  --sku FREE \
  --is-linux

az webapp create \
  --resource-group $RESOURCE_GROUP \
  --plan $PLAN \
  --name $APP_NAME \
  --runtime "PYTHON|3.9"

az webapp up \
  --name $APP_NAME \
  --resource-group $RESOURCE_GROUP