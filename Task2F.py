# import libraries
import matplotlib.pyplot as plt
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_level_with_fit

stations = build_station_list()
update_water_levels(stations)

data = stations_level_over_threshold(stations, 0)[0:1]
dt = 10
for i in data:
    dates,levels = fetch_measure_levels(i[0].measure_id,dt=datetime.timedelta(days=dt))
    plot_water_level_with_fit(i[0], dates, levels, 1)
