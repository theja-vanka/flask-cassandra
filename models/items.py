# Cassandra Model Dependencies
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# CustomerMaster Model Class
class ItemMaster(Model):
    __table_name__ = 'item_master'
    __keyspace__ = 'brand_dev'
    item_code = columns.Integer(primary_key=True)
    item_name = columns.Text()
    item_label = columns.Integer(primary_key=True, clustering_order="ASC")
    category = columns.Text()