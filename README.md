# Body Mass Index (BMI) API 
API to calculate health status based on Body Mass Index (BMI). Live URL https://bmi-api-7kh3wpfy3a-et.a.run.app/
## Built with
- Flask 2.0.1
- Flask-RESTful 0.3.9
- Google Cloud Run
- Google Container Registry
- Google Cloud Build
## Run the App (without docker)
1. Clone the repository.
2. Run `pip install -r requirements.txt`
3. Run `python ./app.py`
4. Test the URL http://localhost:5000/?weight=55&height=167.
## Run the App (with docker)
1. Clone the repository.
2. Run `docker build -t <image name>:<tag> .`
3. Run `docker run -d -p 5000:5000 --name <app name> <image name>:<tag>`
4.  Test the URL http://localhost:5000/?weight=55&height=167.
## Unit Test
`python test_app.py`
## Deployment

