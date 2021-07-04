from flask import Flask, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


@app.route("/")
def index():

    weight = request.args.get('weight', type=int)
    height = request.args.get('height', type=int)

    bmi = round((weight/pow((height/100),2)),2)
    health_status = ""

    if bmi < 18.5:
        health_status = "underweight :("
    elif bmi > 18.5 or bmi <= 24.9:
        health_status = "healthy :)"
    elif bmi >= 25.0:
        health_status = "overweight :("
    
    return {"bmi": bmi,
    "label": health_status}