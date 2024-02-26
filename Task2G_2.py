import matplotlib
import matplotlib.pyplot as plt
import datetime
import numpy as np
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.analysis import polyfit
from floodsystem.warningissuer import flood_predictor, flood_predictor_specific

stations = build_station_list()


flood_predictor_specific("Donyatt",stations,2,10,1)
flood_predictor_specific("Lower Arncott",stations,2,10,1)
flood_predictor_specific("Bray",stations,2,10,1)
flood_predictor_specific("Knettishall",stations,2,10,1)