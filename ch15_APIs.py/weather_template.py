#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 15:04:36 2019

@author: ellenmacpherson
"""

import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather" #Location of the data that we want to fetch.
payload = {"q": "Hobart, Australia", "units":"metric", "appid":"API_HERE"} #The information we want returned. 
response = requests.get(endpoint, params=payload)
data = response.json()

temperature = data['main']['temp']
name = data['name']
weather = data['weather'][0]['main']
print ("It's {} celsius in {} and the sky is {}. \n".format(temperature, name, weather.lower()))

print (response.url)
#print (response.status_code)
#print (response.headers["content-type"])
##print (response.text)
print (data)
