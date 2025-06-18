

from PyQt5 import QtCore, QtGui, QtWidgets

style = """QPushButton {
    background-color: rgb(85, 85, 127);\n
    font: 16pt \"MS Shell Dlg 2\";\n
    color: rgb(255, 255, 255);\n
    transition-duration: 0.4s;\n
    border-radius: 16px;
    margin:0;
}
QPushButton::hover {background-color: rgb(50, 60, 50)}"""

style_label = "QLabel { font: 16pt \"MS Shell Dlg 2\";\n" \
              "color: rgb(255, 255, 255);\n" \
              "max-height: 120px;" \
              "min-height: 35px;}"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.value = -1
        self.MainWindow = MainWindow
        self.layout = QtWidgets.QGridLayout()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(788, 773)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(60, 2, 80);")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)

        self.frame.setGeometry(QtCore.QRect(-1, -1, 591, 571))
        self.frame.setStyleSheet("background-color: rgb(20, 200, 30);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 591, 571))
        self.frame_2.setStyleSheet("background-color: rgb(80, 2, 110);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame2")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label.setObjectName("label")
        self.label.setStyleSheet(style_label)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 331, 71))
        self.pushButton.setStyleSheet(style)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 370, 331, 71))
        self.pushButton_2.setStyleSheet(style)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 290, 331, 71))
        self.pushButton_4.setStyleSheet(style)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 290, 331, 71))
        self.pushButton_5.setStyleSheet(style)
        self.pushButton_5.setObjectName("pushButton_5")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        layout_2 = QtWidgets.QVBoxLayout()
        layout_2.addWidget(self.pushButton)
        layout_2.addWidget(self.pushButton_2)
        layout_2.addWidget(self.pushButton_4)
        layout_2.addWidget(self.pushButton_5)

        layout_2.setContentsMargins(120, 40, 120, 20)

        self.layout.addWidget(self.label)
        self.layout.addLayout(layout_2, 2, 0)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.centralwidget.setLayout(self.layout)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.MainWindow.show()
        self.pushButton.clicked.connect(self.add_words)
        self.pushButton_2.clicked.connect(self.game_1)
        self.pushButton_4.clicked.connect(self.game_2)
        self.pushButton_5.clicked.connect(self.exiit)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Learning a new language"))
        self.label.setText(_translate("MainWindow", "Select Proper Action"))
        self.pushButton.setText(_translate("MainWindow", "Add Word"))
        self.pushButton_2.setText(_translate("MainWindow", "Game 1"))
        self.pushButton_4.setText(_translate("MainWindow", "Game 2"))
        self.pushButton_5.setText(_translate("MainWindow", "Exit"))

    def add_words(self):
        self.value = 1
        self.MainWindow.close()

    def game_1(self):
        self.value = 3
        self.MainWindow.close()

    def simulation(self):
        self.value = 4
        self.MainWindow.close()

    def game_2(self):
        self.value = 2
        self.MainWindow.close()

    def exiit(self):
        self.value = 5
        self.MainWindow.close()


def get_values(ui):
    return ui.value

def main(ui):
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)



