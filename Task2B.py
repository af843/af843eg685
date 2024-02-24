from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels

# create list for stations
stations = build_station_list()

# get latest level for ewach station
update_water_levels(stations)

# print results in descending order
print(stations_level_over_threshold(stations,0.5))

