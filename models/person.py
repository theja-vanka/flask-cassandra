from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import uuid

class Person(Model):
    id = columns.UUID(primary_key=True,default=uuid.uuid4)
    first_name  = columns.Text()
    last_name = columns.Text()