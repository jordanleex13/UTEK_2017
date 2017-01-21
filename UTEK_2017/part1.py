# Part 1: Finding a Charging Station

import urllib, json
from haversine import haversine_func

class Station:

    @staticmethod
    def getMax(station0, station1, station2):
        if station0.distance >= station1.distance and station0.distance >= station1.distance:
            return station0, 0
        if station1.distance >= station0.distance and station1.distance >= station2.distance:
            return station1, 1
        if station2.distance >= station0.distance and station2.distance >= station1.distance:
            return station2, 2


    def __init__(self, latitude, longitude, name, distance):
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
        self.name = name

    def mPrint(self):
        mString = str(self.latitude) + " " + str(self.longitude) + " " + self.name + " " + str(self.distance)
        print mString


# The function for part1. Takes coordinate as input, prints 3 closest stations as output
def part1(coordinate):

    # Parse the coordinate string
    given_lat, given_lng = map(float, coordinate.split(' '))

    # Make the request and get the JSON
    url = "https://gist.githubusercontent.com/c2huc2hu/4164f3893e2c46c978a3159d307905ba/raw/a1eec746ee4c4c0bc1d3dc66fc4c6c07c3b81b7a/charging_stations.json"
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    #num_results = data["total_results"]
    #print num_results

    list_of_stations = data["fuel_stations"]
    min_stations = []

    for station_dict in list_of_stations:

        latitude = station_dict["latitude"]
        longitude = station_dict["longitude"]
        name = station_dict["station_name"]
        distance = haversine_func(latitude, longitude, given_lat, given_lng)

        curr_station = Station(latitude, longitude, name, distance)

        if len(min_stations) < 3:
            min_stations.append(curr_station)
        else:
            max_station, index = Station.getMax(min_stations[0], min_stations[1], min_stations[2])

            if curr_station.distance < max_station.distance:
                min_stations[index] = curr_station


    # To sort the list in place by distance
    min_stations.sort(key=lambda x: x.distance, reverse=False)

    for station in min_stations:
        station.mPrint()

part1('38.8977 -77.0365')

