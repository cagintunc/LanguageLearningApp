
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.result = 0
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(701, 283)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 781, 1261))
        self.frame.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                    "font: 16pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 100, 211, 71))
        self.pushButton.setStyleSheet("background-color: rgb(112, 0, 0);\n"
                                        "alternate-background-color: rgb(106, 0, 53);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 100, 211, 71))
        self.pushButton_2.setStyleSheet("background-color: rgb(112, 0, 0);\n"
                                        "alternate-background-color: rgb(106, 0, 53);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.MainWindow.show()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.pushButton.clicked.connect(self.continuee)
        self.pushButton_2.clicked.connect(self.exitt)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Continue"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))

    def continuee(self):
        self.MainWindow.close()

    def exitt(self):
        self.result = 1
        self.MainWindow.close()


def main(ui):
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)


