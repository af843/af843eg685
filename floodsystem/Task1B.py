import geo
import datafetcher

distance_of_station_to_cambridge = geo.stations_by_distance(stations,(52.2053, 0.1218))

result = []
for i in range(len(distance_of_station_to_cambridge)):
    result.append((distance_of_station_to_cambridge[i][0].name,distance_of_station_to_cambridge[i][0].town,distance_of_station_to_cambridge[i][1]))
