import matplotlib
import matplotlib.pyplot as plt
import datetime
import numpy as np
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
from floodsystem import geo


def marking(relative_level):
    """
    input a station and assess rick of this station
    """
    if relative_level == None:
        return None
    elif relative_level < 1.0:
        return 0
    elif relative_level >= 1.0 and relative_level < 2.0:
        return 1
    elif relative_level >= 2.0 and relative_level < 3.0:
        return 2
    elif relative_level >= 3.0 and relative_level < 4.0:
        return 3
    elif relative_level >= 4.0:
        return 4
    
def predict_risk_level(station, dates, levels, p, time):
    """
    predict water level time days later
    """
    y = levels
    p_coeff,d0 = polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)
    x = dates[0]+datetime.timedelta(days = time)
    x = matplotlib.dates.date2num(x)
    return poly(x-matplotlib.dates.date2num(dates[-1]))

def get_relative_predicted_level(station,predicted_level):
    if predicted_level == None or station.typical_range_consistent() == False:
            return None
    else:
            return (predicted_level-station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])

def get_danger_level(stations,time_after,time_before,degree):
    """
    this function can calculate relative water level of each station 
    and return a dictionary containing station name and rick of flood
    """
    update_water_levels(stations)
    risk_stations = {}
    for i in stations:
        dates,levels = fetch_measure_levels(i.measure_id,dt=datetime.timedelta(days=time_before))
        predicted_level = predict_risk_level(i, dates, levels, degree, time_after)
        risk_stations[i.name] = marking(get_relative_predicted_level(i,predicted_level))
    return risk_stations

def flood_predictor(stations,time_after,time_before,degree):
    towns = list(geo.stations_by_town(stations))
    townstolocations = {}
    townstorisklevel = {}
    for town in towns:
        townstolocations[town] = geo.locate_town(town,stations)
    futurelevels = get_danger_level(stations,time_after,time_before,degree)
    for town in towns:
        stationsintenk = geo.stations_within_radius(stations,townstolocations[town],10)
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
