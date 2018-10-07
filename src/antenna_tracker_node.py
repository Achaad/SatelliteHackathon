from pyorbital.orbital import Orbital
from datetime import datetime


class Tracker:

    orb = Orbital('NANOSAT C BR1', 'C:\\Users\\karlm\\PycharmProjects\\SatelliteHackathonnew\\src\\tle\\current_tle.txt')
    #orb = Orbital("Suomi NPP")
    now = datetime.utcnow()
    # Get longitude, latitude and altitude of the satellite
    print("Longitude, latitude and altitude")
    print(orb.get_lonlatalt(now))

    #tle.get_lonlatalt()
