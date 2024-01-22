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