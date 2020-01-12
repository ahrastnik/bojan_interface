"""
Bojan interface

NEMI - 2019
"""
from PyQt5.QtCore import QTimer, QThread, QCoreApplication
from PyQt5.QtWidgets import *

from connection.communication import SerialCom
from connection.controls import BojanControls
import sys
import time


from ui.joystick import Joystick
from ui.bojan import Ui_MainWindow

XINC = "right"
YINC = "up"
XDEC = "left"
YDEC = "down"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)                          #naredi joystick widget
        self.controls = BojanControls()
        self.joystick = Joystick(self.controls)
        self.gridLayout_3.addWidget(self.joystick, 3, 1)
        QAction("Quit",self).triggered.connect(lambda: self.close_event())
        self.gcode = []
        self.port = ['COM1','COM2','COM3']
        self.progressBar.hide()
        self.pause = True #for pause button
        self.hitrost = self.velocitySlider.value()
        self.velocitySlider.sliderReleased.connect(lambda: self.value_change())
        self.controls.connect('COM9', 115200)
        self.jogTimer = QTimer()
#   #   #       funkcije tipk       #    #    #
        self.load_img_btn.clicked.connect(self.get_image)
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.pause_btn.clicked.connect(self.set_pause)
        self.risi_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.nazaj_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.x_inc.pressed.connect(lambda: self.jog_mode(XINC, self.hitrost))       #lambda start=false
        self.x_decr.pressed.connect(lambda: self.jog_mode(XDEC, self.hitrost))
        self.y_inc.pressed.connect(lambda: self.jog_mode(YINC, self.hitrost))
        self.y_decr.pressed.connect(lambda: self.jog_mode(YDEC, self.hitrost))
        self.x_inc.released.connect(lambda: self.jog_mode_release())
        self.x_decr.released.connect(lambda: self.jog_mode_release())
        self.y_inc.released.connect(lambda: self.jog_mode_release())
        self.y_decr.released.connect(lambda: self.jog_mode_release())

        timer = QTimer(self)
        timer.timeout.connect(self._command_handler)
        timer.start(1000)

    def value_change(self):
        self.hitrost = self.velocitySlider.value()

    def check_gcode(self, line):
        line = line.split(' ')
        if len(line) > 0:
            if line[0] in BojanControls.COMMAND_LIST:
                return self.command_handler(line)
        return False

    def fix_termination(self, x):
        return x[:-1]

    def command_handler(self, x):
        if x[0] == BojanControls.COMMAND_FAST_MOVE:
            return True
        elif x[0] == BojanControls.COMMAND_WORK_MOVE:
            return True
        elif x[0] == BojanControls.COMMAND_ABS_POS:
            return True
        elif x[0] == BojanControls.COMMAND_INC_POS:
            return True
        else:
            return False

    def get_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Image files (*.ngc)")
        file = fname[0]

        if len(file) != 0:
            read = open(file)
            self.gcodeDisplay.setText(read.read())
            self.fileName.setText(file)
            for x in open(file):
                x = self.fix_termination(x)
                if self.check_gcode(x):
                    print(x)
                    self.gcode.append(x)
        else:
            print('nothing to see here')

    def jog_mode(self, direction, vel):
        self.controls.jog(direction, vel)

    def jog_mode_release(self):
        self.controls.jog('', '')

    def close_event(self):
        self.controls.disconnect()

    def start(self):
        self.progressBar.show()
        self.controls.load_gcode(self.gcode)

    def stop(self):
        self.controls.emergency_stop()

    def set_pause(self):
        self.controls.pause()

    def ports(self):
        self.port_btn.addItems(self.port)

    def _command_handler(self):
        # Split package
        return
        command, data = self.controls.read_RXqueue()

        # Handle commands
        if command == SerialCom.SERIAL_COMMAND_SCAN:
            return
        elif command == SerialCom.SERIAL_COMMAND_CONNECT:
            return
        elif command == SerialCom.SERIAL_COMMAND_DISCONNECT:
            return
        elif command == SerialCom.SERIAL_COMMAND_READ:
            return
        elif command == SerialCom.SERIAL_COMMAND_WRITE:
            return
        else:
            print('Invaild command!')

#   #   #    funkcije gumbov     #   #   #


def ui_main():
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec_())


def connection_main():
    pass


def main():
    """ Main function """
    ui_main()
    connection_main()


if __name__ == '__main__':
    main()

