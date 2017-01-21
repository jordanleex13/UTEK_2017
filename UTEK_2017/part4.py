from part2 import get_distance_and_time
import urllib, json
from haversine import haversine_func

class Node:

    def __init__(self, latitude, longitude, name, id):
        self.latitude = latitude
        self.longitude = longitude
        #self.distance = distance
        self.name = name
        self.id = id
        self.closePointsList = []

    def mPrint(self):
        mString = str(self.latitude) + " " + str(self.longitude) + " " + str(self.name) + " " + str(self.id)
        print mString

    def close_points(self, graph):
        # return list of nodes that are within 480km
        for node in graph:
            if node.id == self.id:
                continue
            dist = haversine_func(self.latitude, self.longitude, node.latitude, node.longitude)

            if dist <= 480:
                self.closePointsList.append(node)

class Graph:

    def __init__(self):
        # Make the request and get the JSON
        #url = "https://gist.githubusercontent.com/c2huc2hu/4164f3893e2c46c978a3159d307905ba/raw/a1eec746ee4c4c0bc1d3dc66fc4c6c07c3b81b7a/charging_stations.json"
        #response = urllib.urlopen(url)
        data = json.load(open("charging_stations.json"))

        # num_results = data["total_results"]
        # print num_results

        list_of_stations = data["fuel_stations"]
        self.list_of_nodes = {}

        for station_dict in list_of_stations:
            latitude = station_dict["latitude"]
            longitude = station_dict["longitude"]
            name = station_dict["station_name"]
            id = station_dict["id"]
            
            self.list_of_nodes[id] = Node(latitude, longitude, name, id)


        for key in self.list_of_nodes:
             self.list_of_nodes[key].mPrint()

    def findPath(self, start, end):
        currNode = Node(start[0], start[1], "start", 0)
        endNode = Node(end[0], end[1], "end", 1)

        path = [currNode]
        dist = 0
        time = 0
        while currNode.latitude != endNode.latitude and currNode.longitude != endNode.longitude:
            candidates = currNode.close_points(self.list_of_nodes)
            hdist=[]



            for node in candidates:
                hdist.append(haversine_func(node.latitude,node.longitude,endNode.latitude,endNode.longitude))
            shortest=min(hdist)
            ind=hdist.index(shortest)
            winner=candidates[ind]
            path.append(winner)

            #dist+=

            currNode=candidates[ind]



def part4(startstr, deststr):
    start_lat, start_lon = map(float, startstr.split(' '))
    dest_lat, dest_lon = map(float, deststr.split(' '))

    startPoint = (start_lat, start_lon)
    destPoint = (dest_lat, dest_lon)

    #path = part4_helper(startPoint, destPoint)

    g = Graph()

    path = part4_helper(startPoint, destPoint)



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




