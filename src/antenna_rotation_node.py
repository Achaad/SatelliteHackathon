import serial

class Rotor:
    BAUD_RATE = 9600

    _port = None

    def __init__(self, com_port):
        class_name = self.__class__.__name__
        # opens serial port for communication with Yaesu G-5500
        self._port = serial.Serial(com_port, self.BAUD_RATE, stopbits=1, timeout=None, xonxoff=0, rtscts=0)
        