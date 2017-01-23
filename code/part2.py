import os
import googlemaps

# Google Maps API
GMAPS = googlemaps.Client(key="AIzaSyDTmrZ94vmGz881d2uL3tU73V5w6-jhpRk")

"""
Takes two points and calculates the distance between the two and the time to get there
Arguments:
point1 -- the first point
point2 -- the second point
Return:
distance -- the distance in kilometers
duration -- the time in hours
"""
def get_distance_and_time(point1, point2):

    distance_matrix = GMAPS.distance_matrix(point1,point2)
    element = distance_matrix["rows"][0]["elements"][0]
    distance = element["distance"]["value"]
    duration = element["duration"]["value"]

    # Return distance in kilometers and time in hours
    return distance/1000,duration/(60*60)

# Run from command line
if __name__ == "__main__":
    str1 = input("Enter start coordinate: ")
    str2 = input("Enter end coordinate: ")
    start_lat, start_lon = map(float, str1.split(' '))
    end_lat, end_lon = map(float, str2.split(' '))

    point1 = (start_lat, start_lon)
    point2 = (end_lat, end_lon)

    print(get_distance_and_time(point1, point2))

