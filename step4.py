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
phases = ['dawn', 'sunrise', 'noon', 'sunset', 'dusk']
external_zones = [{'name': 'Tokyo', 'zone': tz.gettz('Asia/Tokyo')},
                  {'name': 'Beijing', 'zone': tz.gettz('Asia/Shanghai')},
                  {'name': 'Moscow', 'zone': tz.gettz('Europe/Moscow')},
                  {'name': 'Lisbon', 'zone': tz.gettz('Europe/Lisbon')},
                  {'name': 'NY', 'zone': tz.gettz('America/New_York')}]


def generate_secondary_text(phase, city):
    return "{city} time at Madrid's {phase}".format(city=city, phase=phase)


def printOutput(time, from_zone, to_zone, text):
    print(f'{text} {time.replace(tzinfo=from_zone).astimezone(to_zone).strftime("%d/%m/%Y %H:%M:%S")}')


for phase in phases:
    printOutput(s[phase], from_zone, madrid_zone, "{phase_cap} Madrid time:".format(phase_cap=phase.capitalize()))

for external_zone in external_zones:
    for phase in phases:
        printOutput(s[phase], from_zone, external_zone['zone'], generate_secondary_text(phase, external_zone['name']))
