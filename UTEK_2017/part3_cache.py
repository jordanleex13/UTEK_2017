import os
import googlemaps
from cache import cache

c = cache('data.pickle') #Initialize a cache

GMAPS = googlemaps.Client(key="AIzaSyBD9ncqo4K7G03DIF-TO-vaRBxq-FDzlyc")


def get_distance_and_time(point1, point2):

    #load cache from data.pickle / get previously looked up locations
    c.load_cache()
    #if inputted the same points previously seen, dont make an API call and just return the distance and time
    if (point1,point2) in c.exact_cache:
        return c.exact_cache[(point1,point2)]

    else:
        #if new points, calculate distance and time and put it in the cache
        print("Using API CALL")
        distance_matrix = GMAPS.distance_matrix(point1,point2)
        element = distance_matrix["rows"][0]["elements"][0]
        distance = element["distance"]["value"]
        duration = element["duration"]["value"]
        c.exact_cache[(point1,point2)] = (distance/1000,duration/(60*60))
        c.save_cache()
        return distance/1000,duration/(60*60)


#test
point1 = (37.773972, -122.431297)
point2 = (37.4931367, -121.9453883)

print(get_distance_and_time((37.773972, -122.431297), (37.4931367, -121.9453883)))
