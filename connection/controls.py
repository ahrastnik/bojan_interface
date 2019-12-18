from threading import Thread
from queue import Queue, Empty
from time import sleep

from connection.communication import SerialCom

class BojanControls:
    COMMAND_FAST_MOVE = 'G00'
    COMMAND_WORK_MOVE = 'G01'
    COMMAND_ABS_POS = 'G91'
    COMMAND_INC_POS = 'G90'
    COMMAND_STOP = 'M112'
    COMMAND_LIST = (
        COMMAND_FAST_MOVE,
        COMMAND_WORK_MOVE,
        COMMAND_ABS_POS,
        COMMAND_INC_POS,
        COMMAND_STOP)

    def __init__(self):
        self.RX_queue = Queue()
        self.TX_queue = Queue()

        self.comm = SerialCom(RXqueue = self.RX_queue, TXqueue=self.TX_queue)

        self.comm_thread = Thread(name="Communication thread", target=self.comm.run)
        self.comm_thread.start()

    def read_RXqueue(self):
        # Read command from communication queue
        return self.RX_queue.get(block=False)


    def emergency_stop(self):
        self._send_command(SerialCom.SERIAL_COMMAND_WRITE, BojanControls.COMMAND_STOP)

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

    def close(self):
        self.comm.close_thread()
        #self.comm_thread.join()

    def jog(self, dir, vel):
        if dir == "right":
            pass
        elif dir == "left":
            pass
        elif dir == "up":
            pass
        elif dir == "down":
            pass


        #gCode = "%s %s" % (self.COMMAND_WORK_MOVE, vel)

        #self._send_command(SerialCom.SERIAL_COMMAND_WRITE, gCode)

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

