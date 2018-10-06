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
        '''Gets azimuth direction of the antenna'''
        self._send_cmd(self.GET_AZIMUTH) # Sends the request to the Rotor

        azimuth = self._port.readline().strip() # Reads the response from the Rotor
        return  azimuth

