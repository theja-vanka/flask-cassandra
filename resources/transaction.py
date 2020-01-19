# Flast RESTFull Dependencies
from flask_restful import Resource, reqparse
# Model dependencies
from models.transaction import TransactionMaster
from models.items import ItemMaster
from models.customer import CustomerMaster

# Customer Master API Scaffold
class TransactionMasterPopularityAPI(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('clusterid', type=int, required=True, help='Clusterid cannot be blank')
        data = parser.parse_args()
        customers = [dict(row) for row in CustomerMaster.objects.filter(customer_label=data['clusterid']).allow_filtering().all()]
        removeitemlist = []
        for customer in customers:
            for request in [dict(row)for row in TransactionMaster.objects.distinct(['item_code','customer_code']).filter(customer_code=customer['customer_code']).allow_filtering().all()]:
                removeitemlist.append(request['item_code'])
        items = [dict(row) for row in ItemMaster.objects().all()]
        itemlist = []
        for item in items:
            itemlist.append(item['item_code'])
        for removeitem in removeitemlist:
            if removeitem in itemlist:
                itemlist.remove(removeitem)
        #result = [dict(row) for row in TransactionMaster.objects().all()]
        return itemlist, 200