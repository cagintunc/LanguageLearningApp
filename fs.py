
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, text):
        self.MainWindow = MainWindow
        self.text = text
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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(320, 50, 331, 61))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(260, 170, 201, 61))
        self.pushButton.setStyleSheet("background-color: rgb(112, 0, 0);\n"
                                    "alternate-background-color: rgb(106, 0, 53);")
        self.pushButton.setObjectName("pushButton")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.MainWindow.show()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.pushButton.clicked.connect(self.clicked)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Result"))
        self.label.setText(_translate("MainWindow", self.text))
        self.pushButton.setText(_translate("MainWindow", "Close"))

    def clicked(self):
        self.MainWindow.close()


def main(ui, text):
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow, text)
