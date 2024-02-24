from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():
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
    test = stations_level_over_threshold(stations,1.2)
    assert len(test) == 2
    assert test[0][1] == 1
    assert test[1][1] == 0.5