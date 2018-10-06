import ephem
import math

class TLEConverter:
    def __init__(self):
        self.GROUND_STATION_LATITUDE = '59.394870'
        self.GROUND_STATION_LONGITUDE = '24.661399'
        self.GROUND_STATION_ELEVATION = 1
        self.MIN_SATELLITE_ELEVATION = 0

    def convert_to_signal(self, time):
        """
        Converts the angle to a range of 0 to pi.
        :param radians: Initial angle
        """
        lst = str(time).split(':')
        return float(lst[0]) + float(lst[1]) / 60.0 + float(lst[2]) / 3600.0

    def get_signal(self):
        final_max_elev_time = ""
        final_max_elev = 0
        tle_lines = []
        for line in open('E:\\Course\\TTU\\CubeSat\\parabol-control-development\\src\\antenna\\antenna_controller\\tle\\tle.txt', 'r').readlines():
            tle_lines.append(line)
        print("Next satellite TLE: \n{}".format(tle_lines))
        print("")

        obs = ephem.Observer()
        obs.lat = self.GROUND_STATION_LATITUDE
        obs.long = self.GROUND_STATION_LONGITUDE
        obs.elevation = self.GROUND_STATION_ELEVATION
 
        print(obs)
        print("")

        satellite = ephem.readtle(tle_lines[0], tle_lines[1], tle_lines[2])
        satellite.compute(obs)
        print(satellite)
        print("")

        rise_time, rise_az, max_elev_time, max_elev, set_time, set_az = obs.next_pass(satellite)
        print("yoo")
        print("rise_time: ", rise_time, " rise_az: ", rise_az, " max_elev_time: ", max_elev_time, "max_elev: ",  max_elev, "set_time: ", set_time, "set_az: ", set_az)

        print("AZ ", satellite.az, "AZ.convert ", self.convert_to_signal(satellite.az),"ELE ", satellite.alt, "ELE.conver ", self.convert_to_signal(satellite.alt))
        return (self.convert_to_signal(satellite.az), self.convert_to_signal(satellite.alt))

def main():
    converter = TLEConverter()
    converter.get_signal()

if __name__ == '__main__':
    main()