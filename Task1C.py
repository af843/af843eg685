from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

monitoringstations = build_station_list()

inrangestations = stations_within_radius(monitoringstations, (52.2053, 0.1218), 10)

names = []
for station in inrangestations:
    names.append(station.name)
    
names.sort()
print(names)