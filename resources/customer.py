# Flast RESTFull Dependencies
from flask_restful import Resource
import flask

# Model dependencies
from models.customer import CustomerMaster
from models.cluster import NewClusterMaster

# Helper Functions
from helpers.cassandradb import CassandraSession
from helpers.haversine import Haversine
import collections
import random
import string

# Customer Master API Scaffold
class CustomerMasterAPI(Resource):

    def get(self):
        queryresult = [dict(row) for row in CustomerMaster.objects().all()]
        grouped = collections.defaultdict(list)
        for item in queryresult:
            grouped[item['customer_label']].append(item)
        result = []
        for model, group in grouped.items():
            resultdict = {}
            resultdict['customer_label'] =  model
            resultdict['customers'] = group
            result.append(resultdict)
        return result, 200

class CustomerCreateAPI(Resource):

    def post(self):
        
        data = {}
        data['latitude'] = flask.request.args.get('latitude')
        data['longitude'] = flask.request.args.get('longitude')
        
        queryresult = [dict(row) for row in CustomerMaster.objects().all()]
        distmin = 999
        for res in queryresult:
            haverdist = Haversine(res['latitude'], res['longitude'], data['latitude'], data['longitude']).getDistance()
            if haverdist < distmin:
                distmin = haverdist
            if distmin <= 0.1:
                return "Failure", 400
        queryresult = [dict(row) for row in NewClusterMaster.objects().all()]
        for res in queryresult:
            haverdist = Haversine(res['latitude'], res['longitude'], data['latitude'], data['longitude']).getDistance()
            if haverdist < distmin:
                distmin = haverdist
            if distmin <= 0.1:
                return "Failure", 400
        count = NewClusterMaster.objects().count() + 1 
        cassObj = CassandraSession()
        asyncquery = cassObj.session.execute_async("SELECT MAX(customer_label) from customer_master ;")
        inputlabel = list(asyncquery.result())[0]['system.max(customer_label)'] + count
        asyncquery = cassObj.session.execute_async("SELECT MAX(customer_code) from customer_master ;")
        inputcode = list(asyncquery.result())[0]['system.max(customer_code)'] + count
        result = NewClusterMaster.create(customer_label=inputlabel, customer_code=inputcode, customer_name=random.choice(string.ascii_letters[0:4]), latitude=data['latitude'], longitude=data['longitude'])
        return dict(result),200