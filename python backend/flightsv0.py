import requests
import json

url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchFlights"

querystring = {"originSkyId":"LOND","destinationSkyId":"NYCA","originEntityId":"27544008","destinationEntityId":"27537542","date":"2025-09-10","cabinClass":"economy","adults":"1","sortBy":"best","currency":"USD","market":"en-US","countryCode":"US"}

headers = {
	"x-rapidapi-key": "397f33e22bmsh01328fc3eb3099cp1fc14ejsnca5184158bdb",
	"x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
}

with open ('test_flights.json', 'r') as f:
    flights = json.load(f)
    i = 1
    for flight in flights['data']['itineraries']:
        print(f"Flight {i}\n_____")
        print(f"Flying From: {flight['legs'][0]['origin']['id']}")
        print(f"Flying To: {flight['legs'][0]['destination']['id']}")
        print(f"Price: {flight['price']['raw']}")
        print(f"Duration: {round(int(flight['legs'][0]['durationInMinutes'])/60, 2)} hours")
        i += 1