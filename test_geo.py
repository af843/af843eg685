""""Tests for stations_within_radius"""
from floodsystem.station import MonitoringStation


def test_stations_within_radius():
    from floodsystem.geo import stations_within_radius
    from floodsystem.stationdata import build_station_list
    """"check that the stations within a 100km radius of a few points is less than the total number of stations"""
    stations = build_station_list()
    assert len(stations_within_radius(stations, (52.2053, 0.1218), 100)) < len(stations) #output should be fewer than
    assert len(set(stations_within_radius(stations, (52.2053, 0.1218), 100))) == len(stations_within_radius(stations, (52.2053, 0.1218), 100))
    assert len(stations_within_radius(stations, (23.4567,-45.6789), 1000)) == 0 #middle of atlantic
    assert len(stations_within_radius(stations, (23.4567,-45.6789), 100000)) == len(stations) #all stations should be withing 100,000km
    assert type(stations_within_radius(stations, (52.2053, 0.1218), 100)) == list
    assert type(stations_within_radius(stations, (52.2053, 0.1218), 100)[0]) == MonitoringStation

def test_stations_by_river():
    from floodsystem.geo import stations_by_river, rivers_with_station
    from floodsystem.stationdata import build_station_list
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    assert len(stations_by_river(stations)) == len(rivers)
    assert len(stations_by_river(stations)) < len(stations)
    assert type(stations_by_river(stations)) == dict
    assert type(stations_by_river(stations)['River Cam']) == list
    assert type(stations_by_river(stations)['River Cam'][0]) == MonitoringStation
    
