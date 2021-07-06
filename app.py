import os
from flask import Flask, request
from flask_restful import Resource, Api
from abc import ABC, abstractmethod

app = Flask(__name__)
api = Api(app)

class Bmi(ABC):
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
   
    @abstractmethod
    def calculate(self):
        result = {}

        bmi = round((self.weight/pow((self.height/100),2)),2)

        if bmi < 18.5:
            result["bmi"] = bmi
            result["label"] = "underweight"
        elif bmi >= 18.5 and bmi <= 24.9:
            result["bmi"] = bmi
            result["label"] = "healthy"
        elif bmi >= 25.0:
            result["bmi"] = bmi
            result["label"] = "overweight"
            
        return result

class Response(Bmi):
    def calculate(self):
        result = super().calculate()
        return result

class Request(Resource):
    def get(self):
        weight = request.args.get('weight', default=None, type=int)
        height = request.args.get('height', default=None, type=int)

        if weight is None and height is None:
            return {"status": 200}
        else:
            bmi = Response(weight, height)
            response = bmi.calculate()
            return response

api.add_resource(Request, "/")

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))