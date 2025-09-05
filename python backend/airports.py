import requests
import json
import sys

url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"

headers = {
	"x-rapidapi-key": "397f33e22bmsh01328fc3eb3099cp1fc14ejsnca5184158bdb",
	"x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
}

class Airport:

    def __init__(self, node):
        self.node = node
        self.query = self.set_query()
        self.response = {}
        with open("test.json", "r") as f:
            self.response = json.load(f)
        # self.response = requests.get(url, headers=headers, params=self.query).json()
        self.available_airports = self.get_airports()
        self.name = self.select_airport()
        self.sky_id, self.entity_id = self.set_ids()

    def set_query(self):
        city = input(f"Enter your {self.node} City: ")
        return {"query":{city}, "locale":"en-US"}

    def get_airports(self):
        if self.response['status'] == False:
            return ["No Nearby Airports Found"]
        else:
            airports = []
            for airport in self.response['data']:
                airports.append(airport['presentation']['suggestionTitle'])
            return airports

    def select_airport(self):
        if self.available_airports[0] == "No Nearby Airports Found":
            print(self.available_airports[0])
            return
        airports = enumerate(self.available_airports)
        print(f"{self.node} Airports\n__________")
        for index, airport in airports:
            print(f"{index} : {airport}")
        while True:
            try:
                index = int(input("Select an Airport by entering the appropriate number: "))
                name = self.available_airports[index]
                return name
            except IndexError:
                print("Invalid number. try again.")
    
    def set_ids(self):
        for airport in self.response['data']:
            if airport['presentation']['suggestionTitle'] == self.name:
                return airport['skyId'], airport['entityId']
    
    def get_sky_id(self):
        return self.sky_id
    
    def get_entity_id(self):
        return self.entity_id


if __name__ == "__main__":
    
    # for airport in airports['data']:
    #     if airport['presentation']['suggestionTitle'] == "New York John F. Kennedy (JFK)":
    #         print(airport['skyId'])
    #         print(airport['entityId'])
    origin_airport = Airport("Origin")
    print(origin_airport.sky_id, origin_airport.entity_id)