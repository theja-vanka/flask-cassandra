# Dependencies for Cassandra
from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.query import dict_factory
from cassandra.auth import PlainTextAuthProvider

class CassandraSession:
    def __init__(self, hostip='104.211.214.233', keyspace='brand_dev'):
        self.hostip = hostip
        self.keyspace = keyspace
        self.profile =  ExecutionProfile(request_timeout=6000,row_factory=dict_factory)
        self.auth_provider = PlainTextAuthProvider(username='cassandra', password='N4udsKzcujSx')
        self.cluster = Cluster(contact_points=[self.hostip],
            auth_provider=self.auth_provider,
            execution_profiles={EXEC_PROFILE_DEFAULT: self.profile})
        self.session = self.cluster.connect(self.keyspace)

    def __del__(self):
        self.session.shutdown()

    def __repr__(self):
        return f"< Hostip : {self.hostip}, Keyspace : {self.keyspace} >"