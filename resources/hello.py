# Flast RESTFull Dependencies
from flask_restful import Resource, reqparse

# Customer Master API Scaffold
class HelloAPI(Resource):

    def get(self):
        return 'Flask up and running', 200