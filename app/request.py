from flask_restful import Resource
from flask import request
from bmi import BmiStatus

class Request(Resource):


    def get(self):
        
        weight = request.args.get('weight', default=None, type=int)
        height = request.args.get('height', default=None, type=int)
        
        bmi = BmiStatus(weight, height)
        response = bmi.calculate()
        return response