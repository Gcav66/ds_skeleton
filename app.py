import os
import googlemaps

GMAPS_KEY = os.environ['GMAPS_KEY']
gmaps = googlemaps.Client(key=GMAPS_KEY)

def geocode_address(address):
    geocode_result = gmaps.geocode(address)
    print (geocode_result)

if __name__ == '__main__':
    geocode_address('1600 Amphitheatre Parkway, Mountain View, CA')