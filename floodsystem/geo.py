# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math

from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    list_station_distance = []
    for i in range(len(stations)):
        d = 2*6.371e6*math.asin(math.sqrt(((math.sin((p[0]-stations[i].coord[0])/2))**2)+(math.cos(stations[i].coord[0]))*(math.cos(p[0]))*(((math.sin((p[1]-stations[i].coord[1])/2))**2))))
        list_station_distance.append((stations[i],d))
    return sorted_by_key(list_station_distance,1)

