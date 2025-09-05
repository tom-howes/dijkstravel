from airport import Airport
from flight import Flight
import requests
from datetime import datetime
import sys
import json
origin_airport = Airport("Origin", "origin.json")
destination_airport = Airport("Destination", "destination.json")

url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchFlights"

querystring = {"originSkyId":"LOND","destinationSkyId":"NYCA","originEntityId":"27544008","destinationEntityId":"27537542","date":"2025-09-10","cabinClass":"economy","adults":"1","sortBy":"best","currency":"USD","market":"en-US","countryCode":"US"}

headers = {
	"x-rapidapi-key": "397f33e22bmsh01328fc3eb3099cp1fc14ejsnca5184158bdb",
	"x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
}
class Flights:

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.date = self.set_date()
        self.query = self.set_query()
        self.response = {}
        with open ("test_flights.json", "r") as f:
            self.response = json.load(f)
        ## Api call
        # self.response = requests.get(url=url, headers=headers, params=self.query).json()
        self.flights = self.set_flights()

    def set_query(self):
        return {"originSkyId":f"{self.origin.get_sky_id()}", "destinationSkyId":f"{self.destination.get_sky_id()}",
                 "originEntityId":f"{self.origin.get_entity_id()}", "destinationEntityId": f"{self.destination.get_entity_id()}",
                 "date": f"{self.date}", "cabinClass":"economy", "adults": 1, "sortBy": "best", "currency":"USD", "market":"en-US", "countryCode": "US"}
    
    def set_date(self):
        while True:
            date_str = input("Enter Date (YYYY-MM-DD): ")
            try:
                parsed_date = datetime.strptime(date_str, '%Y-%m-%d')
                if parsed_date < datetime.now():
                    raise RuntimeError
                return date_str
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            except RuntimeError:
                print("Date cannot be in the past. Try again.")
    
    def set_flights(self):
        if self.response['status'] == False:
            print("No Flights Found")
            sys.exit()
        else:
            flights = {}
            for flight in self.response['data']['itineraries']:
                if len(flight['legs']) > 1:
                    continue
                flight_id = flight['id']
                price = flight['price']['raw']
                flight_seg = flight['legs'][0]['segments'][0]
                flight_num = flight_seg['flightNumber']
                duration = flight_seg['durationInMinutes']
                carrier = flight_seg['operatingCarrier']['name']
                departure = datetime.strptime(flight_seg['departure'], "%Y-%m-%dT%H:%M:%S")
                arrival = datetime.strptime(flight_seg['arrival'], "%Y-%m-%dT%H:%M:%S")
                flights[flight_num] = Flight(id=flight_id, origin=self.origin, destination=self.destination,
                                             duration=duration, price=price, carrier=carrier, departure_time=departure,
                                             arrival_time=arrival)
            
            return flights

    def print_flights(self):
        for key, value in self.flights.items():
            if value.price < 400:
                print(f"Flight Number: {key}\n____")
                value.print_flight()
                print("____")

if __name__ == "__main__":
    flights = Flights(origin_airport, destination_airport)
    flights.print_flights()
