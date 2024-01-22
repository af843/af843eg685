""" import methods from other files"""
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

"""
output inconsistent stations
"""
stations = build_station_list()
inconsistent_station = inconsistent_typical_range_stations(stations)
inconsistent_station_name = []
for i in inconsistent_station:
    inconsistent_station_name.append(i.name)
print(inconsistent_station_name)
print(len(inconsistent_station_name))