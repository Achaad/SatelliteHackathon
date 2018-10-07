from pyorbital.orbital import Orbital
from datetime import datetime


class Tracker:

    orb = Orbital('NANOSAT C BR1', 'tle\\current_tle.txt')
    now = datetime.utcnow()
    # Get longitude, latitude and altitude of the satellite
    print("Longitude, latitude and altitude")
    print(orb.get_lonlatalt(now))
    # My position
    my_lat = '59.394891599999994'
    my_long = '24.660768899999997'

    def __init__(self):
        # class_name = self.__class__.__name__
        self.waiting_for_the_satellite()
        self.tracking_the_satellite()
        """
        Make these functions continuous
        """


    def waiting_for_the_satellite(self):

        """
        While loop
        If satellite reaches to our range then break the loop
        :return:
        """

    def where_to_turn(self):

        """
        orb.get_lonlatalt(now) what gives us
        longitude, latitude and altitude of the satellite
        calculating where to turn
        and returning azimuth and elevation
        :return: azimuth, elevation
        """


    def tracking_the_satellite(self):
        # Turn to
        # While the satellite is in our range then track

        """
        Rotate in while loop until it flies out of our range.
        :param azimuth:
        :param elevation:
        :return:
        """
