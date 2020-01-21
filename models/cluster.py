# Cassandra Model Dependencies
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# CustomerMaster Model Class
class NewClusterMaster(Model):
    __table_name__ = 'new_cluster'
    __keyspace__ = 'brand_dev'
    customer_code = columns.Integer(primary_key=True)
    customer_name = columns.Text()
    latitude = columns.Double()
    longitude = columns.Double()
    customer_label = columns.Integer(primary_key=True, clustering_order="ASC")