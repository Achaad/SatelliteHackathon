from src.antenna_rotation_node import Rotor
from src.tle2signal import TLEConverter
import schedule
import time
import math
import logging

class Tracker(Rotor, TLEConverter):
    def __init__(self, com_port, tle_path):

        Rotor.__init__(self, com_port)
        TLEConverter.__init__(self, tle_path)
        self.azimuth = 0
        self.elevation = 0

    def __call__(self):
        self.run_program()

    def run_program(self):

        schedule.every(1).seconds.do(self.tracking)

        while True:
            schedule.run_pending()
            time.sleep(0.5)

    def tracking(self):
        
        azimuthAndElevation = self.get_signal()

        self.azimuth, self.elevation = azimuthAndElevation[0], azimuthAndElevation[1]
        self.rotate(self.azimuth, self.elevation)
        # print( int(round(self.azimuth, 0)), int(round(self.elevation)) )


def main():
    tracker = Tracker("COM4")
    tracker.run_program()

if __name__ == '__main__':
    main()
