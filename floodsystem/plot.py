# import libraries
import matplotlib.pyplot as plt
import datetime


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