import serial
import logging
import os
import datetime
import time

class Rotor:
    BAUD_RATE = 9600

    # List of available commands
    GET_ELEVATION = 'B'
    GET_AZIMUTH = 'C'
    MOVE_TO = 'W'

    _port = None
    _log = None

    def __init__(self, com_port):
        class_name = self.__class__.__name__
        # opens serial port for communication with Yaesu G-5500
        self._port = serial.Serial(com_port, self.BAUD_RATE, bytesize=8, stopbits=1, timeout=0.5, xonxoff=0, rtscts=0)
        logging.basicConfig(filename=(os.path.abspath(os.pardir) + "/output/rotor.log"), level=logging.DEBUG)
        self._log = logging.getLogger(name="main." + str(class_name))

    def __delete__(self):
        self._port.close()

    def _send_cmd(self, command):
        '''Sends command to Rotor'''
        self._port.write((command + "\r").encode())
        self._log.info(str(datetime.datetime.now()) + ": Executed command: " + command)

    def get_azimuth(self):
        '''Gets azimuth parameter of the antenna'''
        self._send_cmd(self.GET_AZIMUTH) # Sends the request to the Rotor

        azimuth = self._port.readline().strip() # Reads the response from the Rotor
        azimuth = int(azimuth[3:6])
        self._log.info(str(datetime.datetime.now()) + ": Azimuth = " + str(azimuth))
        return  azimuth

    def get_elevation(self):
        '''Gets elevation parameter of the antenna'''
        self._send_cmd(self.GET_ELEVATION)  # Sends the request to the Rotor

        elevation = self._port.readline().strip()  # Reads the response from the Rotor
        elevation = int(elevation[3:6])
        self._log.info(str(datetime.datetime.now()) + ": Elevation = " + str(elevation))
        return elevation

    def rotate(self, azimuth, elevation):
        '''Rotates antenna to the given azimuth and elevation'''
        if azimuth < 0 or azimuth > 361:
            self._log.warning(str(datetime.datetime.now()) + ": Azimuth outside of range: " + str(azimuth))
            return

        if elevation < 0 or elevation > 90:
            self._log.warning(str(datetime.datetime.now()) + ": Elevation outside of range: " + str(elevation))
            return

        elevation = 90 - int(round(elevation, 0))
        azimuth = int(round(azimuth, 0))
        command = self.MOVE_TO + ' ' + str(azimuth) + ' ' + str(elevation)
        self._send_cmd(command)


if __name__ == "__main__":
    # Just an example of the use of this class
    r = Rotor("COM3")

    print(r.get_azimuth())
    print(r.get_elevation())
    r.rotate(180, 44)
    time.sleep(1)
    r.rotate(180, 50)
    time.sleep(1)
    r.rotate(180, 64)
    time.sleep(1)
    r.rotate(180, 74)
