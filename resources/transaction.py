# Flast RESTFull Dependencies
from flask_restful import Resource, reqparse
import flask
# Model dependencies
from models.transaction import TransactionMaster
from models.items import ItemMaster
from models.customer import CustomerMaster

# For Aggregate / Helper Functions
from helpers.cassandradb import CassandraSession
from collections import Counter, defaultdict
import math

# Customer Master API Scaffold
class TransactionMasterPopularityAPI(Resource):

    def get(self):
        # To force a required parameter
        data = {}
        data['clusterid'] = flask.request.args.get('clusterid')# Async query started
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
            _['quantity'] = i[1] / 1212
            result.append(_)
        return result, 200

class TransactionMasterSellerAPI(Resource):
    def get(self):
        # To force a required parameter
        data = {}
        data['clusterid'] = flask.request.args.get('clusterid')# Async query started
        cassObj = CassandraSession()
        asyncquery = cassObj.session.execute_async("SELECT groupbyandsum(item_code, quantity) from transaction_master")
        # Get all customers in that cluster id
        customers = [dict(row) for row in CustomerMaster.objects.filter(customer_label=data['clusterid']).allow_filtering().all()]
        # Create list of items that are selling from query
        sellingitemlist = []
        for customer in customers:
            for request in [dict(row)for row in TransactionMaster.objects.distinct(['item_code','customer_code']).filter(customer_code=customer['customer_code']).allow_filtering().all()]:
                sellingitemlist.append(request['item_code'])
        itemTransaction = dict(list(asyncquery.result())[0]['brand_dev.groupbyandsum(item_code, quantity)'])
        items = {item: itemTransaction[item] for item in sellingitemlist}
        queryresult = []
        for k, v in items.items():
            _ = {}
            _temp = [dict(row) for row in ItemMaster.objects.filter(item_code=k).all().allow_filtering()]
            _temp2 = [dict(row) for row in TransactionMaster.objects.filter(item_code=k).all().allow_filtering()]
            _['item_name'] = _temp[0]['item_name']
            _['category'] = _temp[0]['category']
            _['logquantity'] = math.log1p(v)
            _['quantity'] = v
            _['unitprice'] = round(_temp2[0]['item_rate'])
            queryresult.append(_)
        
        grouped = defaultdict(list)
        for item in queryresult:
            grouped[item['category']].append(item)
        result = []
        for model, group in grouped.items():
            resultdict = {}
            resultdict['category'] =  model
            resultdict['items'] = group
            result.append(resultdict)
        return result, 200       

class TransactionMasterCollaboratorAPI(Resource):
    def get(self):
        # To force a required parameter
        return "Nothing",200