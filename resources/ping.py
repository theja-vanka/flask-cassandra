# Flast RESTFull Dependencies
from flask_restful import Resource, reqparse

# Ping API Scaffold
class pingAPI(Resource):

    def get(self):
        return 'Service Active', 200

    def post(self):
        return 'Service Active', 200