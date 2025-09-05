from airport import Airport
from datetime import datetime
class Flight:

    def __init__(self, id: str, origin: Airport, destination: Airport, duration: float, price: float, carrier: str, departure_time: datetime, arrival_time: datetime):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.duration = round(duration / 60, 2)
        self.price = price
        self.carrier = carrier
        self.departure_time = departure_time
        self.arrival_time = arrival_time
