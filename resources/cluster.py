# Flast RESTFull Dependencies
from flask_restful import Resource, reqparse

# Model dependencies
from models.cluster import NewClusterMaster

class NewClusterAPI(Resource):

    def get(self):
        result = [dict(row) for row in NewClusterMaster.objects().all()]
        return result, 200