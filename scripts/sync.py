# Cassandra dependencies
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine import connection
from cassandra.auth import PlainTextAuthProvider

# Cassandra Helpers
from helpers.cassandradb import CassandraSession

# Cassandra Data Models
from models.customer import CustomerMaster
from models.cluster import NewClusterMaster
from models.items import ItemMaster
from models.transaction import TransactionMaster

# Session/connection creation
cassObj = CassandraSession()
connection.set_session(cassObj.session)

sync_table(CustomerMaster)
sync_table(NewClusterMaster)
sync_table(ItemMaster)
sync_table(TransactionMaster)