
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
        self.result = -1 # 0 is german, 1 is english
        self.MainWindow = MainWindow
        self.layout = QtWidgets.QGridLayout()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(710, 427)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 713, 427))
        self.frame.setStyleSheet("background-color: rgb(85, 2, 127);\n"
                                    "font: 16pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 60, 201, 91))
        self.label.setStyleSheet(style_label)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 331, 71))
        self.pushButton.setStyleSheet(style)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 290, 331, 71))
        self.pushButton_4.setStyleSheet(style)
        self.pushButton_4.setObjectName("pushButton_4")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        temp_layout = QtWidgets.QGridLayout()
        temp_layout.addWidget(self.label)
        temp_layout.addWidget(self.pushButton)
        temp_layout.addWidget(self.pushButton_4)
        self.frame.setLayout(temp_layout)

        self.layout.addWidget(self.frame)
        self.centralwidget.setLayout(self.layout)
        self.retranslateUi()
        self.pushButton.clicked.connect(self.german)
        self.pushButton_4.clicked.connect(self.english)
        self.MainWindow.show()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Language Selection"))
        self.label.setText(_translate("MainWindow", "Select Proper Action"))
        self.pushButton.setText(_translate("MainWindow", "German"))
        self.pushButton_4.setText(_translate("MainWindow", "English"))

    def german(self):
        self.result = 0
        self.MainWindow.close()

    def english(self):
        self.result = 1
        self.MainWindow.close()


def get_result(ui):
    return ui.result

def main(ui):
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
