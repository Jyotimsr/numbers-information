import phonenumbers
from phonenumbers import timezone,geocoder,carrier

numbers=input("Enter Your No. with+--:")
phone=phonenumbers.parse(numbers)
time=timezone.time_zones_for_nimber(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.desription_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)
