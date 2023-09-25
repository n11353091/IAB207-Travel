from datetime import datetime
from travel.user import User 
from travel.user import FrequentTraveller
from travel.booking import Booking
from travel.city import City


user = User()
user.register('jill','pass123','jill@google.com')
print(user)
print()
startdate = datetime(2023,11,23,10,0,0)
enddate = datetime(2023,11,30,10,0,0)
brisbane = City('Brisbane', 'City in Queensland with a good weather')
print(brisbane)
print()
booking = Booking(startdate, enddate, brisbane, user)
print(booking)
print()
freq_user = FrequentTraveller()
freq_user.register('jack','pass123', 'jack@google.com', 123231)
print(freq_user)