import os
import googlemaps
from tinydb import TinyDB, Query

GMAPS = googlemaps.Client(key=os.environ['UTEK_2017_API_KEY'])
db = TinyDB('db.json')
query = Query()

#testing
db.insert({'type': 'apple', 'count': 3})
db.insert({'type':'peach', 'count': 3})

if (db.search(query.type == 'apple')):
    print(1234)



print(db.all())
#done testing


#format of each dict
{p1: point1, p2: point2, distance: 3, time: 4}

def check_cache(point1, point2):

    if db.search(query.p1 == point1) and db.search(query.p2 == point2):
        lst = []
        dct = db.search(query.p1 == p1)
        lst.append(dct[distance])
        lst.append(dct[time])

        return lst
    else:
        db.insert({'p1': point1, 'p2': point2, 'distance': 4, 'time': 6})
