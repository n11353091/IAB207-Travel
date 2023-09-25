from datetime import datetime
class Booking:
    def __init__(self,startdate, enddate, city, user):
        self.startdate = startdate
        self.enddate = enddate
        self.num_guests = 1
        self.city = city
        self.user = user
    def __repr__(self):
        str = f"User: {self.user}\nCity: {self.city.name}\nStart date: {self.startdate}\nEnd date: {self.enddate}\nNumber of Guests: {self.num_guests}"
        return str