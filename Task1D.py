from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list

stations = build_station_list()

rivers = rivers_with_station(stations)

print(rivers)