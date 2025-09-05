from airport import Airport
from datetime import datetime
class Flight:

    def __init__(self, id: str, origin: Airport, destination: Airport, duration: float, price: float, carrier: str, departure_time: datetime, arrival_time: datetime):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.price = price
        self.carrier = carrier
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def print_flight(self):
        print("Flying From:", end=" ")
        self.origin.print_airport()
        print(f"Flying To:", end=" ")
        self.destination.print_airport()
        print(f"Duration: {str(self.duration // 60)} hours {str(self.duration % 60)} minutes")
        print(f"Price: ${str(self.price)}")
        print(f"Carrier: {self.carrier}")
        print(f"Departing at: {self.departure_time.strftime("%A, %B %d, %H:%M")}")
        print(f"Arriving at: {self.arrival_time.strftime("%A, %B %d, %H:%M")}")
