# Model Dependencies
from models.customer import CustomerMaster
from models.pointsofinterest import PointsOfInterestMaster

# Cassandra Session and Connection Dependencies
from cassandra.cqlengine import connection
from helpers.cassandradb import CassandraSession

# Cassandra Model Functions
from models.poiframe import PointsOfInterestFrame

# Helper functions
import collections
from helpers.haversine import Haversine

cassObj = CassandraSession()
connection.set_session(cassObj.session)
customers = [dict(row) for row in CustomerMaster.objects().all()]
interest = [dict(row) for row in PointsOfInterestMaster.objects().all()]

grouped = collections.defaultdict(list)
for customer in customers:
    grouped[customer['customer_label']].append(customer)
result = []
for model, group in grouped.items():
    resultdict = {}
    resultdict['customer_label'] =  model
    resultdict['customers'] = group
    result.append(resultdict)

jsondict = []
for cluster in result:
    temp = {}
    temp['customer_label'] = cluster['customer_label']
    temp['POI'] = 0
    for _ in cluster['customers']:
        latitude = _['latitude']
        longitude = _['longitude']
        for _2 in interest:
            dist = Haversine(latitude,longitude,_2['latitude'],_2['longitude']).getDistance()
            if dist <= 1:
                temp['POI'] += 1
    jsondict.append(temp)

for son in jsondict:
    result = PointsOfInterestFrame.create(customer_label=son['customer_label'], poi=son['POI'])