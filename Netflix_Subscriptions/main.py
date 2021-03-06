#This is main file to display the graph of The price of netflix subscription throughout the countries

#Before starting install these : 
#1. pip3 install pandas
#2. pip3 install np
#1. pip install pycountry-convert (to GET COUNTRY_CODES & CONTINENTS)
#2.  pip3 install geopy - To get longitude & Latitude
#3. pip3 install folium -  To create world map
#
#To import data from data.csv
import numpy as np
import pandas as pd
# This is function to convert to country codes and  continents
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2
#This function to get longtitude and latitude
from geopy.geocoders import Nominatim
# Create world map : 
import folium
from folium.plugins import MarkerCluster


#Function to get continent & country code
def get_continent(col):
    try: 
        cn_a2_code = country_name_to_country_alpha2(col)
    except:
        cn_a2_code = 'Unknown'
    try: 
        cn_continents = country_alpha2_to_continent_code(cn_a2_code)
    except:
        cn_continents = 'Unknown'
    return (cn_a2_code , cn_continents)
    
#   This is to get the longtitude & latitude
# This is function to get longtitude and latitude data from country name
geolocator = Nominatim()
def geolocate (country):
    try : 
        #Geolocate the center of the country
        loc = geolocator.geocode(country)
        #Return Latitude & Longitude
        return (loc.latitude , loc.longtitude)
    except : 
        #Return mising value 
        return ('NaN ' , 'NaN')

#To create empty map : 
world_map = folium.Map(tiles = "cartodbpositron")

marker_cluster = MarkerCluster().add_to(world_map)

#For each coordinate , create circlemarker of user percent
for i in range(len(df)):
    lat = df.iloc[i]['Latitude']
    long = df.iloc[i]['Longtitude']
    radius = 5
    popup_text = """Country : {} <br> %of Users : {}"""
    popup_text = popup_text.format(df.iloc[i]['Country'], df.iloc[i]['User_Percent'])
    
    folium.CircleMarker(location = [lat,long] , radius = radius, popup = popup_text , fill= True).add_to(marker_cluster)

#Display the map
world_map
    

