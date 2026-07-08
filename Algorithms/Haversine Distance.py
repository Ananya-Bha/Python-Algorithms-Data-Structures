-----------------------------------
#Finding the Haversine Distance

import math
def haversine_distance(lat1,long1,lat2,long2):
    R=6371
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    long1 = math.radians(long1)
    long2 = math.radians(long2)
    a = (math.sin((lat2-lat1)/2)**2) + (math.cos(lat1)) * (math.cos(lat2)) * (math.sin((long2-long1)/2)**2)
    c = 2 * math.atan2(a**0.5, (1-a)**0.5)
    d = R * c
    return d

lat1=int(input())
long1=int(input())
lat2=int(input())
long2=int(input())

print(haversine_distance(lat1,long1,lat2,long2))

---------------------------------------
