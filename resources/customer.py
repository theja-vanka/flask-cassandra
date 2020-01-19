# Flast RESTFull Dependencies
from flask_restful import Resource, reqparse
from models.customer import CustomerMaster
import collections

# Customer Master API Scaffold
class CustomerMasterAPI(Resource):

    def get(self):
        queryresult = [dict(row) for row in CustomerMaster.objects().all()]
        grouped = collections.defaultdict(list)
        for item in queryresult:
            grouped[item['labels']].append(item)
        result = []
        for model, group in grouped.items():
            resultdict = {}
            resultdict['label'] =  model
            resultdict['customers'] = group
            result.append(resultdict)
        return result, 200