import os
from part2 import get_distance_and_time
import urllib, json
from haversine import haversine_func


"""
Class to represent a Node in the graph
"""
class Node:

    """ Constructor """
    def __init__(self, latitude, longitude, name, id):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.id = id

    """ Prints according to competitions specification """
    def mPrint(self):
        mString = str(self.latitude) + " " + str(self.longitude) + " " + str(self.name) + " " + str(self.id)
        print (mString)

    """
    Function that takes a dictionary of points as input and returns the list of points that are within 480km
    Arguments:
    list_of_nodes -- the graph of nodes represented by a dictionary
    Return:
    closePointsList -- a list of points that are within 480km
    """
    def close_points(self, list_of_nodes):
        # return list of nodes that are within 480km
        closePointsList = []
        for key in list_of_nodes:
            node = list_of_nodes[key]

            # Skip over self
            if self.id == node.id:
                continue

            dist = haversine_func(self.latitude, self.longitude, node.latitude, node.longitude)
            if dist <= 480:
                closePointsList.append(node)

        return closePointsList


""" Class that represents the graph """
class Graph:

    """ Constructor that parses through JSON file to create the graph """
    def __init__(self):

        # JSON parsing to get list of stations
        data = json.load(open("charging_stations.json"))
        list_of_stations = data["fuel_stations"]

        # the actual graph
        self.list_of_nodes = {}

        for station_dict in list_of_stations:
            latitude = station_dict["latitude"]
            longitude = station_dict["longitude"]
            name = station_dict["city"]
            id = station_dict["id"]

            # Put node into the dictionary
            self.list_of_nodes[id] = Node(latitude, longitude, name, id)

        # Debugging purposes
        # for key in self.list_of_nodes:
        #      self.list_of_nodes[key].mPrint()

    """
    Function that takes a start and end point as input and returns the optimal path, time and distance
    """
    def findPath(self, start, end):

        # Create nodes for start and end
        currNode = Node(start[0], start[1], "Start", 0)
        endNode = Node(end[0], end[1], "End", 1)

        # Initialize with starting node in path
        path = [currNode]
        dist = 0
        time = 0

        while currNode.latitude != endNode.latitude and currNode.longitude != endNode.longitude:

            # Get the list of valid points from the current node
            candidates = currNode.close_points(self.list_of_nodes)
            hdist=[]

            # Check if can reach destination from current node
            if haversine_func(currNode.latitude, currNode.longitude, endNode.latitude, endNode.longitude) <= 480:
                currDist, currTime = get_distance_and_time((currNode.latitude, currNode.longitude),
                                                           (endNode.latitude, endNode.longitude))
                dist += currDist
                time += currTime
                # Don't need to refuel at end so discount the refuelling time
                #time += currDist / 480 * 20
                break

            # Greedy algorithm. Find distance from each candidate to the end then choose the node that minimizes this
            for node in candidates:
                hdist.append(haversine_func(node.latitude, node.longitude, endNode.latitude, endNode.longitude))

            shortest = min(hdist)
            ind = hdist.index(shortest)
            chosen = candidates[ind]
            path.append(chosen)

            currDist, currTime = get_distance_and_time((currNode.latitude, currNode.longitude),
                                                       (chosen.latitude, chosen.longitude))

            # Add onto running sums. Distance in kilometers, time in hours
            dist += currDist
            time += currTime

            # The time to refuel at the station
            # Car can travel 480km then must refuel for 20min to get to full charge again
            time += currDist / 480 * 20 / 60.0

            currNode = chosen

        # At the end, append the end node
        path.append(endNode)
        return (path, time, dist)


"""
Part 4 of the competition

Arguments:
startstr -- the coordinates of the starting point as a string
endstr -- the coordinates of the end point as a string

Output:
outputs the list of nodes along the path, the time, and the distance

Returns:
the path, the time, the distance

"""
def part4(startstr, endstr):
    start_lat, start_lon = map(float, startstr.split(' '))
    end_lat, end_lon = map(float, endstr.split(' '))

    startPoint = (start_lat, start_lon)
    endPoint = (end_lat, end_lon)

    # Check the distance and time from start to end
    dist, time = get_distance_and_time(startPoint, endPoint)

    path = []
    if dist <= 480:
        path.append(Node(startPoint[0], startPoint[1], "Start", 0))
        path.append(Node(endPoint[0], endPoint[1], "End", 1))
        for station in path:
            station.mPrint()
        print (str(time) + " " + str(dist))
        return (path, time, dist)

    # Create the graph and find the path
    g = Graph()
    output = g.findPath(startPoint, endPoint)

    path = output[0]
    for station in path:
        station.mPrint()

    # time then distance
    print(str(output[1]) + " " + str(output[2]))

    return output

"""
Function called from part5.py (the UI application)
Same as part4 but with an additional step to parse the data to a string
"""
def part4Tuple(startTuple, endTuple):
    start_str = startTuple[0] + " " + startTuple[1]
    end_str = endTuple[0] + " " + endTuple[1]

    return part4(start_str,end_str)

# Run from command line
if __name__ == "__main__":
    str1 = input("Enter start coordinate: ")
    str2 = input("Enter end coordinate: ")
    part4(str1, str2)



