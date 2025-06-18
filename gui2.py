from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def __init__(self):
        self.value = None
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("Add Your Word")
        self.MainWindow.resize(701, 375)
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
        self.label.setGeometry(QtCore.QRect(220, 40, 431, 61))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(170, 160, 381, 41))
        self.comboBox.setStyleSheet("background-color: rgb(109, 0, 55);\n"
                                    "alternate-background-color: rgb(77, 0, 39);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(260, 240, 201, 61))
        self.pushButton.setStyleSheet("background-color: rgb(112, 0, 0);\n"
                                        "alternate-background-color: rgb(106, 0, 53);")
        self.pushButton.setObjectName("pushButton")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.MainWindow.show()
        self.pushButton.clicked.connect(self.button_pushed)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Add Your Word"))
        self.label.setText(_translate("MainWindow", "What will you add ?"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Noun"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Adjective"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Adverb"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Verb"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Phrase"))
        self.pushButton.setText(_translate("MainWindow", "Continue"))

    def button_pushed(self):
        self.value = self.comboBox.currentText()
        self.MainWindow.close()

def get_values(ui):
    return ui.value

def main(ui):
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    #return app

