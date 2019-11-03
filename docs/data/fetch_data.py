#!/usr/bin/env python
"""

create the data set that is used as the running example

1. get lat and lon for cities
2. fetch elevation 

https://www.nerdwallet.com/blog/snowfall-totals-city/

"""
import re,sys,os
import pandas as pd
from geopy.geocoders import Nominatim
import geocoder
API_KEY = os.environ['GOOGLE_GEO_KEY']

## load data
df = pd.read_csv('annual-snowfall-by-city.csv', delimiter=';')
print(df.head())

def get_state(x):
    """
    return state
    """
    return(re.findall(",\s*[A-Z]+",x)[0][-2:])

def get_city(x):
    """
    return city
    """
    return(re.sub(",\s*[A-Z]+","",x).lower().title())

## clean up city and state
df['state'] = list(map(get_state, df['location']))
df['city'] = list(map(get_city, df['location']))

print(type(df['location'].values))

## use geopy to find latitude and longitude
lats,longs,elevations = [],[],[]

## get lat,long and elevation
for loc in df["location"].values:

    print("\n",loc)
    
    geolocator = Nominatim()
    #g = geocoder.google(loc)
        
    location = geolocator.geocode(loc)
    if location:
        lats.append(location.latitude)
        longs.append(location.longitude)
        g = geocoder.elevation([location.latitude,location.longitude],key=API_KEY)
        elevation = g.meters
        elevations.append(elevation)
        print("\t",location.latitude, location.longitude)
        print("\t",elevation)
    else:
        lats.append("NaN")
        longs.append("NaN")
        elevations.append(elevation)
        print("did not find it")
        
df['lat'] = lats
df['long'] = longs
df['elevation'] = elevations

df.to_csv("snowfall.csv",sep=';')

print(df.head())
