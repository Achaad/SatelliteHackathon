from pyorbital.orbital import Orbital
from datetime import datetime


class Tracker:

    orb = Orbital('NANOSAT C BR1', 'tle\\current_tle.txt')
    now = datetime.utcnow()
    # Get longitude, latitude and altitude of the satellite
    print("Longitude, latitude and altitude")
    print(orb.get_lonlatalt(now))

    def __init__(self):
        # class_name = self.__class__.__name__
        self.tracking_the_satellite(self.waiting_for_the_satellite)

    def waiting_for_the_satellite(self):
        # While loop
        # Convert orb.get_lonlatalt(now) to longitude and latitude
        """
        While loop runs until the satellite
        is in suitable position to track.
        :return: longitude, latitude
        """

    def tracking_the_satellite(self, longitude, latitude):
        # While the satellite is in our range then track

        """
        Rotate in while loop until it flies out of our range.
        :param longitude:
        :param latitude:
        :return:
        """
