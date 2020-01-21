# Cassandra Model Dependencies
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# CustomerMaster Model Class
class PointsOfInterestFrame(Model):
    __table_name__ = 'poi_frame'
    __keyspace__ = 'brand_dev'
    customer_label = columns.Integer(primary_key=True)
    poi = columns.Integer(primary_key=True)
    