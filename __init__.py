"""
Bojan interface

NEMI - 2019
"""
import sys

from PyQt5.QtWidgets import *

from ui.joystick import Joystick
from ui.bojan import Ui_MainWindow
from connection.controls import BojanControls


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.joystick = Joystick()  # naredi joystick widget
        self.gridLayout_3.addWidget(self.joystick,3,1)


#   #   #   definicija funkcij tipk   #   #   #

#   #   #

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
