from threading import Thread, Lock
from PyQt5.QtCore import QThread
from queue import Queue, Empty
from time import sleep

from connection.communication import SerialCom,CommThread


class BojanControls:
    COMMAND_FAST_MOVE = 'G00'
    COMMAND_WORK_MOVE = 'G01'
    COMMAND_ABS_POS = 'G91'
    COMMAND_INC_POS = 'G90'
    COMMAND_STOP = 'M112'
    COMMAND_PAUSE = 'M226'
    COMMAND_JOG = 'J69'

    COMMAND_LIST = (
        COMMAND_FAST_MOVE,
        COMMAND_WORK_MOVE,
        COMMAND_ABS_POS,
        COMMAND_INC_POS,
        COMMAND_STOP,
        COMMAND_PAUSE,
        COMMAND_JOG
    )

    def __init__(self):
        self.RX_queue = Queue()
        self.TX_queue = Queue()

        self.comm_thread = CommThread(self.RX_queue, self.TX_queue)
        self.comm_thread.start()

    def read_RXqueue(self):
        # Read command from communication queue
        try:
            if self.RX_queue is None:
                return None
            data = self.RX_queue.get_nowait()
            self.RX_queue.task_done()
            # print(data)
            return data
        except Empty:
            return None

    def read_all(self):
        while True:
            try:
                self.TX_queue.get_nowait()
            except Empty:
                return

    def pause(self):
        self._send_command(SerialCom.SERIAL_COMMAND_WRITE, BojanControls.COMMAND_PAUSE)

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
        for i, line in enumerate(gcode):
            self._send_command(SerialCom.SERIAL_COMMAND_GCODE_RESPONSE, (line, i))

    def close(self):
        self.comm_thread.comm.close_thread()
        # self.comm_thread.join()

    def jog(self, direction, vel):
        if direction == "right":
            g_code = "%s %s%s" % (self.COMMAND_JOG, 'X', str(vel))
        elif direction == "left":
            g_code = "%s %s%s" % (self.COMMAND_JOG, 'X-', str(vel))
        elif direction == "up":
            g_code = "%s %s%s" % (self.COMMAND_JOG, 'Y', str(vel))
        elif direction == "down":
            g_code = "%s %s%s" % (self.COMMAND_JOG, 'Y-', str(vel))
        elif direction == "":
            g_code = "%s" % self.COMMAND_JOG
        else:
            g_code = "%s %s" % (self.COMMAND_JOG, direction)
        print(g_code)

        self._send_command(SerialCom.SERIAL_COMMAND_WRITE, g_code)


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

