"""
Bojan interface

NEMI - 2019
"""
from PyQt5.QtWidgets import *

import sys

from ui.joystick import Joystick
from ui.bojan import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.joystick = Joystick()                              #naredi joystick widget
        self.gridLayout_3.addWidget(self.joystick,3,1)


#   #   #   definicija funkcij tipk   #   #   #

#   #   #

def ui_main():
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec_())

def main():
    """ Main function """
    ui_main()


if __name__ == '__main__':
    main()

