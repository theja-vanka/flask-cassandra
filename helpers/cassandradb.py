# Dependencies for Cassandra
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
from cassandra.auth import PlainTextAuthProvider

class CassandraSession:
    def __init__(self, hostip='104.211.214.233', keyspace='brand_dev'):
        self.hostip = hostip
        self.keyspace = keyspace
        self.auth_provider = PlainTextAuthProvider(username='cassandra', password='N4udsKzcujSx')
        self.cluster = Cluster(contact_points=[self.hostip],auth_provider=self.auth_provider)
        self.session = self.cluster.connect(self.keyspace)
        self.session.row_factory = dict_factory

    def __del__(self):
        self.session.shutdown()

    def __repr__(self):
        return f"< Hostip : {self.hostip}, Keyspace : {self.keyspace} >"