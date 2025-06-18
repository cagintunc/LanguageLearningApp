
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):

    def __init__(self, name):
        self.name = name.lower()
        self.result = {"word": "", "meaning": "", "preposition": "",
                        "is_gerund": "", "pronounce": ""}

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        if self.name.lower() == "adjective":
            self.MainWindow.resize(701, 800)
            self.centralwidget = QtWidgets.QWidget(self.MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.frame = QtWidgets.QFrame(self.centralwidget)
            self.frame.setGeometry(QtCore.QRect(-1, -1, 900, 1261))
            self.frame.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                     "font: 16pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255, 255, 255);")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.pushButton = QtWidgets.QPushButton(self.frame)
            self.pushButton.setGeometry(QtCore.QRect(260, 700, 201, 61))
            self.pushButton.setStyleSheet("background-color: rgb(112, 0, 0);\n"
                                          "alternate-background-color: rgb(106, 0, 53);")
            self.pushButton.setObjectName("pushButton")
            self.lineEdit = QtWidgets.QLineEdit(self.frame)
            self.lineEdit.setGeometry(QtCore.QRect(70, 120, 571, 61))
            self.lineEdit.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit.setObjectName("lineEdit")
            self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
            self.lineEdit_2.setGeometry(QtCore.QRect(70, 280, 571, 61))
            self.lineEdit_2.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit_2.setObjectName("lineEdit_2")
            self.label_2 = QtWidgets.QLabel(self.frame)
            self.label_2.setGeometry(QtCore.QRect(70, 30, 381, 61))
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.frame)
            self.label_3.setGeometry(QtCore.QRect(70, 200, 381, 61))
            self.label_3.setObjectName("label_3")

            self.label_4 = QtWidgets.QLabel(self.frame)
            self.label_4.setGeometry(QtCore.QRect(70, 350, 381, 61))
            self.label_4.setObjectName("label_4")
            self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
            self.lineEdit_3.setGeometry(QtCore.QRect(70, 440, 571, 61))
            self.lineEdit_3.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit_3.setObjectName("lineEdit_3")

            self.label_6 = QtWidgets.QLabel(self.frame)
            self.label_6.setGeometry(QtCore.QRect(70, 500, 381, 61))
            self.label_6.setObjectName("label_6")
            self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
            self.lineEdit_5.setGeometry(QtCore.QRect(70, 600, 571, 61))
            self.lineEdit_5.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit_5.setObjectName("lineEdit_5")


        elif self.name == "verb":
            self.MainWindow.resize(701, 900)
            self.centralwidget = QtWidgets.QWidget(self.MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.frame = QtWidgets.QFrame(self.centralwidget)
            self.frame.setGeometry(QtCore.QRect(-1, -1, 950, 1261))
            self.frame.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                     "font: 16pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255, 255, 255);")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.pushButton = QtWidgets.QPushButton(self.frame)
            self.pushButton.setGeometry(QtCore.QRect(260, 800, 201, 61))
            self.pushButton.setStyleSheet("background-color: rgb(112, 0, 0);\n"
                                          "alternate-background-color: rgb(106, 0, 53);")
            self.pushButton.setObjectName("pushButton")
            self.lineEdit = QtWidgets.QLineEdit(self.frame)
            self.lineEdit.setGeometry(QtCore.QRect(70, 120, 571, 61))
            self.lineEdit.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit.setObjectName("lineEdit")
            self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
            self.lineEdit_2.setGeometry(QtCore.QRect(70, 280, 571, 61))
            self.lineEdit_2.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit_2.setObjectName("lineEdit_2")
            self.label_2 = QtWidgets.QLabel(self.frame)
            self.label_2.setGeometry(QtCore.QRect(70, 30, 381, 61))
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.frame)
            self.label_3.setGeometry(QtCore.QRect(70, 200, 381, 61))
            self.label_3.setObjectName("label_3")

            self.label_4 = QtWidgets.QLabel(self.frame)
            self.label_4.setGeometry(QtCore.QRect(70, 350, 381, 61))
            self.label_4.setObjectName("label_4")
            self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
            self.lineEdit_3.setGeometry(QtCore.QRect(70, 440, 571, 61))
            self.lineEdit_3.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit_3.setObjectName("lineEdit_3")

            self.label_5 = QtWidgets.QLabel(self.frame)
            self.label_5.setGeometry(QtCore.QRect(70, 500, 381, 61))
            self.label_5.setObjectName("label_5")
            self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
            self.lineEdit_4.setGeometry(QtCore.QRect(70, 590, 571, 61))
            self.lineEdit_4.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit_4.setObjectName("lineEdit_4")

            self.label_6 = QtWidgets.QLabel(self.frame)
            self.label_6.setGeometry(QtCore.QRect(70, 660, 381, 61))
            self.label_6.setObjectName("label_6")
            self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
            self.lineEdit_5.setGeometry(QtCore.QRect(70, 740, 571, 61))
            self.lineEdit_5.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit_5.setObjectName("lineEdit_5")


        else:
            self.MainWindow.resize(701, 650)
            self.centralwidget = QtWidgets.QWidget(self.MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.frame = QtWidgets.QFrame(self.centralwidget)
            self.frame.setGeometry(QtCore.QRect(-1, -1, 950, 1261))
            self.frame.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                     "font: 16pt \"MS Shell Dlg 2\";\n"
                                     "color: rgb(255, 255, 255);")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.pushButton = QtWidgets.QPushButton(self.frame)
            self.pushButton.setGeometry(QtCore.QRect(260, 540, 201, 61))
            self.pushButton.setStyleSheet("background-color: rgb(112, 0, 0);\n"
                                          "alternate-background-color: rgb(106, 0, 53);")
            self.pushButton.setObjectName("pushButton")
            self.lineEdit = QtWidgets.QLineEdit(self.frame)
            self.lineEdit.setGeometry(QtCore.QRect(70, 120, 571, 61))
            self.lineEdit.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit.setObjectName("lineEdit")
            self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
            self.lineEdit_2.setGeometry(QtCore.QRect(70, 280, 571, 61))
            self.lineEdit_2.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit_2.setObjectName("lineEdit_2")
            self.label_2 = QtWidgets.QLabel(self.frame)
            self.label_2.setGeometry(QtCore.QRect(70, 30, 381, 61))
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.frame)
            self.label_3.setGeometry(QtCore.QRect(70, 200, 381, 61))
            self.label_3.setObjectName("label_3")


            self.label_6 = QtWidgets.QLabel(self.frame)
            self.label_6.setGeometry(QtCore.QRect(70, 370, 381, 61))
            self.label_6.setObjectName("label_6")
            self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
            self.lineEdit_5.setGeometry(QtCore.QRect(70, 450, 571, 61))
            self.lineEdit_5.setStyleSheet("background-color: rgb(97, 0, 49);")
            self.lineEdit_5.setObjectName("lineEdit_5")


        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.MainWindow.show()
        self.pushButton.clicked.connect(self.button_clicked)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Bilgiler"))
        self.pushButton.setText(_translate("MainWindow", "Continue"))
        self.label_2.setText(_translate("MainWindow", "Kelime"))
        self.label_3.setText(_translate("MainWindow", "Anlami"))
        self.label_6.setText(_translate("MainWindow", "Okunus"))
        if self.name == "adjective":
            self.label_4.setText(_translate("MainWindow", "Preposition"))
        elif self.name == "verb":
            self.label_4.setText(_translate("MainWindow", "Preposition"))
            self.label_5.setText(_translate("MainWindow", "Gerund mu ?"))

    def button_clicked(self):
        v1 = self.lineEdit.text()
        v2 = self.lineEdit_2.text()
        v5 = self.lineEdit_5.text()
        v3, v4 = "", ""
        if self.name == "adjective":
            v3 = self.lineEdit_3.text()
        elif self.name == "verb":
            v3 = self.lineEdit_3.text()
            v4 = self.lineEdit_4.text()
        self.result["word"] = v1
        self.result["meaning"] = v2
        self.result["preposition"] = v3
        self.result["is_gerund"] = v4
        self.result["pronounce"] = v5
        self.MainWindow.close()


def get_values(ui):
    return ui.result

def main(ui):
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)


