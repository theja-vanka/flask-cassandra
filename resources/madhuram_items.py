# Flast RESTFull Dependencies
from flask_restful import Resource, reqparse
from models.madhuram_items import ItemMadhuramMaster
import collections

# Customer Master API Scaffold
class ItemMadhuramMasterAPI(Resource):

    def get(self):
        result = [dict(row) for row in ItemMadhuramMaster.objects().all()]
        return result, 200