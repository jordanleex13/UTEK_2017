from part2 import get_distance_and_time, check_cache
import urllib, json
from haversine import haversine_func

class Node:

    def __init__(self, latitude, longitude, name, id):
        self.latitude = latitude
        self.longitude = longitude
        #self.distance = distance
        self.name = name
        self.id = id

    def mPrint(self):
        mString = str(self.latitude) + " " + str(self.longitude) + " " + self.name + " " + self.id
        print mString

# class Graph:
#     def __init__(self):

class Graph:

    def __init__(self):
        # Make the request and get the JSON
        url = "https://gist.githubusercontent.com/c2huc2hu/4164f3893e2c46c978a3159d307905ba/raw/a1eec746ee4c4c0bc1d3dc66fc4c6c07c3b81b7a/charging_stations.json"
        response = urllib.urlopen(url)
        data = json.loads(response.read())

        # num_results = data["total_results"]
        # print num_results

        list_of_stations = data["fuel_stations"]
        self.adjList = {}

        for station_dict in list_of_stations:
            latitude = station_dict["latitude"]
            longitude = station_dict["longitude"]
            name = station_dict["station_name"]
            id = station_dict["id"]

            self.adjList[id] = Node(latitude, longitude, name, id)

        for node in self.adjList:
            node.mPrint()

def part4(startstr, deststr):
    start_lat, start_lon = map(float, startstr.split(' '))
    dest_lat, dest_lon = map(float, deststr.split(' '))

    startPoint = (start_lat, start_lon)
    destPoint = (dest_lat, dest_lon)

    path = part4_helper(startPoint, destPoint)

    g = Graph()

    for station in path:
        station.mPrint()


# Specs: can drive 480km @ full (80km/hr)
# MINIMIZE dist_from_curr + dist_from_end @ each station
def part4_helper(startPoint, endPoint):

    path = []
    path.append(Node(startPoint[0], startPoint[1], "Start", 0, 0))


    dist, time = get_distance_and_time(startPoint, endPoint)

    # Double[] dist = new Double[g.getV()];
    # Integer[] prev = new Integer[g.getV()]; // this is the path
    #
    # AbstractQueue < Capsule > priority_queue = new PriorityQueue <> ();

    if dist < 480:
        path.append(Node(startPoint[0], startPoint[1], "Start", dist, 1))
        return path







    return path




part4("37.773972 -122.431297", "40.7128 -74.0059")




