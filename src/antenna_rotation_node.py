import serial

class Rotor:
    BAUD_RATE = 9600

    # List of available commands
    GET_ELEVATION = 'B'
    GET_AZIMUTH = 'C'
    MOVE_TO = 'W'

    _port = None

    def __init__(self, com_port):
        class_name = self.__class__.__name__
        # opens serial port for communication with Yaesu G-5500
        self._port = serial.Serial(com_port, self.BAUD_RATE, stopbits=1, timeout=None, xonxoff=0, rtscts=0)


    def __delete__(self, instance):
        self._port.close()

    def _send_cmd(self, command):
        '''Sends command to Rotor'''
        self._port.write(command + "\r\n")

    def get_azimuth(self):
        '''Gets azimuth parameter of the antenna'''
        self._send_cmd(self.GET_AZIMUTH) # Sends the request to the Rotor

        azimuth = self._port.readline().strip() # Reads the response from the Rotor
        return  azimuth

    def get_elevation(self):
        '''Gets elevation parameter of the antenna'''
        self._send_cmd(self.GET_ELEVATION)  # Sends the request to the Rotor

        elevation = self._port.readline().strip()   # Reads the response from the Rotor
        return elevation

    def rotate(self, azimuth, elevaation):
        '''Rotates antenna to the given azimuth and elevation'''
        if azimuth < 0 or azimuth > 361:
            return

        if elevaation < 0 or elevaation > 90:
            return

        command = self.MOVE_TO + ' ' + azimuth + ' ' + elevaation
        self._send_cmd(command)


if __name__ == "__main__":
    r = Rotor("COM4")

    print(r.get_elevation())
    print(r.get_azimuth())
    r.rotate(180, 44)