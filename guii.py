from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 781, 1600))
        self.frame.setStyleSheet("background-color: rgb(85, 85, 127);\n"
        "font: 16pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 40, 381, 61))
        # x, y, x_width, y_width
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(260, 800, 201, 61))
        self.pushButton.setStyleSheet("background-color: rgb(112, 0, 0);\n"
        "alternate-background-color: rgb(106, 0, 53);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit.setStyleSheet("background-color: rgb(97, 0, 49);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 380, 571, 61))
        self.lineEdit_2.setStyleSheet("background-color: rgb(97, 0, 49);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 130, 381, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 290, 381, 61))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 450, 381, 61))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 540, 571, 61))
        self.lineEdit_3.setStyleSheet("background-color: rgb(97, 0, 49);")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(70, 610, 381, 61))
        self.label_5.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 700, 571, 61))
        self.lineEdit_4.setStyleSheet("background-color: rgb(97, 0, 49);")
        self.lineEdit_4.setObjectName("lineEdit_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Gerekli Yerleri Doldurun"))
        self.pushButton.setText(_translate("MainWindow", "Continue"))
        self.label_2.setText(_translate("MainWindow", "Kelime"))
        self.label_3.setText(_translate("MainWindow", "Anlamı"))
        self.label_4.setText(_translate("MainWindow", "kkskksk"))
        self.label_5.setText(_translate("MainWindow", "5555"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
