from flask import Flask,render_template,url_for,request
from geopy.geocoders import Nominatim
from part4 import part4Tuple
from urllib.parse import urlencode

geolocator = Nominatim()
APP = Flask(__name__)

@APP.route("/")
def home():
    return render_template('home.html')

@APP.route("/search")
def search():
    start_str = request.args["start"]
    end_str = request.args["end"]
    start_location = geolocator.geocode(start_str)
    end_location = geolocator.geocode(end_str)
    start_tuple = (start_location.latitude, start_location.longitude)
    end_tuple = (end_location.latitude, end_location.longitude)
    path, dist, time = part4Tuple(start_tuple, end_tuple)

    name_of_path_points = [start_location.address]
    params = [('origin',start_location.address),('destination',end_location.address),('waypoints',)]
    for index,node in enumerate(path[1:]):
        if index < len(path) - 2:
            name_of_path_points.append(node.name)
    name_of_path_points.append(end_location.address)

    params = {}
    print(name_of_path_points)
    params['origin'] = start_location.address
    params['destination'] = end_location.address
    params['waypoints'] = '|'.join(name_of_path_points[1:len(name_of_path_points)-1])
    embed_url = "https://www.google.com/maps/embed/v1/directions?key=AIzaSyBD9ncqo4K7G03DIF-TO-vaRBxq-FDzlyc&"
    embed_url += urlencode(params)
    print(embed_url)

    return render_template('search.html',path_names=name_of_path_points,embed_url=embed_url)

if __name__ == "__main__":
    APP.run(debug=True)
