# Cassandra Model Dependencies
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

# CustomerMaster Model Class
class TransactionMaster(Model):
    __table_name__ = 'transaction_master'
    customer_code = columns.Integer(primary_key=True)
    item_code = columns.Integer(primary_key=True)
    item_name = columns.Text()
    item_rate = columns.Double()
    quantity = columns.Double(primary_key=True, clustering_order="DESC")
    amount = columns.Double()