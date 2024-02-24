from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)

print(stations_highest_rel_level(stations, 3))

