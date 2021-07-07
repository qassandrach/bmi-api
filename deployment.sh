#!/bin/sh

# Input variables
read -p "Enter your github username : .." github_owner

# create artifact registry
echo 'Create artifact repository...'
gcloud artifacts repositories create bmi-repo --repository-format=docker --location=asia-southeast2 --description="Docker repository"

echo 'Authentication to artifact repository...'
# authentication for artifact registry
gcloud auth configure-docker asia-southeast2-docker.pkg.dev

echo 'Create build trigger..'
#create build trigger
gcloud beta builds triggers create github --repo-name=bmi-api \
--repo-owner=$github_owner \
--branch-pattern=^main$ \
--build-config=cloudbuild.yaml \
--name=bmi-api

echo 'completed'
