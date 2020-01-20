from math import radians, cos, sin, asin, sqrt

class Haversine:
    def __init__(self, latitude1, longitude1, latitude2, longitude2):
        self.lat1 = latitude1
        self.lng1 = longitude1
        self.lat2 = latitude2
        self.lng2 = longitude2

    def __del__(self):
        self.lat1 = None
        self.lng1 = None
        self.lat2 = None
        self.lng2 = None

    def __repr__(self):
        return f"< Latitude1 : {self.lat1}, Longitude1 : {self.lng1},Latitude2 : {self.lat2}, Longitude2 : {self.lng2} >"
    
    def getDistance(self):
        self.lng1, self.lat1, self.lng2, self.lat2 = map(radians, [self.lng1, self.lat1, self.lng2, self.lat2])
        # haversine formula
        self.dlon = self.lng2 - self.lng1
        self.dlat = self.lat2 - self.lat1
        self.a = sin(self.dlat / 2)**2 + cos(self.lat1) * cos(self.lat2) * sin(self.dlon / 2)**2
        self.c = 2 * asin(sqrt(self.a))
        self.r = 6371  # Radius of earth in kilometers. Use 3956 for miles
        return self.c * self.r