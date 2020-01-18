from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.customer import CustomerMasterAPI
from resources.ping import pingAPI

from cassandra.cqlengine import connection
from helpers.cassandradb import CassandraSession

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(pingAPI, '/ping')
api.add_resource(CustomerMasterAPI, '/getCustomers')

if __name__ == '__main__':
    cassObj = CassandraSession()
    connection.set_session(cassObj.session)
    app.run(host='127.0.0.1', port=8080, debug=True)