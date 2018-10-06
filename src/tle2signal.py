import ephem
import math
import schedule
import time

class TLEConverter:
    def __init__(self):
        self.GROUND_STATION_LATITUDE = '59.394870'
        self.GROUND_STATION_LONGITUDE = '24.661399'
        self.GROUND_STATION_ELEVATION = 1

    def run_program(self):
        """
        Check the Satellite position every second
        """

        schedule.every(1).seconds.do(self.get_signal)
        while True:
            schedule.run_pending()
            time.sleep(0.5)

    def convert_tuple_to_signal(self, tuple):
        """
        Converts the angle to a range of 0 to pi.
        :param: Tuple of (Azimuth, Altitude)
        """

        def str2float(strlst):
            if float(strlst[0]) < 0:
                return float(strlst[0]) - float(strlst[1]) / 60.0 - float(strlst[2]) / 3600.0
            return float(strlst[0]) + float(strlst[1]) / 60.0 + float(strlst[2]) / 3600.0

        lstAz, lstEle = str(tuple[0]).split(':'), str(tuple[1]).split(':')

        return (str2float(lstAz), str2float(lstEle))

    def get_signal(self):
        """
        Take TLE and compute the azimuth & elevation
        """
        
        tle_lines = []

        for line in open('E:\\Course\\TTU\\CubeSat\\parabol-control-development\\src\\antenna\\antenna_controller\\tle\\tle.txt', 'r').readlines():
            tle_lines.append(line)
        # print("Next satellite TLE: \n{}".format(tle_lines))

        observer = ephem.Observer()
        observer.lat = self.GROUND_STATION_LATITUDE
        observer.long = self.GROUND_STATION_LONGITUDE
        observer.elev = self.GROUND_STATION_ELEVATION
 
        satellite = ephem.readtle(tle_lines[0], tle_lines[1], tle_lines[2])
        satellite.compute(observer)

        # print(self.convert_to_signal(satellite.az), self.convert_to_signal(satellite.alt))
        print(self.convert_tuple_to_signal((satellite.az, satellite.alt)))
        # return (self.convert_to_signal(satellite.az), self.convert_to_signal(satellite.alt))
        return self.convert_tuple_to_signal((satellite.az, satellite.alt))

def main():
    converter = TLEConverter()
    converter.run_program()


if __name__ == '__main__':
    main()