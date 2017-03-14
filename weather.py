import requests,json,time
from flask import Flask
from flask import render_template
from flask import request

def myWeather(city):
	#the api address
	endpoint = 'http://api.openweathermap.org/data/2.5/weather'
	# the query
	payload = { 'q': city+',uk', 'appid': 'c9388d4d03fe84bb4d47b71d69443c2b' }
	
	#connect and get results
	response = requests.get(endpoint, params=payload)
	
	#debugging code
	#print response.url
	#print response.status_code
	#print response.headers['content-type']
	#print response.text

	result=response.json()
	return result["main"]["temp"], result["weather"][0]["description"], result["sys"]["sunset"]

app = Flask("MyApp")

@app.route("/")
def weather():
	city="London"
	temp, desc, sunset = myWeather(city)
	return render_template("weather.html",city=city,temp=(float(temp)-273),desc=desc)

app.run()
