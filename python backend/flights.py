from airports import Airport
import requests
from datetime import datetime
import sys
# origin_airport = Airport("Origin")
# destination_airport = Airport("Destination")

url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchFlights"

querystring = {"originSkyId":"LOND","destinationSkyId":"NYCA","originEntityId":"27544008","destinationEntityId":"27537542","date":"2025-09-10","cabinClass":"economy","adults":"1","sortBy":"best","currency":"USD","market":"en-US","countryCode":"US"}

headers = {
	"x-rapidapi-key": "397f33e22bmsh01328fc3eb3099cp1fc14ejsnca5184158bdb",
	"x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
}
class Flights:

    def __init__(self, origin, destination):
        # self.origin = origin
        # self.destination = destination
        self.date = self.set_date()
        sys.exit()
        self.query = self.set_query()
        self.response = requests.get(url=url, headers=headers, query=self.query)

    def set_query(self):

        return {"originSkyId":f"{self.origin.get_sky_id()}", "destinationSkyId":f"{self.destination.get_sky_id()}",
                 "originEntityId":f"{self.origin.get_entity_id()}", "destinationEntityId": f"{self.destination.get_entity_id()}",
                 "date": f"{self.date}"}
    
    def set_date(self):
        while True:
            date_str = input("Enter Date (YYYY-MM-DD): ")
            try:
                parsed_date = datetime.strptime(date_str, '%Y-%m-%d')
                if parsed_date < datetime.now():
                    raise RuntimeError
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            except RuntimeError:
                print("Date cannot be in the past. Try again.")
        self.date = date_str


if __name__ == "__main__":
    flights = Flights("yo", "lo")
