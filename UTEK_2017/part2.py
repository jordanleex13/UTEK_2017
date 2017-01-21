import os
import googlemaps

GMAPS = googlemaps.Client(key="AIzaSyBD9ncqo4K7G03DIF-TO-vaRBxq-FDzlyc")


def get_distance_and_time(point1, point2):
    distance_matrix = GMAPS.distance_matrix(point1,point2)
    element = distance_matrix["rows"][0]["elements"][0]
    distance = element["distance"]["value"]
    duration = element["duration"]["value"]
    return distance/100,duration/(60*60)

point1 = (37.773972, -122.431297)
point2 = (37.4931367, -121.9453883)
print(get_distance_and_time(point1, point2))