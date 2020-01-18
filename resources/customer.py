from flask_restful import Resource, reqparse
from models.customer import CustomerMaster

class CustomerMasterAPI(Resource):
    def get(self):
        return [dict(row) for row in CustomerMaster.objects().all()], 200