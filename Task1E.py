from floodsystem.geo import rivers_by_station_number,stations_by_river
from floodsystem.stationdata import build_station_list

# get stations using build_station_list() from stationdata
stations = build_station_list()

print(rivers_by_station_number(stations,9))