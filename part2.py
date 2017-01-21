import os
import googlemaps
from tinydb import TinyDB, Query

GMAPS = googlemaps.Client(key=os.environ['UTEK_2017_API_KEY'])
db = TinyDB('db.json')

