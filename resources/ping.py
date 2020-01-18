from flask_restful import Resource, reqparse

class pingAPI(Resource):
    
    def get(self):
        return 'Service Active', 200

    def post(self):
        return 'Service Active', 200