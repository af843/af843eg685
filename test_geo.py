""""Tests for stations_within_radius"""
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_within_radius,rivers_with_station,stations_by_river
from floodsystem.stationdata import build_station_list

def test_stations_within_radius():   
    stations = build_station_list()
    assert len(stations_within_radius(stations, (52.2053, 0.1218), 100)) < len(stations) #output should be fewer than
    assert len(set(stations_within_radius(stations, (52.2053, 0.1218), 100))) == len(stations_within_radius(stations, (52.2053, 0.1218), 100))
    assert len(stations_within_radius(stations, (23.4567,-45.6789), 1000)) == 0 #middle of atlantic
    assert len(stations_within_radius(stations, (23.4567,-45.6789), 100000)) == len(stations) #all stations should be withing 100,000km
    assert type(stations_within_radius(stations, (52.2053, 0.1218), 100)) == list
    assert type(stations_within_radius(stations, (52.2053, 0.1218), 100)[0]) == MonitoringStation
def test_rivers_with_station():
    stations = build_station_list()
    assert len(rivers_with_station(stations)) < len(stations)
    assert len(rivers_with_station([])) == 0
    assert type(rivers_with_station(stations)) == set
    assert type(list(rivers_with_station(stations))[0]) == str
def test_stations_by_river():
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    assert len(stations_by_river(stations)) == len(rivers)
    assert len(stations_by_river(stations)) < len(stations)
    assert type(stations_by_river(stations)) == dict
    assert type(stations_by_river(stations)['River Cam']) == list
    assert type(stations_by_river(stations)['River Cam'][0]) == MonitoringStation
    
