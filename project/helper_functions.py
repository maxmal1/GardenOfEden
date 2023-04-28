import urllib.request
import requests
import json
import urllib.parse
from .models import Plot_Location
from flask import url_for

# IP address to test

def location_finder():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    request_url = 'https://geolocation-db.com/jsonp/' + external_ip
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    return result['longitude'],result['latitude']

def street_to_loc(address):
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

    response = requests.get(url).json()
    
    return response[0]["lon"],response[0]["lat"]

def all_plots():
    #format needed is :
    #markers=
    """{
                'icon': icons.alpha.B,
                'lat':  37.4419,
                'lng':  -122.1419,
                'infobox': "Hello I am < b style='color:green;'>B< / b >!"
            }"""
    
    plots = Plot_Location.query.all()
    
    locs = [0]*len(plots)
    count = 0 #"<p style='color:black;'>"+plot.street_addr +"</p>"
    for plot in plots:
        locs[count] = {
            'lat': plot.lat,
            'lng': plot.lon,
            'infobox': "<a href =  " + url_for('auth.add_plant',mid = plot.street_addr) +"><p style='color:black;'>"+plot.street_addr +"</p></a>",
            
        } 
        count+=1
    return locs

def user_plots(userid):
    plots = Plot_Location.query.filter_by(user_id = userid)
    #plots = Plot_Location.query.all()
    return plots

