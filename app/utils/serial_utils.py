import glob
import sys
import serial


class SerialCommunicator:
    def __init__(self):
        self.serial = None
    
    @staticmethod
    def _available_port() -> str:
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass

        return result[0]

    def setup(self):
        port_name = self._available_port()
        self.serial = serial.Serial(port_name, 11520)
    
    def close(self):
        self.serial.close()


    def write_to_port(self, message: str) -> None:
        self.serial.write(str.encode(message))

serial_communicator = SerialCommunicator()
