# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

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