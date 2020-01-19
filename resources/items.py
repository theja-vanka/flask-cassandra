# Flast RESTFull Dependencies
from flask_restful import Resource, reqparse
from models.items import ItemMaster
import collections

# Customer Master API Scaffold
class ItemMasterAPI(Resource):

    def get(self):
        result = [dict(row) for row in ItemMaster.objects().all()]
        return result, 200