import os
import googlemaps
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


    def mPrint(self):
        mString = str(self.latitude) + " " + str(self.longitude) + " " + str(self.name) + " " + str(self.id)
        print (mString)

    def close_points(self, list_of_nodes):
        # return list of nodes that are within 480km
        closePointsList = []
        for key in list_of_nodes:
            node = list_of_nodes[key]
            if self.id  == node.id:
                continue
            dist = haversine_func(self.latitude, self.longitude, node.latitude, node.longitude)

            if dist <= 480:
                closePointsList.append(node)

        return closePointsList

class Graph:

    def __init__(self):

        data = json.load(open("charging_stations.json"))

        list_of_stations = data["fuel_stations"]
        self.list_of_nodes = {}

        for station_dict in list_of_stations:
            latitude = station_dict["latitude"]
            longitude = station_dict["longitude"]
            name = station_dict["station_name"]
            id = station_dict["id"]

            self.list_of_nodes[id] = Node(latitude, longitude, name, id)

        # for key in self.list_of_nodes:
        #      self.list_of_nodes[key].mPrint()

    def findPath(self, start, end):
        currNode = Node(start[0], start[1], "Start", 0)
        endNode = Node(end[0], end[1], "End", 1)

        # Initialize
        path = [currNode]
        dist = 0
        time = 0

        while currNode.latitude != endNode.latitude and currNode.longitude != endNode.longitude:

            candidates = currNode.close_points(self.list_of_nodes)
            hdist=[]

            if haversine_func(currNode.latitude, currNode.longitude, endNode.latitude, endNode.longitude) <= 480:
                currDist, currTime = get_distance_and_time((currNode.latitude, currNode.longitude),(endNode.latitude, endNode.longitude))
                dist += currDist
                time += currTime
                # Don't need to refuel at end
                #time += currDist / 480 * 20
                break

            for node in candidates:
                hdist.append(haversine_func(node.latitude,node.longitude,endNode.latitude,endNode.longitude))
            shortest=min(hdist)
            ind=hdist.index(shortest)

            winner=candidates[ind]
            path.append(winner)

            currDist, currTime = get_distance_and_time((currNode.latitude, currNode.longitude), (winner.latitude, winner.longitude))

            dist += currDist
            time += currTime
            time += currDist / 480 * 20 /60.0


            currNode = candidates[ind]

        path.append(endNode)
        return (path, time, dist)



def part4(startstr, endstr):
    start_lat, start_lon = map(float, startstr.split(' '))
    end_lat, end_lon = map(float, endstr.split(' '))

    startPoint = (start_lat, start_lon)
    endPoint = (end_lat, end_lon)

    dist, time = get_distance_and_time(startPoint, endPoint)

    # Double[] dist = new Double[g.getV()];
    # Integer[] prev = new Integer[g.getV()]; // this is the path
    #
    # AbstractQueue < Capsule > priority_queue = new PriorityQueue <> ();
    path = []
    if dist <= 480:
        path.append(Node(startPoint[0], startPoint[1], "Start", 0))
        path.append(Node(endPoint[0], endPoint[1], "End", 1))
        for station in path:
            station.mPrint()

        return path
    g = Graph()
    output = g.findPath(startPoint, endPoint)

    path = output[0]

    print("\n\n\n\n\n\n\n\n")
    for station in path:
        station.mPrint()
        # time then distance
    print(str(output[1])+ " " + str(output[2]))


# Specs: can drive 480km @ full (80km/hr)
# MINIMIZE dist_from_curr + dist_from_end @ each station





part4("37.773972 -122.431297", "40.7128 -74.0059")
