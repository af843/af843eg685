from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from haversine import haversine, Unit
from floodsystem.geo import rivers_by_station_number


def test_stations_by_distance():
    p = (0,0)
    stations = [MonitoringStation("","","Clare",(0,0),(0,0),"Nice river","Cambridge"),MonitoringStation("","","Kings",(1,1),"0,0","Long river","Cambridge")]
    result = stations_by_distance(stations, p)
    assert result[0] == (stations[0],haversine((0,0),p))
    assert result[1] == (stations[1],haversine((1,1),p))

test_stations_by_distance()

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

test_rivers_by_station_number()
    
