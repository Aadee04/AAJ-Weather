import requests
import time

def forecast_five(lat, lon):
	url = 'https://api.openweathermap.org/data/2.5/onecall?lat='+str(lat)+'&lon='+str(lon)+'&exclude=minutely,hourly&appid=c8461f473291c2cfc27b573bfaa572b4'
	data = (requests.get(url)).json()
	timezone = data['timezone_offset']
	day1 = (data['daily'][1])
	day2 = (data['daily'][2])
	day3 = (data['daily'][3])
	day4 = (data['daily'][4])
	day5 = (data['daily'][5])

	weather = {
		'day1':
			{
			'day' : time.strftime('%a',time.gmtime(day1['dt'])),
			'day_temp': int(day1['temp']['day'] - 273.15),
			'night_temp': int(day1['temp']['night'] - 273.15),
			'main': day1['weather'][0]['main'],
			'icon_url': ('http://openweathermap.org/img/wn/' + str(day1['weather'][0]['icon']) + '@2x.png'),
			'pop': (str(round(day1['pop'] * 100)) + '%')
			},
		'day2':
			{
			'day' : time.strftime('%a',time.gmtime(day2['dt'])),
			'day_temp': int(day2['temp']['day'] - 273.15),
			'night_temp': int(day2['temp']['night'] - 273.15),
			'main': day2['weather'][0]['main'],
			'icon_url': ('http://openweathermap.org/img/wn/' + str(day2['weather'][0]['icon']) + '@2x.png'),
			'pop': (str(round(day2['pop'] * 100)) + '%')
			},
		'day3':
			{
			'day' : time.strftime('%a',time.gmtime(day3['dt'])),
			'day_temp': int(day3['temp']['day'] - 273.15),
			'night_temp': int(day3['temp']['night'] - 273.15),
			'main': day3['weather'][0]['main'],
			'icon_url': ('http://openweathermap.org/img/wn/' + str(day3['weather'][0]['icon']) + '@2x.png'),
			'pop': (str(round(day3['pop'] * 100)) + '%')
			},
		'day4':
			{
			'day' : time.strftime('%a',time.gmtime(day4['dt'])),
			'day_temp': int(day4['temp']['day'] - 273.15),
			'night_temp': int(day4['temp']['night'] - 273.15),
			'main': day4['weather'][0]['main'],
			'icon_url': ('http://openweathermap.org/img/wn/' + str(day4['weather'][0]['icon']) + '@2x.png'),
			'pop': (str(round(day4['pop'] * 100)) + '%')
			},
		'day5':
			{
			'day' : time.strftime('%a',time.gmtime(day5['dt'])),
			'day_temp': int(day5['temp']['day'] - 273.15),
			'night_temp': int(day5['temp']['night'] - 273.15),
			'main': day5['weather'][0]['main'],
			'icon_url': ('http://openweathermap.org/img/wn/' + str(day5['weather'][0]['icon']) + '@2x.png'),
			'pop': (str(round(day5['pop'] * 100)) + '%')
			},
	}

	return weather

