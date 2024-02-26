import matplotlib
import numpy as np

def polyfit(dates, levels, p):
    """
    a function that given the water level time history (dates, levels) for a station computes 
    a least-squares fit of a polynomial of degree p to water level data. 
    The function should return a tuple of (i) the polynomial object 
    and (ii) any shift of the time (date) axis (see below)
    """
    x = matplotlib.dates.date2num(dates)
    y = levels
    p_coeff = np.polyfit(x-x[-1], y, p)
    return p_coeff, x[-1]
