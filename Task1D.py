from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

stations = build_station_list()

rivers = rivers_with_station(stations)

print(rivers)

stationsbyriver = stations_by_river(stations)

print(stationsbyriver)