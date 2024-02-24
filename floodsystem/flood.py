from floodsystem.station import MonitoringStation
from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """
    a function that returns a list of tuples, 
    where each tuple holds (i) a station (object) at which the latest relative water level is over tol 
    and (ii) the relative water level at the station. 
    The returned list should be sorted by the relative level in descending order"""
    result = []
    for i in stations:
        if i.typical_range_consistent() == True and i.latest_level != None:
            if i.latest_level > tol:
                result.append((i,i.relative_water_level()))
    result = sorted_by_key(result,1)
    result.reverse()
    return result

def stations_highest_rel_level(stations,N):
    output = []
    stationssorted = stations_level_over_threshold(stations,-9999)
    for i in range(N):
        if stationssorted[i][0].typical_range_consistent == False:
            N += 1
        else:
            output.append(stationssorted[i])
    return output
            