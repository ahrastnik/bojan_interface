from threading import Thread
from queue import Queue, Empty
from time import sleep

from connection.communication import SerialCom

class BojanControls:
    COMMAND_JOG = "J "
    COMMAND_WORK_MOVE = "G1"
    COMMAND_FAST_MOVE = "G0"

    def __init__(self):
        self.RX_queue = Queue()
        self.TX_queue = Queue()

        self.comm = SerialCom(RXqueue = self.RX_queue, TXqueue=self.TX_queue)

        comm_thread = Thread(name="Communication thread", target=self.comm.run)
        comm_thread.start()

    def read_RXqueue(self):
        # Read command from communication queue
        return self.RX_queue.get(block=False)


    def _send_command(self, command, data=None):
        # Make package
        package = (
            command,
            data
        )
        # Send command to communication queue
        self.TX_queue.put(package)

    def scan_ports(self):
        self._send_command(SerialCom.SERIAL_COMMAND_SCAN)

    def connect(self,port,baudrate):
        self._send_command(SerialCom.SERIAL_COMMAND_CONNECT, (port, baudrate))

    def disconnect(self):
        self._send_command(SerialCom.SERIAL_COMMAND_DISCONNECT)

    def load_gcode(self, gcode):
        for line in gcode:
            self._send_command(SerialCom.SERIAL_COMMAND_WRITE, line)

    def jog(self, dir, vel):
        x_dir = dir[0] * vel
        y_dir = dir[1] * vel

        X = "X" + str(x_dir)
        Y = "Y" + str(y_dir)

        gCode = self.COMMAND_JOG + X + " " + Y

        self._send_command(SerialCom.SERIAL_COMMAND_WRITE, gCode)

if __name__ == '__main__':
    controller = BojanControls()

    while True:
        try:
            controller.scan_ports()
            sleep(0.5)
            print(controller.read_RXqueue())
        except Empty:
            pass
        sleep(1)

