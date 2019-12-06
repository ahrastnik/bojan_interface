# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bojan.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 863)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bojan_kral.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background:#aaa;")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(0, -10, 491, 391))
        self.frame.setStyleSheet("background-color:#5CA2F1;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 11, 461, 371))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stop_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.stop_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.stop_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.stop_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        self.stop_btn.setFont(font)
        self.stop_btn.setStyleSheet("background-color: white;\n"
"color: rgb(69, 124, 182);\n"
"color: black;\n"
"border: 2px solid #457cb6;\n"
"border-radius:7%;")
        self.stop_btn.setObjectName("stop_btn")
        self.gridLayout_3.addWidget(self.stop_btn, 2, 3, 1, 1)
        self.risi_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.risi_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.risi_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        self.risi_btn.setFont(font)
        self.risi_btn.setStyleSheet("background-color: white;\n"
"color: rgb(69, 124, 182);\n"
"color: black;\n"
"border: 2px solid #457cb6;\n"
"border-radius:7%;")
        self.risi_btn.setObjectName("risi_btn")
        self.gridLayout_3.addWidget(self.risi_btn, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.y_inc = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_inc.sizePolicy().hasHeightForWidth())
        self.y_inc.setSizePolicy(sizePolicy)
        self.y_inc.setMinimumSize(QtCore.QSize(50, 50))
        self.y_inc.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        self.y_inc.setFont(font)
        self.y_inc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.y_inc.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.y_inc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.y_inc.setStyleSheet("image: url(C:/Users/jakak/Desktop/Jaka/Šola/4.letnik/NEMI/bojan_interface/ui/img/puscica_gor.png);\n"
"background-color:white;\n"
"border-radius:25px;\n"
"\n"
"")
        self.y_inc.setText("")
        self.y_inc.setObjectName("y_inc")
        self.gridLayout_3.addWidget(self.y_inc, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 4, 1, 1, 1)
        self.pause_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pause_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.pause_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.pause_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        self.pause_btn.setFont(font)
        self.pause_btn.setStyleSheet("background-color: white;\n"
"color: rgb(69, 124, 182);\n"
"color: black;\n"
"border: 2px solid #457cb6;\n"
"border-radius:7%;")
        self.pause_btn.setObjectName("pause_btn")
        self.gridLayout_3.addWidget(self.pause_btn, 3, 3, 1, 1)
        self.x_inc = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.x_inc.setMinimumSize(QtCore.QSize(50, 50))
        self.x_inc.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        self.x_inc.setFont(font)
        self.x_inc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.x_inc.setStyleSheet("image: url(C:/Users/jakak/Desktop/Jaka/Šola/4.letnik/NEMI/bojan_interface/ui/img/puscica_desno.png);\n"
"background-color:white;\n"
"border-radius:25px;")
        self.x_inc.setText("")
        self.x_inc.setObjectName("x_inc")
        self.gridLayout_3.addWidget(self.x_inc, 3, 2, 1, 1)
        self.y_decr = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.y_decr.setMinimumSize(QtCore.QSize(50, 50))
        self.y_decr.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        self.y_decr.setFont(font)
        self.y_decr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.y_decr.setStyleSheet("image: url(C:/Users/jakak/Desktop/Jaka/Šola/4.letnik/NEMI/bojan_interface/ui/img/puscica_dol.png);\n"
"background-color:white;\n"
"border-radius:25px;")
        self.y_decr.setText("")
        self.y_decr.setObjectName("y_decr")
        self.gridLayout_3.addWidget(self.y_decr, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.calibrate_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.calibrate_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.calibrate_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.calibrate_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        self.calibrate_btn.setFont(font)
        self.calibrate_btn.setStyleSheet("background-color: white;\n"
"color: rgb(69, 124, 182);\n"
"color: black;\n"
"border: 2px solid #457cb6;\n"
"border-radius:7%;")
        self.calibrate_btn.setObjectName("calibrate_btn")
        self.gridLayout_3.addWidget(self.calibrate_btn, 5, 3, 1, 1)
        self.x_decr = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.x_decr.setMinimumSize(QtCore.QSize(50, 50))
        self.x_decr.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        self.x_decr.setFont(font)
        self.x_decr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.x_decr.setStyleSheet("image: url(C:/Users/jakak/Desktop/Jaka/Šola/4.letnik/NEMI/bojan_interface/ui/img/puscica_levo.png);\n"
"background-color:white;\n"
"border-radius:25px;")
        self.x_decr.setText("")
        self.x_decr.setObjectName("x_decr")
        self.gridLayout_3.addWidget(self.x_decr, 3, 0, 1, 1)
        self.start_btn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.start_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.start_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.start_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet("background-color: white;\n"
"color: rgb(69, 124, 182);\n"
"color: black;\n"
"border: 2px solid #457cb6;\n"
"border-radius:7%;")
        self.start_btn.setObjectName("start_btn")
        self.gridLayout_3.addWidget(self.start_btn, 1, 3, 1, 1)
        self.velocitySlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.velocitySlider.setOrientation(QtCore.Qt.Vertical)
        self.velocitySlider.setObjectName("velocitySlider")
        self.gridLayout_3.addWidget(self.velocitySlider, 1, 4, 5, 1)
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setGeometry(QtCore.QRect(510, 0, 491, 381))
        self.frame_3.setStyleSheet("background-color:#5CA2F1;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(350, 10, 131, 121))
        self.label_2.setStyleSheet("border:2px solid #457cb6;\n"
"border-image: url(C:/Users/jakak/Desktop/Jaka/Šola/4.letnik/NEMI/bojan_interface/ui/img/bojan_kral.jpg);\n"
"\n"
"")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 140, 461, 231))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:")
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 4, 0, 1, 1)
        self.x_poz = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.x_poz.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.x_poz.setFont(font)
        self.x_poz.setStyleSheet("background-color:white;\n"
"border:2px solid #457cb6;\n"
"color: black;\n"
"font: 8pt \"Luckiest Guy\";")
        self.x_poz.setFrameShape(QtWidgets.QFrame.Box)
        self.x_poz.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.x_poz.setLineWidth(1)
        self.x_poz.setMidLineWidth(1)
        self.x_poz.setText("")
        self.x_poz.setObjectName("x_poz")
        self.gridLayout_4.addWidget(self.x_poz, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:")
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.z_poz = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.z_poz.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.z_poz.setFont(font)
        self.z_poz.setStyleSheet("background-color:white;\n"
"border:2px solid #457cb6;\n"
"color: black;\n"
"font: 8pt \"Luckiest Guy\";")
        self.z_poz.setFrameShape(QtWidgets.QFrame.Box)
        self.z_poz.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.z_poz.setLineWidth(1)
        self.z_poz.setMidLineWidth(1)
        self.z_poz.setText("")
        self.z_poz.setObjectName("z_poz")
        self.gridLayout_4.addWidget(self.z_poz, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:")
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 1)
        self.y_poz = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.y_poz.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.y_poz.setFont(font)
        self.y_poz.setStyleSheet("background-color:white;\n"
"border:2px solid #457cb6;\n"
"color: black;\n"
"font: 8pt \"Luckiest Guy\";")
        self.y_poz.setFrameShape(QtWidgets.QFrame.Box)
        self.y_poz.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.y_poz.setLineWidth(1)
        self.y_poz.setMidLineWidth(1)
        self.y_poz.setText("")
        self.y_poz.setObjectName("y_poz")
        self.gridLayout_4.addWidget(self.y_poz, 3, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 9, 321, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.load_img_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.load_img_btn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        self.load_img_btn.setFont(font)
        self.load_img_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.load_img_btn.setStyleSheet("background-color: white;\n"
"color: rgb(69, 124, 182);\n"
"color: black;\n"
"border: 2px solid #457cb6;\n"
"border-radius:7%;\n"
"")
        self.load_img_btn.setFlat(False)
        self.load_img_btn.setObjectName("load_img_btn")
        self.verticalLayout.addWidget(self.load_img_btn)
        self.fileName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.fileName.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.fileName.setFont(font)
        self.fileName.setStyleSheet("background-color:white;\n"
"border:2px solid #457cb6;\n"
"color: black;\n"
"font: 8pt \"Luckiest Guy\";")
        self.fileName.setFrameShape(QtWidgets.QFrame.Box)
        self.fileName.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fileName.setLineWidth(1)
        self.fileName.setMidLineWidth(1)
        self.fileName.setObjectName("fileName")
        self.verticalLayout.addWidget(self.fileName)
        self.frame_4 = QtWidgets.QFrame(self.page)
        self.frame_4.setGeometry(QtCore.QRect(0, 400, 491, 401))
        self.frame_4.setStyleSheet("background-color:#5CA2F1;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 440, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.gcodeDisplay = QtWidgets.QTextBrowser(self.frame_4)
        self.gcodeDisplay.setGeometry(QtCore.QRect(25, 31, 441, 351))
        self.gcodeDisplay.setStyleSheet("background-color:#000000;\n"
"color:#f0f0f0;")
        self.gcodeDisplay.setObjectName("gcodeDisplay")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(510, 400, 495, 401))
        self.frame_2.setStyleSheet("background-color:#5CA2F1;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.predogled = QtWidgets.QGraphicsView(self.frame_2)
        self.predogled.setGeometry(QtCore.QRect(30, 30, 431, 351))
        self.predogled.setStyleSheet("background-color:#ffffff;")
        self.predogled.setObjectName("predogled")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 440, 26))
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.page_2)
        self.widget.setStyleSheet("background-color:#5CA2F1;")
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.widget)
        self.frame_5.setStyleSheet("background-color:white;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5.addWidget(self.frame_5, 0, 0, 1, 1)
        self.nazaj_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(12)
        self.nazaj_btn.setFont(font)
        self.nazaj_btn.setStyleSheet("background-color: white;\n"
"color: rgb(69, 124, 182);\n"
"color: black;\n"
"border: 2px solid #457cb6;\n"
"border-radius:7%;")
        self.nazaj_btn.setObjectName("nazaj_btn")
        self.gridLayout_5.addWidget(self.nazaj_btn, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1028, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bojan"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.risi_btn.setText(_translate("MainWindow", "rIŠI"))
        self.label.setText(_translate("MainWindow", "JOG"))
        self.pause_btn.setText(_translate("MainWindow", "Pavza"))
        self.calibrate_btn.setText(_translate("MainWindow", "Kalibriraj"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.label_7.setText(_translate("MainWindow", "TRENUTNA POZICIJA Z"))
        self.label_3.setText(_translate("MainWindow", "TRENUTNA POZICIJA X"))
        self.label_5.setText(_translate("MainWindow", "TRENUTNA POZICIJA Y"))
        self.load_img_btn.setText(_translate("MainWindow", "Naloži datoteko"))
        self.fileName.setText(_translate("MainWindow", "Ime datoteke"))
        self.label_4.setText(_translate("MainWindow", "    Ukazi (GCODE)"))
        self.label_6.setText(_translate("MainWindow", "     Predogled"))
        self.nazaj_btn.setText(_translate("MainWindow", "Nazaj"))
