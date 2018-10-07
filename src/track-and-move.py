from antenna_rotation_node import Rotor
from tle2signal import TLEConverter
import schedule
import time
import math
import logging



class Tracker(Rotor, TLEConverter):
    def __init__(self, com_port):

        Rotor.__init__(self, com_port)
        self.azimuth = 0
        self.elevation = 0

    def run_program(self):

        schedule.every(1).seconds.do(self.tracking)

        while True:
            schedule.run_pending()
            time.sleep(0.5)

    def tracking(self):
        
        azimuthAndElevation = self.get_signal()

        self.azimuth, self.elevation = azimuthAndElevation[0], azimuthAndElevation[1]
        self.rotate(self.azimuth, self.elevation)
        print( int(round(self.azimuth, 0)), int(round(self.elevation)) )


def main():
    tracker = Tracker("COM3")
    tracker.run_program()

if __name__ == '__main__':
    main()
