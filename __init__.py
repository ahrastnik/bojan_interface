"""
Bojan interface

NEMI - 2019
"""
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *

from connection.communication import Communication
from connection.controls import BojanControls
import sys

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
        self.stackedWidget.setCurrentIndex(0)
        self.joystick = Joystick()                              #naredi joystick widget
        self.gridLayout_3.addWidget(self.joystick, 3, 1)
        self.controls = BojanControls()
        self.gcode = []
#   #   #   definicija spremenljivk #    #    #

        #   #   #   slider   #   #   #



#   #   #       funkcije tipk       #    #    #
        self.load_img_btn.clicked.connect(self.get_image)
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.pause_btn.clicked.connect(self.pause)
        self.calibrate_btn.clicked.connect(self.calibrate)
        self.risi_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.nazaj_btn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.x_inc.pressed.connect(lambda: self.jog_mode(XINC))
        self.x_decr.pressed.connect(lambda: self.jog_mode(XDEC))
        self.y_inc.pressed.connect(lambda: self.jog_mode(YINC))
        self.y_decr.pressed.connect(lambda: self.jog_mode(YDEC))

        timer = QTimer(self)
        timer.timeout.connect(lambda: print('sekunda'))
        timer.start(1000)



    def check_gcode(self, line):
        x = line.split(' ')
        if len(x) > 0:
            if x[0] in BojanControls.COMMAND_LIST:
                return self.command_handler(x)
        return False

    def fix_termination(self,x):
        return x[:-1] + '\r\n'

    def command_handler(self, x):
        if x[0] == BojanControls.COMMAND_FAST_MOVE:
            return True
        elif x[0]  == BojanControls.COMMAND_WORK_MOVE:
            return  True
        elif x[0]  == BojanControls.COMMAND_ABS_POS:
            return  True
        elif x[0] == BojanControls.COMMAND_INC_POS:
            return True
        else:
            return False

    def get_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Image files (*.ngc)")
        file =  fname[0]

        if len(file) != 0:
            read = open(file)
            self.gcodeDisplay.setText(read.read())
            self.fileName.setText(file)
            for x in open(file):
                if self.check_gcode(x):
                    self.gcode.append(self.fix_termination(x))
            #self.controls.load_gcode(gcode)
        else:
            print('nothing to see here')

    def jog_mode(self, direction, velocity):
        pass#BojanControls.jog(direction, velocity)


    def which_port(self, port):
        pass

    def start(self):
        self.controls.load_gcode(self.gcode)

    def stop(self):
        self.controls.emergency_stop()

    def pause(self):
        print('pause')

    def calibrate(self):
        print('calibrate')

    def vodenje(self):
        print('vodenje')
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

