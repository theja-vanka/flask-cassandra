# Flask Dependencies
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

# Controller Dependencies
from resources.customer import CustomerMasterAPI
from resources.customer import CustomerCreateAPI
from resources.cluster import NewClusterAPI
from resources.items import ItemMasterAPI
from resources.transaction import TransactionMasterPopularityAPI
from resources.transaction import TransactionMasterCollaboratorAPI
from resources.transaction import TransactionMasterSellerAPI
from resources.hello import HelloAPI

# Cassandra Session and Connection Dependencies
from cassandra.cqlengine import connection
from helpers.cassandradb import CassandraSession

# Flask Constructors
app = Flask(__name__)
CORS(app)
api = Api(app)

# RESTFull End-points
api.add_resource(HelloAPI,'/') #http://127.0.0.1:8080/
api.add_resource(CustomerMasterAPI, '/getCustomers') #http://127.0.0.1:8080/getCustomers
api.add_resource(CustomerCreateAPI, '/createCluster') #http://127.0.0.1:8080/createCluster
api.add_resource(NewClusterAPI,'/getNewClusters') #http://127.0.0.1:8080/getNewClusters
api.add_resource(ItemMasterAPI, '/getItems') #http://127.0.0.1:8080/getItems
api.add_resource(TransactionMasterPopularityAPI, '/popularityModel') #http://127.0.0.1:8080/popularityModel
api.add_resource(TransactionMasterCollaboratorAPI, '/collaborativeModel') #http://127.0.0.1:8080/collaborativeModel
api.add_resource(TransactionMasterSellerAPI, '/getSelling') #http://127.0.0.1:8080/getSelling

# Main Function for app
if __name__ == '__main__':
    cassObj = CassandraSession()
    connection.set_session(cassObj.session)
    app.run(host='127.0.0.1', port=8080, debug=True)