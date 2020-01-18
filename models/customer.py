# Cassandra Model Dependencies
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# CustomerMaster Model Class
class CustomerMaster(Model):
    __table_name__ = 'customer_master'
    customer_code = columns.Integer(primary_key=True)
    customer_name = columns.Text()
    latitude = columns.Double()
    longitude = columns.Double()
    labels = columns.Integer(primary_key=True, clustering_order="ASC")