# UTEK_2017     January 21-22, 2017
### Awarded 2nd place out of 30 teams in 2017 Programming competition

### The following is a brief summary of the project
#### Part I
Task: Given a coordinate, parse through a JSON file containing information on all the electric vehicle charging stations
and return the 3 closest stations.

Accomplished in linear time by keeping track of the minimum distance stations and updating those when a lower distance
station was found.

#### Part II
Task: Given a start and end coordinate, return the distance and time to get from start to end.

Utilized GoogleMaps API to accomplish this

#### Part III
Implemented a cache to reduce the API calls in part II.
When using previously inputted coordinates, the cache allows for constant look up time.

#### **Part IV**
Task: Given a start and end coordinate, find the optimal route between the two given:
A) The vehicle can only travel 480km before recharging
B) The list of recharging stations

Implemented a greedy algorithm that chose the next station to go to based on how close it was to the destination (minimizing the the distance from the station to the destination each time).
Used the Haversine formula to approximate which stations would minize the distance between them and the destination before making the API call.

#### **Part V**
Produced a web application that takes user input and displays the results of part IV in an intuitive UI using pure HTML, CSS, and Flask.
