"""
Bojan interface

NEMI - 2019
"""
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

from ui.joystick import Joystick
from ui.bojan import Ui_MainWindow
from connection.controls import BojanControls

XINC = 1
YINC = 2
XDEC = 3
YDEC = 4


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        self.joystick = Joystick()  # naredi joystick widget
        self.gridLayout_3.addWidget(self.joystick, 3, 1)
        self.load_img_btn.clicked.connect(self.get_image)

    def get_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.txt)")
        file = fname[0]
        if len(file) != 0:
            read = open(file)
            self.gcodeDisplay.setText(read.read())
            self.fileName.setText(file)
        else:
            print('nothing to see here')

    def jog_mode(self, direction, velocity):
        pass

    def which_port(self, port):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def pause(self):
        pass

    def calibrate(self):
        pass

#   #   #    funkcije gumbov     #   #   #

        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.pause_btn.clicked.connect(self.pause)
        self.calibrate_btn.clicked.connect(self.calibrate)
        self.x_inc.pressed.connect(self.jog_mode(XINC, self.velocitySlider.value()))
        self.x_decr.pressed.connect(self.jog_mode(XDEC, self.velocitySlider.value()))
        self.y_inc.pressed.connect(self.jog_mode(YINC, self.velocitySlider.value()))
        self.y_decr.pressed.connect(self.jog_mode(YDEC, self.velocitySlider.value()))


def ui_main():
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec_())


def connection_main():
    pass


def main():
    """ Main function """
    connection_main()
    ui_main()


if __name__ == '__main__':
    main()
