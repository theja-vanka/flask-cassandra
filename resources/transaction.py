# Flast RESTFull Dependencies
from flask_restful import Resource, reqparse

# Model dependencies
from models.transaction import TransactionMaster
from models.items import ItemMaster
from models.customer import CustomerMaster

# For Aggregate Functions
from helpers.cassandradb import CassandraSession
from collections import Counter

# Customer Master API Scaffold
class TransactionMasterPopularityAPI(Resource):

    def get(self):
        # To force a required parameter
        parser = reqparse.RequestParser()
        parser.add_argument('clusterid', type=int, required=True, help='Clusterid cannot be blank')
        data = parser.parse_args()
        # Async query started
        cassObj = CassandraSession()
        asyncquery = cassObj.session.execute_async("SELECT groupbyandsum(item_code, quantity) from transaction_master")
        # Get all customers in that cluster id
        customers = [dict(row) for row in CustomerMaster.objects.filter(customer_label=data['clusterid']).allow_filtering().all()]
        # Create list of items to be removed from query
        removeitemlist = []
        for customer in customers:
            for request in [dict(row)for row in TransactionMaster.objects.distinct(['item_code','customer_code']).filter(customer_code=customer['customer_code']).allow_filtering().all()]:
                removeitemlist.append(request['item_code'])

        itemTransaction = dict(list(asyncquery.result())[0]['brand_dev.groupbyandsum(item_code, quantity)'])
        [itemTransaction.pop(key) for key in removeitemlist if key in itemTransaction]
        topItems = Counter(itemTransaction)
        topItems = topItems.most_common(20) 
        result = []
        for i in topItems:
            _ = {}
            _temp = [dict(row) for row in ItemMaster.objects.filter(item_code=i[0]).all().allow_filtering()]
            _['item_name'] = _temp[0]['item_name']
            _['quantity'] = i[1] / 1000
            result.append(_)
        return result, 200