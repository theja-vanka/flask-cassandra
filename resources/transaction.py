# Flast RESTFull Dependencies
from flask_restful import Resource, reqparse

# Model dependencies
from models.transaction import TransactionMaster
from models.items import ItemMaster
from models.customer import CustomerMaster

# For Aggregate Functions
from helpers.cassandradb import CassandraSession
from helpers.globalvar import asyncquery
import operator

# Customer Master API Scaffold
class TransactionMasterPopularityAPI(Resource):

    def get(self):
        # To force a required parameter
        parser = reqparse.RequestParser()
        parser.add_argument('clusterid', type=int, required=True, help='Clusterid cannot be blank')
        data = parser.parse_args()
        # Get all customers in that cluster id
        customers = [dict(row) for row in CustomerMaster.objects.filter(customer_label=data['clusterid']).allow_filtering().all()]
        # Create list of items to be removed from query
        removeitemlist = []
        for customer in customers:
            for request in [dict(row)for row in TransactionMaster.objects.distinct(['item_code','customer_code']).filter(customer_code=customer['customer_code']).allow_filtering().all()]:
                removeitemlist.append(request['item_code'])

        itemTransaction = dict(list(asyncquery.result())[0]['brand_dev.groupbyandsum(item_code, quantity)'])
        [itemTransaction.pop(key) for key in removeitemlist if key in itemTransaction]
        result = dict( sorted(itemTransaction.items(), key=operator.itemgetter(1),reverse=True))
        return result, 200