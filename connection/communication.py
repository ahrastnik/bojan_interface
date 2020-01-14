"""
Bojan communication
"""
import serial                       # import pySerial
from serial.tools import list_ports
from time import sleep, perf_counter, time
from queue import Empty
from PyQt5.QtCore import QThread


class Communication:

    def __init__(self, RXqueue, TXqueue):
        self.TXqueue = TXqueue
        self.RXqueue = RXqueue

    def connect(self):
        pass

    def disconnect(self):
        pass

    def write(self, data):
        pass

    def read(self):
        return ""


class SerialCom(Communication, QThread):
    # Serial communicator commands
    SERIAL_COMMAND_SCAN = "SERIAL_COMMAND_SCAN"
    SERIAL_COMMAND_CONNECT = "SERIAL_COMMAND_CONNECT"
    SERIAL_COMMAND_DISCONNECT = "SERIAL_COMMAND_DISCONNECT"
    SERIAL_COMMAND_WRITE = "SERIAL_COMMAND_WRITE"
    SERIAL_COMMAND_READ = "SERIAL_COMMAND_READ"
    SERIAL_COMMAND_RESPONSE = "ACK"
    SERIAL_REPLY_TIMEOUT = 5.0
    SERIAL_READ_TIMEOUT = 5.0

    def __init__(self, RXqueue=None, TXqueue=None):
        # super().__init__() - call from base class
        super().__init__(RXqueue, TXqueue)

        self.ser = None
        self.__started = False

    def run(self):
        self.__started = True
        print('START')
        while self.__started:
            try:
                package = self.TXqueue.get(block=True, timeout=1.0)
                self.TXqueue.task_done()
                self._command_handler(package)
            except Empty:
                pass

    def _command_handler(self, package):
        # Split package
        print('c_h', package)
        command, data = package
        # Handle commands
        if command == SerialCom.SERIAL_COMMAND_SCAN:
            self.scan_ports()
            return
        elif command == SerialCom.SERIAL_COMMAND_CONNECT:
            self.serial_connect(data[0], data[1])
            return
        elif command == SerialCom.SERIAL_COMMAND_DISCONNECT:
            self.disconnect()
            return
        elif command == SerialCom.SERIAL_COMMAND_READ:
            self.read()
            return
        elif command == SerialCom.SERIAL_COMMAND_WRITE:
            self.write(data)
            return
        else:
            print('Invaild command!')

    def scan_ports(self):
        ports = list_ports.comports(include_links=False)
        package = (SerialCom.SERIAL_COMMAND_SCAN, [i.device for i in ports])
        self.RXqueue.put(package)

    def serial_connect(self, port, baudrate):
        if self.ser is not None:
            print('Serial connection already opened!')
            return

        super().connect()
        self.ser = serial.Serial(timeout=SerialCom.SERIAL_READ_TIMEOUT)
        self.ser.baudrate = baudrate
        self.ser.port = port
        self.ser.open()

    def disconnect(self):
        if self.ser is None:
            print('Serial connection already closed!')
            return

        self.ser.close()
        self.ser = None

    def write(self, data):
        # Append line termination
        data += '\r\n'
        # Write data
        self.ser.write(data.encode('utf-8'))
        print(data.encode('utf-8'))
        self.ser.flush()
        ack = self.read()
        print(ack)
        if ack == SerialCom.SERIAL_COMMAND_RESPONSE:
            return

    def close_thread(self):
        self.__started = False

    def read(self):                        #Serial send
        data = self.ser.readline()
        data = data.decode("utf-8")
        data = data[0:-1]
        return data


class CommThread(QThread):
    def __init__(self, rx_queue, tx_queue):
        super().__init__()
        self.comm = SerialCom(RXqueue=rx_queue, TXqueue=tx_queue)

    def run(self):
        self.comm.run()
