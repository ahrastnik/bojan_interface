"""
Bojan communication
"""
import serial                       # import pySerial
import  time
from serial.tools import list_ports



class Communication:

    def __init__(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass


    def send(self, data):
        pass

    def read(self):
        return ""


class SerialCom(Communication):

    ser = None

    def __init__(self):
        super().__init__()                              #super().__init__() - call from base class

    def scan_ports(self):
        ports = list_ports.comports(include_links=False)
        return ports

    def serial_connect(self, port, baudrate):
        # if self.ser is not None:
        #     print('Serial connection already opened!')
        #     return

        super().connect()
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        self.ser.open()


    def disconnect(self):
        if self.ser is None:
            print('Serial connection already closed!')
            return

        self.ser.close()
        self.ser = None


    def send(self, data):
        self.ser.write(data.encode('utf-8'))
        self.ser.flush()

    def read(self):                        #Serial send
        data = self.ser.readline()
        data = data.decode("utf-8")
        data = data[0:-2]
        return  data

if __name__ == '__main__':
    serial_communication = SerialCom()

    scanned_ports = (serial_communication.scan_ports())

    port_list = []
    for element in  scanned_ports:
        port_list.append(element.device)
    serial_communication.serial_connect(port_list[0], 9600)   # Enable Serial communication
    i = 1
    while True:
        i=i+1
        serial_communication.send(str(i))
        data = serial_communication.read()
        print(data)











