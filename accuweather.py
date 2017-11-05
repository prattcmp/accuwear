import requests, json

def get_weather():
	request = requests.get('http://freegeoip.net/json')
	location_data = request.json()

	url = 'http://dataservice.accuweather.com/locations/v1/postalcodes/search'
	params = (
    	('apikey', 'HackPSU2017'),
    	('q', location_data['zip_code'])
	)

	request = requests.get(url, params=params)
	key_data = request.json()
		
	url = 'http://dataservice.accuweather.com/currentconditions/v1/' + key_data[0]['Key']
	params = (
    	('apikey', 'HackPSU2017'),
    	('details', 'true')
	)

	request = requests.get(url, params=params)
	data = request.json()

	realFeelTemp = data[0]['RealFeelTemperatureShade']['Imperial']['Value']
	realFeelTemp = int(realFeelTemp)
	
	if realFeelTemp < 0:
		description = 'Why the f*** are you outside'
	elif 0 <= realFeelTemp < 32:
		description = 'Bundle Up! Its pretty cold out there. Put a winter coat on'
		image = 'images/parka.jpg'
	elif 35 <= realFeelTemp < 50:
		description = 'Pretty chilly out there. Put this on!'
		image = 'images/fleece.png'
	elif 50 <= realFeelTemp < 60:
		description =  'Its a little chilly, might wanna grab a sweatshirt!'
		image = 'images/Sweatshirt.gif'
	elif 60 <= realFeelTemp < 70:
		description = 'No need for a jacket today, but still try to keep your arms covered!'
		image = 'images/longsleeve.jpg'
	elif 70 <= realFeelTemp < 80:
		description = 'Pretty warm today, try to stay cool!'
		image = 'images/Tshirt.png'
	elif 80 <= realFeelTemp:
		description = 'Woah! Its pretty hot out there! Try not to sweat!'
		image = 'images/tank.png'
		
	return (image, description, realFeelTemp)