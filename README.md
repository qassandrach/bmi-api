# Calculate Body Mass Index (BMI) 
API to calculate health status based on Body Mass Index (BMI). Live URL https://bmi-api-7kh3wpfy3a-et.a.run.app/ (inactivated)
## Built with
- Flask 2.0.1
- Flask-RESTful 0.3.9
- Docker
- Google Cloud Run
- Google Artifact Registry
- Google Cloud Build
## Set Up
1. Install [python](https://www.python.org/downloads/), [pip](https://pip.pypa.io/en/stable/cli/pip_install/), [venv](https://cloud.google.com/python/docs/setup) and [docker](https://docs.docker.com/get-docker/) (optional)
2. Clone the repository
## Run the App (without docker)
1. Create a virtual env

    ```
    python3 -m venv env
    source env/bin/activate
    ```
2. Run installation
    ```
    pip install -r requirements.txt
    ```
3. Run the app 
    ```
    python app/app.py
    ```
4. Test the URL http://localhost:5000/?weight=55&height=167.
## Run the App (with docker)
1. Create docker image 

    ```
    docker build -t bmi-image:latest .
    ```
2. Run docker container 

    ```
    docker run -d -p 5000:5000 --name bmi-api bmi-image:latest
    ```
3.  Test the URL http://localhost:5000/?weight=55&height=167.
## Unit Test
1. Activate virtual env

    ```
    source env/bin/activate
    ```
2. Run Test

    ```
    python app/test_app.py
    ```
## Deployment
Create Artifact Registry and Build Trigger in Google Cloud.
1. Fork the repository
2. Install and initialize [Cloud SDK](https://cloud.google.com/sdk/docs/install)
3. Create Artifact Registry

    ```
   gcloud artifacts repositories create bmi-repo --repository-format=docker --location=asia-southeast2 --description="Docker repository"
   ``` 
4. Create Build Triggers

    ```
    gcloud beta builds triggers create github --repo-name=bmi-api \
    --repo-owner=YOUR_GITHUB_USERNAME \
    --branch-pattern=^main$ \
    --build-config=cloudbuild.yaml \
    --name=bmi-api
    ```
5. Create commit to branch `main` in the forked repository to trigger the build, test, and deployment to Cloud Run

