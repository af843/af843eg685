from floodsystem.geo import stations_by_distance,stations_within_radius,rivers_with_station,stations_by_river,rivers_by_station_number,stations_by_town,stations_of_town,locate_town
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

def test_stations_by_distance():
    p = (0,0)
    stations = [MonitoringStation("","","Clare",(0,0),(0,0),"Nice river","Cambridge"),MonitoringStation("","","Kings",(1,1),"0,0","Long river","Cambridge")]
    result = stations_by_distance(stations, p)
    assert result[0] == (stations[0],haversine((0,0),p))
    assert result[1] == (stations[1],haversine((1,1),p))
def test_rivers_by_station_number():
    stations = [MonitoringStation("-","-","1",(0,0),(0,0),"Clare","-"),
                MonitoringStation("-","-","2",(0,0),(0,0),"Clare","-"),
                MonitoringStation("-","-","3",(0,0),(0,0),"Clare","-"),
                MonitoringStation("-","-","4",(0,0),(0,0),"Clare","-"),
                MonitoringStation("-","-","5",(0,0),(0,0),"Clare","-"),
                MonitoringStation("-","-","6",(0,0),(0,0),"Clare","-"),
                MonitoringStation("-","-","7",(0,0),(0,0),"Kings","-"),
                MonitoringStation("-","-","8",(0,0),(0,0),"Kings","-"),
                MonitoringStation("-","-","9",(0,0),(0,0),"Kings","-"),
                MonitoringStation("-","-","10",(0,0),(0,0),"Kings","-"),
                MonitoringStation("-","-","11",(0,0),(0,0),"Kings","-"),
                MonitoringStation("-","-","12",(0,0),(0,0),"Jhons","-"),
                MonitoringStation("-","-","13",(0,0),(0,0),"Jhons","-"),
                MonitoringStation("-","-","14",(0,0),(0,0),"Jhons","-"),
                MonitoringStation("-","-","15",(0,0),(0,0),"Jhons","-"),
                MonitoringStation("-","-","12",(0,0),(0,0),"Trinity","-"),
                MonitoringStation("-","-","13",(0,0),(0,0),"Trinity","-"),
                MonitoringStation("-","-","14",(0,0),(0,0),"Trinity","-"),
                MonitoringStation("-","-","15",(0,0),(0,0),"Trinity","-"),
                MonitoringStation("-","-","16",(0,0),(0,0),"Girton","-"),
                MonitoringStation("-","-","17",(0,0),(0,0),"Girton","-"),
                MonitoringStation("-","-","18",(0,0),(0,0),"Girton","-")
                ]
    result_1 = rivers_by_station_number(stations, 2)
    result_2 = rivers_by_station_number(stations, 3)
    assert result_1 == [("Clare",6),("Kings",5)]
    assert result_2 == [("Clare",6),("Kings",5),("Jhons",4),("Trinity",4)] or [("Clare",6),("Kings",5),("Trinity",4),("Jhons",4)]    
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
def test_stations_by_town():
    stations = build_station_list()
    assert len(stations_by_town(stations)) < len(stations)
    assert len(stations_by_town([])) == 0
def test_stations_of_town():
    stations = build_station_list()
    assert len(stations_of_town('Cam', stations)) > 0
def test_locate_town():
    stations = build_station_list()
    assert locate_town('Cam',stations)[0] 
    assert locate_town('Cam',stations)[1] 