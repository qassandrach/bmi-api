from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# @app.route("/")
class Bmi (Resource):

    def get(self):

        weight = request.args.get('weight', type=int)
        height = request.args.get('height', type=int)

        bmi = round((weight/pow((height/100),2)),2)
        health_status = ""

        if bmi < 18.5:
            health_status = "underweight :("
        elif bmi >= 18.5 and bmi <= 24.9:
            health_status = "healthy :)"
        elif bmi >= 25.0:
            health_status = "overweight :("
        
        return {"bmi": bmi,
        "label": health_status}

api.add_resource(Bmi, '/')


if __name__ == '__main__':
   app.run('0.0.0.0','5000')