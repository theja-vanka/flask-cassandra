from cassandra.cqlengine.management import sync_table
from models.customer import CustomerMaster
from cassandra.cqlengine import connection
from cassandra.auth import PlainTextAuthProvider
from cassandradb import CassandraSession

cassObj = CassandraSession()
connection.set_session(cassObj.session)

sync_table(CustomerMaster)