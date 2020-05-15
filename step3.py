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
japan_zone = tz.gettz('Asia/Tokyo')
china_zone = tz.gettz('Asia/Shanghai')
moscow_zone = tz.gettz('Europe/Moscow')
lisbon_zone = tz.gettz('Europe/Lisbon')
ny_zone = tz.gettz('America/New_York')


def generateSecondaryText(phase, city):
    return "{city} time at Madrid's {phase}".format(city=city, phase=phase)


def printOutput(time, from_zone, to_zone, text):
    print(f'{text} {time.replace(tzinfo=from_zone).astimezone(to_zone).strftime("%d/%m/%Y %H:%M:%S")}')


printOutput(s["dawn"], from_zone, madrid_zone, "Dawn Madrid time:")
printOutput(s["sunrise"], from_zone, madrid_zone, "Sunrise Madrid time:")
printOutput(s["noon"], from_zone, madrid_zone, "Noon Madrid time:")
printOutput(s["sunset"], from_zone, madrid_zone, "Sunset Madrid time:")
printOutput(s["dusk"], from_zone, madrid_zone, "Dusk Madrid time:")

printOutput(s["dawn"], from_zone, japan_zone, generateSecondaryText("dawn", "Tokyo"))
printOutput(s["sunrise"], from_zone, japan_zone, generateSecondaryText("sunrise", "Tokyo"))
printOutput(s["noon"], from_zone, japan_zone, generateSecondaryText("noon", "Tokyo"))
printOutput(s["sunset"], from_zone, japan_zone, generateSecondaryText("sunset", "Tokyo"))
printOutput(s["dusk"], from_zone, japan_zone, generateSecondaryText("dusk", "Tokyo"))

printOutput(s["dawn"], from_zone, china_zone, generateSecondaryText("dawn", "Shanghai"))
printOutput(s["sunrise"], from_zone, china_zone, generateSecondaryText("sunrise", "Shanghai"))
printOutput(s["noon"], from_zone, china_zone, generateSecondaryText("noon", "Shanghai"))
printOutput(s["sunset"], from_zone, china_zone, generateSecondaryText("sunset", "Shanghai"))
printOutput(s["dusk"], from_zone, china_zone, generateSecondaryText("dusk", "Shanghai"))

printOutput(s["dawn"], from_zone, moscow_zone, generateSecondaryText("dawn", "Moscow"))
printOutput(s["sunrise"], from_zone, moscow_zone, generateSecondaryText("sunrise", "Moscow"))
printOutput(s["noon"], from_zone, moscow_zone, generateSecondaryText("noon", "Moscow"))
printOutput(s["sunset"], from_zone, moscow_zone, generateSecondaryText("sunset", "Moscow"))
printOutput(s["dusk"], from_zone, moscow_zone, generateSecondaryText("dusk", "Moscow"))

printOutput(s["dawn"], from_zone, lisbon_zone, generateSecondaryText("dawn", "Lisbon"))
printOutput(s["sunrise"], from_zone, lisbon_zone, generateSecondaryText("sunrise", "Lisbon"))
printOutput(s["noon"], from_zone, lisbon_zone, generateSecondaryText("noon", "Lisbon"))
printOutput(s["sunset"], from_zone, lisbon_zone, generateSecondaryText("sunset", "Lisbon"))
printOutput(s["dusk"], from_zone, lisbon_zone, generateSecondaryText("dusk", "Lisbon"))

printOutput(s["dawn"], from_zone, ny_zone, generateSecondaryText("dawn", "NY"))
printOutput(s["sunrise"], from_zone, ny_zone, generateSecondaryText("sunrise", "NY"))
printOutput(s["noon"], from_zone, ny_zone, generateSecondaryText("noon", "NY"))
printOutput(s["sunset"], from_zone, ny_zone, generateSecondaryText("sunset", "NY"))
printOutput(s["dusk"], from_zone, ny_zone, generateSecondaryText("dusk", "NY"))
