from dis import COMPILER_FLAG_NAMES
from python_utils import camel_to_underscore
from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

stations = build_station_list()

rivers = sorted(list(rivers_with_station(stations)))

stationsbyriver = stations_by_river(stations)

print(f'There are {len(rivers)} rivers with at least one monitoring station, the first ten of which are:')
print(rivers[0:10])

Aire = stationsbyriver['River Aire']
Cam = stationsbyriver['River Cam']
Thames = stationsbyriver['River Thames']

Airenames = []
Camnames =[]
Thamesnames =[]

for stationa, stationc, stationt in zip(Aire, Cam, Thames):
    Airenames.append(stationa.name)
    Camnames.append(stationc.name)
    Thamesnames.append(stationt.name)


print(f"Stations on the river Aire are {sorted(Airenames)}")
print(f"Stations on the river Cam are {sorted(Camnames)}")
print(f"Stations on the river Thames are {sorted(Thamesnames)}")