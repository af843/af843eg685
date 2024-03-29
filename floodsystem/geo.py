# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math
from haversine import haversine, Unit

from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    from haversine import haversine, Unit
    """ this function calculates the distance of a station to a position with coordinate p
        haversine method is used to calculate distance here
        return a list of tuples (station_name,distance_to_p) and the list is sorted by distance
    """
    list_station_distance = []
    for i in range(len(stations)):
        d = haversine((stations[i].coord[0],stations[i].coord[1]),p)
        list_station_distance.append((stations[i],d))
    return sorted_by_key(list_station_distance,1)

  
""" [stations_within_radius] uses the haversine function to find the distance between the station and 
the centre, then compares that to the radius. If the distance is less than the radius the station is 
added to the output list.
"""

def stations_within_radius(stations, centre, r):
    from haversine import haversine, Unit
    stations_in_range = []
    for station in stations:
        if haversine(centre, station.coord) < r:
            stations_in_range.append(station)
    return stations_in_range

""" [rivers_with_station] creates an empty set of rivers, then iterates over all stations adding their 
river attribute to the set, a set is used to prevent duplicate entries which would be an issue if
using a list.
"""

def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return rivers

""" [stations_by_river] creates a list of rivers using the rivers_with_station function above, then 
iterates over the rivers, for each river checking the list of stations to assemble a list of stations on
that river. The list of stations is added to the dictionary at the end of the process with the key 
being the name of the river
"""

def stations_by_river(stations):
    rivers = rivers_with_station(stations)
    dictionary = {}
    for river in rivers:
        stationsonriver = []
        for station in stations:
            if station.river == river:
                stationsonriver.append(station)
        dictionary[river] = stationsonriver
    return dictionary 



def rivers_by_station_number(stations, N):
    """
       determines the N rivers with the greatest number of monitoring stations. 
       It should return a list of (river name, number of stations) tuples, sorted by the number of stations. 
       In the case that there are more rivers with the same number of stations as the N th entry, include these rivers in the list.
    """
    River_linked_to_station = stations_by_river(stations)
    list_River_linked_to_station = []
    for i in River_linked_to_station:
        list_River_linked_to_station.append((i,len(River_linked_to_station[i])))
    list_River_linked_to_station = sorted_by_key(list_River_linked_to_station,1)
    list_River_linked_to_station.reverse()
    result = []
    end = N-1
    for i in range(N-1,len(list_River_linked_to_station)):
        if list_River_linked_to_station[i][1] == list_River_linked_to_station[end][1]:
            end = i
        else:
            break
    for i in range(end+1):
        result.append(list_River_linked_to_station[i])
    return result

# creates a list of towns based on the towns with monitoring stations.
def stations_by_town(stations):
    townset = set()
    for station in stations:
        townset.add(station.town)
    return townset

#finds the location of a town by averaging the latitudes and longitudes of the stations with that town
def locate_town(town,stations):
    lat = 0
    long = 0
    numberofstations = 0
    for station in stations:
        if station.town == town:
            lat += station.coord[0]
            long += station.coord[1] 
            numberofstations += 1
    lat = lat/numberofstations
    long = long/numberofstations
    return [lat,long]

# finds and returns all the stations with the town 
def stations_of_town(town,stations):
    stationsoftown = []
    for station in stations:
        if station.town == town:
            stationsoftown.append(station)
    return stationsoftown