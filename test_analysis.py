from floodsystem.plot import plot_water_levels
import datetime
import matplotlib.pyplot as plt
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.analysis import polyfit

def test_polyfit():
    stations = build_station_list()
    update_water_levels(stations)
    data = stations_level_over_threshold(stations, 0)[0]
    dates,levels = fetch_measure_levels(data[0].measure_id,dt=datetime.timedelta(days=10))
    ploy,do = polyfit(dates, levels, 4)