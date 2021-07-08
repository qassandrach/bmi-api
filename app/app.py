from flask import Flask
from flask_restful import Api
from request import Request

app = Flask(__name__)
api = Api(app)

api.add_resource(Request, "/")

if __name__ == '__main__':
   app.run('0.0.0.0','5000')