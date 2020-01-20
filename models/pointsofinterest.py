# Cassandra Model Dependencies
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# CustomerMaster Model Class
class PointsOfInterestMaster(Model):
    __table_name__ = 'points_of_interest'
    category = columns.Text(primary_key=True)
    latitude = columns.Double(primary_key=True, clustering_order="ASC")
    longitude = columns.Double(primary_key=True, clustering_order="ASC")
    name = columns.Text(primary_key=True, clustering_order="ASC")