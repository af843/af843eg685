# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


    One_problems_1 = MonitoringStation(s_id, m_id, label, coord,None, river, town)

    One_problems_2 = MonitoringStation(s_id, m_id, label, coord, (5,1), river, town)

    No_problems =  MonitoringStation(s_id, m_id, label, coord, (1,5), river, town)

    assert One_problems_1.typical_range_consistent() == False
    assert One_problems_2.typical_range_consistent() == False
    assert No_problems.typical_range_consistent() == True

def test_inconsistent_typical_range_stations():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    stations = [MonitoringStation(s_id, m_id, label, coord,None, river, town),MonitoringStation(s_id, m_id, label, coord, (5,1), river, town),MonitoringStation(s_id, m_id, label, coord, (1,5), river, town)]
    assert inconsistent_typical_range_stations(stations) == [stations[0],stations[1]]


def test_inconsistent_typical_range_stations():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    stations = [MonitoringStation(s_id, m_id, label, coord,(1,2), river, town),MonitoringStation(s_id, m_id, label, coord, (1,2), river, town),MonitoringStation(s_id, m_id, label, coord, (1,2), river, town),MonitoringStation(s_id, m_id, label, coord,(1,2), river, town),MonitoringStation(s_id, m_id, label, coord, None, river, town)]
    stations[0].latest_level = 1
    stations[1].latest_level = 2
    stations[2].latest_level = 1.5
    stations[3].latest_level = None
    stations[4].latest_level = 2
    assert stations[0].relative_water_level() == 0
    assert stations[1].relative_water_level() == 1
    assert stations[2].relative_water_level() == 0.5
    assert stations[3].relative_water_level() == None
    assert stations[4].relative_water_level() == None
    
