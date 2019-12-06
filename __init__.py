"""
Bojan interface

NEMI - 2019
"""
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *

import sys

from ui.joystick import Joystick
from ui.bojan import Ui_MainWindow

XINC = 1
YINC = 2
XDEC = 3
YDEC = 4
COMMAND_G00 = 'G00'
COMMAND_G01 = 'G01'
COMMAND_G91 = 'G91'
COMMAND_G90 = 'G90'
COMMAND_LIST = (
    COMMAND_G00,
    COMMAND_G01,
    COMMAND_G90,
    COMMAND_G91)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.joystick = Joystick()                              #naredi joystick widget
        self.gridLayout_3.addWidget(self.joystick, 3, 1)

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
        self.x_inc.clicked.connect(lambda: self.jog_mode(XINC))
        self.x_decr.pressed.connect(lambda: self.jog_mode(XDEC))
        self.y_inc.pressed.connect(lambda: self.jog_mode(YINC))
        self.y_decr.pressed.connect(lambda: self.jog_mode(YDEC))

    def split_gcode(self, line):
        x = line.split(' ')
        if len(x) > 0:
            if x[0] in COMMAND_LIST:
                self.command_handler(x)
                print(x)

    def command_handler(self, x):
        if x[0] == COMMAND_G00:
            return
        elif x[0]  == COMMAND_G01:
            return
        elif x[0]  == COMMAND_G90:
            return
        elif x[0] == COMMAND_G91:
            return
        else:
            print('ni pravilna komanda')

    def get_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Image files (*.ngc)")
        file =  fname[0]
        gcode = []

        if len(file) != 0:
            read = open(file)
            self.gcodeDisplay.setText(read.read())
            self.fileName.setText(file)
            for x in open(file):
                self.split_gcode(x)
        else:
            print('nothing to see here')
        for j in range(len(gcode)):
            self.split_gcode(gcode)

    def jog_mode(self, direction, velocity):
        pass

        '''print('You didn\'t click anything.')
        open(file).close()
        print(gcode)'''

    def which_port(self, port):
        pass

    def start(self):
        print('start')

    def stop(self):
        print('stop')

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

