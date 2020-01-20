# Cassandra Model Dependencies
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# CustomerMaster Model Class
class ItemMadhuramMaster(Model):
    __table_name__ = 'item_madhuram_master'
    item_code = columns.Integer(primary_key=True)
    item_name = columns.Text()
    item_label = columns.Integer(primary_key=True, clustering_order="ASC")
    category = columns.Text()