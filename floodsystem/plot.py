# import libraries
import matplotlib
import matplotlib.pyplot as plt
import datetime
import numpy as np

from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """
    This function is used to plot a graph  of the water level data against time for a station, 
    and include on the plot lines for the typical low and high levels
    """
    t = dates
    level = levels
    plt.plot(t,level)
    plt.plot(t,[station.typical_range[0] for i in range(len(dates))], linestyle='dotted')
    plt.plot(t,[station.typical_range[1] for i in range(len(dates))], linestyle='dotted')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """
    a function that plots the water level data and the best-fit polynomial
    """
    y = levels
    p_coeff,d0 = polyfit(dates, levels, p)
    poly = np.poly1d(p_coeff)
    dates_ex = []
    for i in range(192):
        dates_ex.append(dates[0]+(192-i)*datetime.timedelta(minutes = 15))
    dates_fit = dates_ex + dates
    plt.plot(dates, y, '.')
    x = matplotlib.dates.date2num(dates_fit)
    plt.plot(dates_fit, poly(x-d0))   
    plt.plot(dates_fit,[station.typical_range[0] for i in range(len(x))], linestyle='dotted')
    plt.plot(dates_fit,[station.typical_range[1] for i in range(len(x))], linestyle='dotted')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show() 

