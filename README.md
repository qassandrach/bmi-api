# Calculate Body Mass Index (BMI) 
API to calculate health status based on Body Mass Index (BMI). Live URL https://bmi-api-7kh3wpfy3a-et.a.run.app/
## Built with
- Flask 2.0.1
- Flask-RESTful 0.3.9
- Docker
- Google Cloud Run
- Google Container Registry
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
2. Run `pip install -r requirements.txt`
3. Run `python ./app.py`
4. Test the URL http://localhost:5000/?weight=55&height=167.
## Run the App (with docker)
1. Create docker image 

    ```
    docker build -t <image name>:<tag> .
    ```
2. Run docker container 

    ```
    docker run -d -p 5000:5000 --name <app name> <image name>:<tag>
    ```
3.  Test the URL http://localhost:5000/?weight=55&height=167.
## Unit Test
1. Activate virtual env

    ```
    source env/bin/activate
    ```
2. Run Test

    ```
    python ./test_app.py
    ```
## Deployment
1. Installing and initialize [Cloud SDK] (https://cloud.google.com/sdk/docs/install)
2. Execute

    ```
    chmod +x deployment.sh
    ./deployment.sh
    ``` 

