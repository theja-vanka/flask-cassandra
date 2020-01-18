# Flask Dependencies
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

# Controller Dependencies
from resources.customer import CustomerMasterAPI
from resources.ping import pingAPI

# Cassandra Session and Connection Dependencies
from cassandra.cqlengine import connection
from helpers.cassandradb import CassandraSession

# Flask Constructors
app = Flask(__name__)
CORS(app)
api = Api(app)

# RESTFull End-points
api.add_resource(pingAPI, '/ping') #http://127.0.0.1:8080/ping
api.add_resource(CustomerMasterAPI, '/getCustomers') #http://127.0.0.1:8080/getCustomers

# Main Function for app
if __name__ == '__main__':
    cassObj = CassandraSession()
    connection.set_session(cassObj.session)
    app.run(host='127.0.0.1', port=8080, debug=True)