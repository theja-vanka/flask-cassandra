from helpers.cassandradb import CassandraSession
from cassandra.query import dict_factory

cassObj = CassandraSession()
asyncquery = cassObj.session.execute_async("SELECT groupbyandsum(item_code, quantity) from transaction_master")
