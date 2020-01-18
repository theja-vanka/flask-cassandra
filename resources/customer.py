from flask_restful import Resource, reqparse
from models.customer import CustomerMaster
from cassandra.cqlengine import connection
from helpers.cassandradb import CassandraSession

class CustomerMasterAPI(Resource):
    cassObj = CassandraSession()
    def get(self):
        connection.set_session(self.cassObj.session)
        return [dict(row) for row in CustomerMaster.objects().all()], 200