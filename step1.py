from datetime import datetime

from astral import LocationInfo
from astral.sun import sun
from dateutil import tz

city = LocationInfo("Madrid", "Spain", "Europe/Madrid", 44.419177, -3.703295)
print(f"Information for {city.name}/{city.region}")
print(f"Timezone: {city.timezone}")
print(f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n")

s = sun(city.observer, date=datetime.now())

from_zone = tz.gettz('UTC')
madrid_zone = tz.gettz('Europe/Madrid')

print(f'Dawn Madrid time: {s["dawn"].replace(tzinfo=from_zone).astimezone(madrid_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Sunrise Madrid time: {s["sunrise"].replace(tzinfo=from_zone).astimezone(madrid_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(f'Noon Madrid time: {s["noon"].replace(tzinfo=from_zone).astimezone(madrid_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Sunset Madrid time: {s["sunset"].replace(tzinfo=from_zone).astimezone(madrid_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(f'Dusk Madrid time: {s["dusk"].replace(tzinfo=from_zone).astimezone(madrid_zone).strftime("%d/%m/%Y %H:%M:%S")}')
