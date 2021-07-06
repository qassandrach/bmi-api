import os
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)



class Bmi (Resource):
   

    def get(self):
        weight = request.args.get('weight', default=None, type=int)
        height = request.args.get('height', default=None, type=int)

        if weight is None and height is None:
            return "ok"
        else:
            message = {}

            bmi = round((weight/pow((height/100),2)),2)

            if bmi < 18.5:
                message["bmi"] = bmi
                message["label"] = "underweight"
            elif bmi >= 18.5 and bmi <= 24.9:
                message["bmi"] = bmi
                message["label"] = "healthy"
            elif bmi >= 25.0:
                message["bmi"] = bmi
                message["label"] = "overweight"
            
            return message
        

api.add_resource(Bmi, "/")

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))