from antenna_rotation_node import Rotor
from tle2signal import TLEConverter
import schedule
import time
import math

rotator = Rotor("COM3")
converter = TLEConverter()

azimuthAndElevation = 0
azimuth = 150
elevation = 30

# rotator.rotate(150, 30)
# time.sleep(1)

# rotator.rotate(150, 40)
# time.sleep(1)

# rotator.rotate(150, 50)
# time.sleep(1)

# rotator.rotate(150, 60)
# time.sleep(1)

while True:
    time.sleep(1)
    azimuthAndElevation = converter.get_signal()
    # azimuth, elevation = round(azimuthAndElevation[0], 3), round(azimuthAndElevation[1], 3)
    rotator.rotate(azimuth, abs(elevation))
    print("azimuth", azimuth, "elevation ", abs(elevation))
    elevation += 10

