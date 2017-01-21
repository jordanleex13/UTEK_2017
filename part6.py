from flask import Flask,render_template,url_for,request
from geopy.geocoders import Nominatim
from part4 import startPath

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
    path = part4.startPath(start_tuple, end_tuple)
    
    name_of_path_points = [start_location.address]
    for index,node in enumerate(path[1:]):
        if index < len(path) - 1:
            name_of_path_points.append(node.address)
    name_of_path_points.append(end_location.address)

    return render_template('search.html',path_names=name_of_path_points)

if __name__ == "__main__":
    APP.run()