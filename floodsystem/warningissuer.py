import geo,flood,stationdata

def flood_predictor(stations):
    towns = list(geo.stations_by_town(stations))
    townstolocations = {}
    townstorisklevel = {}
    for town in towns:
        townstolocations['town'] = geo.locate_town(town,stations)
    futurelevels = level_predictor(stations, past_data_depth = 2, distance_into_future = 2, poly_degree = 1)
    for town in towns:
        stationsintenk = geo.stations_within_radius(stations,townstolocations['town'],10)
        futureriskscore = 0
        nonestations = 0
        for station in stationsintenk:
            if futurelevels[station.name] == None:
                nonestations += 1
            else:
                futureriskscore += futurelevels[station.name]
        averagefutureriskscore = futureriskscore/(len(stationsintenk) - nonestations)        
        townstorisklevel[town] = averagefutureriskscore
    return townstorisklevel
