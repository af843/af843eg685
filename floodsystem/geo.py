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
    # this function calculates the distance of a station to a position with coordinate p
    # haversine method is used to calculate distance here
    # return a list of tuples (station_name,distance_to_p) and the list is sorted by distance
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