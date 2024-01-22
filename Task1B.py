from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

# get stations using build_station_list() from stationdata
stations = build_station_list()

# get distances of stations to p using stations_by_distance() from geo
distance_of_station_to_cambridge = stations_by_distance(stations,(52.2053, 0.1218))

# add town to result
result = []
for i in range(len(distance_of_station_to_cambridge)):
    result.append((distance_of_station_to_cambridge[i][0].name,distance_of_station_to_cambridge[i][0].town,distance_of_station_to_cambridge[i][1]))

# print result
print(result[:10])
print("--------------")
print(result[-10:])