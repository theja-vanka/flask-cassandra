# Flast RESTFull Dependencies
from flask_restful import Resource, reqparse
import flask
# Model dependencies
from models.cluster import NewClusterMaster
from helpers.cassandradb import CassandraSession

class NewClusterAPI(Resource):

    def get(self):
        # Return all clusters created by user
        result = [dict(row) for row in NewClusterMaster.objects().all()]
        return result, 200

class ClusterPropAPI(Resource):
    
    def get(self):
        data = {}
        data['clusterid'] = flask.request.args.get('clusterid')
        count = NewClusterMaster.objects().count() + 1 
        cassObj = CassandraSession()
        asyncquery = cassObj.session.execute_async('SELECT MAX(poi) FROM poi_frame ;')
        maxvalue = list(asyncquery.result())[0]['system.max(poi)']
        asyncquery = cassObj.session.execute_async('SELECT * FROM poi_frame WHERE customer_label ='+data['clusterid'])
        queryresult = list(asyncquery.result())
        returndict = {}
        returndict['probability'] = (maxvalue - queryresult[0]['poi']) / maxvalue
        returndict['customer_label'] = queryresult[0]['customer_label']
        return returndict, 200