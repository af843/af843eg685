# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

""" [stations_within_radius] uses the haversine function also defined here to find the distance over the
surface of the earth between the station and the centre, then compares that to the radius. If the 
distance is less than the radius the station is added to the output list.
"""
def haversine(cone, ctwo):
    import math

    deltalat = cone[0] - ctwo[0]
    deltalong = cone[1] - ctwo[1]

    a = math.sin(deltalat/2)**2 + math.cos(cone[0])*math.cos(ctwo[0])*math.sin(deltalong/2)**2
    b = 2*math.atan(math.sqrt(a)*math.sqrt(1-a))**2
    distance = 6371*b
    return distance

def stations_within_radius(stations, centre, r):
    stations_in_range = []
    for station in stations:
        print(station.name)
        if haversine(centre, station.coord) < r:
            stations_in_range.append(station)
    return stations_in_range