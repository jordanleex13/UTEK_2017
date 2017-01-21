import os
import googlemaps
from tinydb import TinyDB, Query

GMAPS = googlemaps.Client(key="AIzaSyBD9ncqo4K7G03DIF-TO-vaRBxq-FDzlyc")
db = TinyDB('db.json')
query = Query()

def get_distance_and_time(point1, point2):
    distance_matrix = GMAPS.distance_matrix(point1,point2)
    element = distance_matrix["rows"][0]["elements"][0]
    distance = element["distance"]["value"]
    duration = element["duration"]["value"]
    return distance/100,duration/(60*60)

point1 = (37.773972, -122.431297)
point2 = (37.4931367, -121.9453883)
print(get_distance_and_time(point1, point2))


#format of each dict
#{p1: point1, p2: point2, distance: 3, time: 4}

def check_cache(point1, point2):

    if db.search(query.p1 == point1) and db.search(query.p2 == point2):
        lst = []
        dct = db.search(query.p1 == p1)
        lst.append(dct[distance])
        lst.append(dct[time])

        return lst
    else:
        distance, duration = get_distance_and_time(point1, point2)
        db.insert({'p1': point1, 'p2': point2, 'distance': distance, 'time': duration})
