

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(733, 311)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 781, 571))
        self.frame.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                "font: 16pt \"MS Shell Dlg 2\";\n"
                                "color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(190, 30, 431, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(260, 180, 201, 61))
        self.pushButton.setStyleSheet("background-color: rgb(112, 0, 0);\n"
                                        "alternate-background-color: rgb(106, 0, 53);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 631, 51))
        self.label_2.setObjectName("label_2")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.MainWindow.show()
        self.pushButton.clicked.connect(self.pushed)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Notification"))
        self.label.setText(_translate("MainWindow", "Make sure that the string "))
        self.pushButton.setText(_translate("MainWindow", "Continue"))
        self.label_2.setText(_translate("MainWindow", "does not exceed 58 character number !"))

    def pushed(self):
        self.MainWindow.close()

def main(ui):
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)

