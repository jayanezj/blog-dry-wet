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

print(f'Dawn Madrid time: {s["dawn"].replace(tzinfo=from_zone).astimezone(madrid_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Sunrise Madrid time: {s["sunrise"].replace(tzinfo=from_zone).astimezone(madrid_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(f'Noon Madrid time: {s["noon"].replace(tzinfo=from_zone).astimezone(madrid_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Sunset Madrid time: {s["sunset"].replace(tzinfo=from_zone).astimezone(madrid_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(f'Dusk Madrid time: {s["dusk"].replace(tzinfo=from_zone).astimezone(madrid_zone).strftime("%d/%m/%Y %H:%M:%S")}')

print(
    f'Tokyo time at Madrid\'s dawn: {s["dawn"].replace(tzinfo=from_zone).astimezone(japan_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Tokyo time at Madrid\'s sunrise: {s["sunrise"].replace(tzinfo=from_zone).astimezone(japan_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Tokyo time at Madrid\'s noon: {s["noon"].replace(tzinfo=from_zone).astimezone(japan_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Tokyo time at Madrid\'s sunset: {s["sunset"].replace(tzinfo=from_zone).astimezone(japan_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Tokyo time at Madrid\'s dusk: {s["dusk"].replace(tzinfo=from_zone).astimezone(japan_zone).strftime("%d/%m/%Y %H:%M:%S")}')

print(
    f'Shanghai time at Madrid\'s dawn: {s["dawn"].replace(tzinfo=from_zone).astimezone(china_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Shanghai time at Madrid\'s sunrise: {s["sunrise"].replace(tzinfo=from_zone).astimezone(china_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Shanghai time at Madrid\'s noon: {s["noon"].replace(tzinfo=from_zone).astimezone(china_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Shanghai time at Madrid\'s sunset: {s["sunset"].replace(tzinfo=from_zone).astimezone(china_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Shanghai time at Madrid\'s dusk: {s["dusk"].replace(tzinfo=from_zone).astimezone(china_zone).strftime("%d/%m/%Y %H:%M:%S")}')

print(
    f'Moscow time at Madrid\'s dawn: {s["dawn"].replace(tzinfo=from_zone).astimezone(moscow_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Moscow time at Madrid\'s sunrise: {s["sunrise"].replace(tzinfo=from_zone).astimezone(moscow_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Moscow time at Madrid\'s noon: {s["noon"].replace(tzinfo=from_zone).astimezone(moscow_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Moscow time at Madrid\'s sunset: {s["sunset"].replace(tzinfo=from_zone).astimezone(moscow_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Moscow time at Madrid\'s dusk: {s["dusk"].replace(tzinfo=from_zone).astimezone(moscow_zone).strftime("%d/%m/%Y %H:%M:%S")}')

print(
    f'Lisbon time at Madrid\'s dawn: {s["dawn"].replace(tzinfo=from_zone).astimezone(lisbon_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Lisbon time at Madrid\'s sunrise: {s["sunrise"].replace(tzinfo=from_zone).astimezone(lisbon_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Lisbon time at Madrid\'s noon: {s["noon"].replace(tzinfo=from_zone).astimezone(lisbon_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Lisbon time at Madrid\'s sunset: {s["sunset"].replace(tzinfo=from_zone).astimezone(lisbon_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'Lisbon time at Madrid\'s dusk: {s["dusk"].replace(tzinfo=from_zone).astimezone(lisbon_zone).strftime("%d/%m/%Y %H:%M:%S")}')

print(
    f'NY time at Madrid\'s dawn: {s["dawn"].replace(tzinfo=from_zone).astimezone(ny_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'NY time at Madrid\'s sunrise: {s["sunrise"].replace(tzinfo=from_zone).astimezone(ny_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'NY time at Madrid\'s noon: {s["noon"].replace(tzinfo=from_zone).astimezone(ny_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'NY time at Madrid\'s sunset: {s["sunset"].replace(tzinfo=from_zone).astimezone(ny_zone).strftime("%d/%m/%Y %H:%M:%S")}')
print(
    f'NY time at Madrid\'s dusk: {s["dusk"].replace(tzinfo=from_zone).astimezone(ny_zone).strftime("%d/%m/%Y %H:%M:%S")}')
