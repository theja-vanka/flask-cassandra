from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.customer import CustomerMasterAPI

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(CustomerMasterAPI, '/getCustomers')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)