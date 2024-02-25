# import libraries
import matplotlib.pyplot as plt
import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.warningissuer import marking, predict_risk_level,get_relative_predicted_level,get_danger_level
from floodsystem.analysis import polyfit

stations = build_station_list()
update_water_levels(stations)

data = stations_level_over_threshold(stations, 0)[0][0]
# dt = 10
# for i in data:
#     dates,levels = fetch_measure_levels(i[0].measure_id,dt=datetime.timedelta(days=dt))
#     plot_water_level_with_fit(i[0], dates, levels, 1)
risk_stations = {}
dates,levels = fetch_measure_levels(data.measure_id,dt=datetime.timedelta(days=10))
predicted_level = predict_risk_level(data, dates, levels, 1, 2)
risk_stations[data.name] = marking(get_relative_predicted_level(data,predicted_level))
print(risk_stations)
