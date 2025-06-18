from PyQt5 import QtCore, QtGui, QtWidgets
import sys

style = """QPushButton {
    background-color: rgb(85, 85, 127);\n
    font: 16pt \"MS Shell Dlg 2\";\n
    color: rgb(255, 255, 255);\n
    transition-duration: 0.4s;\n
    border-radius: 16px;
    margin:0;
    min-height: 40px;
}
QPushButton::hover {background-color: rgb(50, 60, 50)}"""

style_label = "QLabel { font: 16pt \"MS Shell Dlg 2\";\n" \
              "color: rgb(255, 255, 255);\n" \
              "max-height: 120px;}"

class Ui_MainWindow(object):
    def __init__(self, selection):
        self.selection = selection.lower()
        self.result = {"word": "", "meaning": ""}
        self.result_list = list()

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        print(self.selection)
        if self.selection == "noun":
            self.noun()

        elif self.selection == "adjective" or self.selection == "adverb":
            self.adjective_adverb()

        elif self.selection == "verb":
            self.verb()

        elif self.selection == "phrase":
            self.phrase()

    def noun(self):
        self.layout = QtWidgets.QGridLayout()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(788, 973)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(60, 2, 80);")

        self.frame = QtWidgets.QFrame(self.centralwidget)

        self.frame.setGeometry(QtCore.QRect(-1, -1, 591, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label.setObjectName("label")
        self.label.setStyleSheet(style_label)
        self.label.setAlignment(QtCore.Qt.AlignLeft)

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_2.setObjectName("label2")
        self.label_2.setStyleSheet(style_label)
        self.label_2.setAlignment(QtCore.Qt.AlignLeft)

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_3.setObjectName("label3")
        self.label_3.setStyleSheet(style_label)
        self.label_3.setAlignment(QtCore.Qt.AlignLeft)

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_4.setObjectName("label4")
        self.label_4.setStyleSheet(style_label)
        self.label_4.setAlignment(QtCore.Qt.AlignLeft)

        #TODO: Lines

        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_1.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                 "color: rgb(255, 255, 255);" 
                                 "min-height: 35px;" 
                  "margin-left: 40;"
                  "margin-right: 40;"
                  "margin-top: 20;" 
                  "margin-bottom: 20;"
                  "background-color: rgb(130, 130, 130);")
        self.lineEdit_1.setObjectName("lineEdit1")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                 "color: rgb(255, 255, 255);" 
                                 "min-height: 35px;" 
                  "margin-left: 40;"
                  "margin-right: 40;"
                  "margin-top: 20;" 
                  "margin-bottom: 20;"
                  "background-color: rgb(130, 130, 130);")
        self.lineEdit_2.setObjectName("lineEdit2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                 "color: rgb(255, 255, 255);" 
                                 "min-height: 35px;" 
                  "margin-left: 40;"
                  "margin-right: 40;"
                  "margin-top: 20;" 
                  "margin-bottom: 20;"
                  "background-color: rgb(130, 130, 130);")
        self.lineEdit_3.setObjectName("lineEdit3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "margin-left: 40;"
                                      "margin-right: 40;"
                                      "margin-top: 20;"
                                      "margin-bottom: 20;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_4.setObjectName("lineEdit4")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 331, 71))
        self.pushButton.setStyleSheet(style)
        self.pushButton.setObjectName("pushButton")

        tmp_layer1 = QtWidgets.QVBoxLayout()
        tmp_layer2 = QtWidgets.QVBoxLayout()
        tmp_layer3 = QtWidgets.QVBoxLayout()
        tmp_layer4 = QtWidgets.QVBoxLayout()
        tmp_layer5 = QtWidgets.QVBoxLayout()

        tmp_layer1.addWidget(self.label)
        tmp_layer1.addWidget(self.lineEdit_1)

        tmp_layer2.addWidget(self.label_2)
        tmp_layer2.addWidget(self.lineEdit_2)

        tmp_layer3.addWidget(self.label_3)
        tmp_layer3.addWidget(self.lineEdit_3)

        tmp_layer4.addWidget(self.label_4)
        tmp_layer4.addWidget(self.lineEdit_4)

        tmp_layer5.addWidget(self.pushButton)

        self.layout.addLayout(tmp_layer1, 1, 0)
        self.layout.addLayout(tmp_layer2, 2, 0)
        self.layout.addLayout(tmp_layer3, 3, 0)
        self.layout.addLayout(tmp_layer4, 4, 0)
        self.layout.addLayout(tmp_layer5, 5, 0)

        self.MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.layout.setContentsMargins(20, 20, 20, 20)
        self.centralwidget.setLayout(self.layout)

        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Eine neue Sprache lernen"))
        self.label.setText(_translate("MainWindow", "Wort"))
        self.label_2.setText(_translate("MainWindow", "Bedeutung (Meaning)"))
        self.label_3.setText(_translate("MainWindow", "Bestimmte Artikel"))
        self.label_4.setText(_translate("MainWindow", "Plural Form"))
        self.pushButton.setText(_translate("MainWindow", "Sparen"))
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.MainWindow.show()
        self.pushButton.clicked.connect(self.sparen_1)


    def adjective_adverb(self):
        self.layout = QtWidgets.QGridLayout()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(788, 973)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(60, 2, 80);")

        self.frame = QtWidgets.QFrame(self.centralwidget)

        self.frame.setGeometry(QtCore.QRect(-1, -1, 591, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label.setObjectName("label")
        self.label.setStyleSheet(style_label)
        self.label.setAlignment(QtCore.Qt.AlignLeft)

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_2.setObjectName("label2")
        self.label_2.setStyleSheet(style_label)
        self.label_2.setAlignment(QtCore.Qt.AlignLeft)

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_3.setObjectName("label3")
        self.label_3.setStyleSheet(style_label)
        self.label_3.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_1.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "margin-left: 40;"
                                      "margin-right: 40;"
                                      "margin-top: 20;"
                                      "margin-bottom: 20;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_1.setObjectName("lineEdit1")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "margin-left: 40;"
                                      "margin-right: 40;"
                                      "margin-top: 20;"
                                      "margin-bottom: 20;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_2.setObjectName("lineEdit2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "margin-left: 40;"
                                      "margin-right: 40;"
                                      "margin-top: 20;"
                                      "margin-bottom: 20;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_3.setObjectName("lineEdit3")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 331, 71))
        self.pushButton.setStyleSheet(style)
        self.pushButton.setObjectName("pushButton")

        tmp_layer1 = QtWidgets.QVBoxLayout()
        tmp_layer2 = QtWidgets.QVBoxLayout()
        tmp_layer3 = QtWidgets.QVBoxLayout()
        tmp_layer4 = QtWidgets.QVBoxLayout()

        tmp_layer1.addWidget(self.label)
        tmp_layer1.addWidget(self.lineEdit_1)

        tmp_layer2.addWidget(self.label_2)
        tmp_layer2.addWidget(self.lineEdit_2)

        tmp_layer3.addWidget(self.label_3)
        tmp_layer3.addWidget(self.lineEdit_3)

        tmp_layer4.addWidget(self.pushButton)

        self.layout.addLayout(tmp_layer1, 1, 0)
        self.layout.addLayout(tmp_layer2, 2, 0)
        self.layout.addLayout(tmp_layer3, 3, 0)
        self.layout.addLayout(tmp_layer4, 4, 0)

        self.MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.layout.setContentsMargins(20, 20, 20, 20)
        self.centralwidget.setLayout(self.layout)

        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Eine neue Sprache lernen"))
        self.label.setText(_translate("MainWindow", "Wort"))
        self.label_2.setText(_translate("MainWindow", "Bedeutung (Meaning)"))
        self.label_3.setText(_translate("MainWindow", "Das Antonym"))
        self.pushButton.setText(_translate("MainWindow", "Sparen"))
        self.MainWindow.show()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.pushButton.clicked.connect(self.sparen_4)

    def verb(self):
        self.layout = QtWidgets.QGridLayout()
        self.layout.setSpacing(40)
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1288, 973)

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(60, 2, 80);")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 591, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # wort
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label.setObjectName("label")
        self.label.setStyleSheet(style_label)
        self.label.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_1.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "min-width: 100px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_1.setObjectName("lineEdit1")
        # meaning
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_2.setObjectName("label2")
        self.label_2.setStyleSheet(style_label)
        self.label_2.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_2.setObjectName("lineEdit2")
        # dativ akkusativ
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_3.setObjectName("label3")
        self.label_3.setStyleSheet(style_label)
        self.label_3.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_3.setObjectName("lineEdit3")

        # preposition
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_33.setObjectName("label33")
        self.label_33.setStyleSheet(style_label)
        self.label_33.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_33.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_33.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_33.setObjectName("lineEdit33")

        # ich
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_4.setObjectName("label4")
        self.label_4.setStyleSheet(style_label)
        self.label_4.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "min-width: 100px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_4.setObjectName("lineEdit4")
        # du
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_5.setObjectName("label5")
        self.label_5.setStyleSheet(style_label)
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_5.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_5.setObjectName("lineEdit5")

        # Sie_sing
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_6.setObjectName("label6")
        self.label_6.setStyleSheet(style_label)
        self.label_6.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_6.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_6.setObjectName("lineEdit6")
        # er-sie-es
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_7.setObjectName("label7")
        self.label_7.setStyleSheet(style_label)
        self.label_7.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_7.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_7.setObjectName("lineEdit7")

        # wir
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_8.setObjectName("label8")
        self.label_8.setStyleSheet(style_label)
        self.label_8.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_8.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_8.setObjectName("lineEdit8")

        # ihr
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_9.setObjectName("label9")
        self.label_9.setStyleSheet(style_label)
        self.label_9.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_9.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_9.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_9.setObjectName("lineEdit9")

        # Sie_plur
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_10.setObjectName("label10")
        self.label_10.setStyleSheet(style_label)
        self.label_10.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_10.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_10.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_10.setObjectName("lineEdit10")

        # sie
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_11.setObjectName("label11")
        self.label_11.setStyleSheet(style_label)
        self.label_11.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_11.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_11.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_11.setObjectName("lineEdit11")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 331, 71))
        self.pushButton.setStyleSheet(style)
        self.pushButton.setObjectName("pushButton")

        #layers
        tmp_layer1 = QtWidgets.QVBoxLayout()
        tmp_layer1.addStretch(5)
        tmp_layer2 = QtWidgets.QVBoxLayout()
        tmp_layer2.addStretch(2)
        tmp_layer3 = QtWidgets.QVBoxLayout()
        tmp_layer3.addStretch(2)
        tmp_layer4 = QtWidgets.QVBoxLayout()

        #layer 1
        tmp_layer1.addWidget(self.label)
        tmp_layer1.addWidget(self.lineEdit_1)
        tmp_layer1.addWidget(self.label_2)
        tmp_layer1.addWidget(self.lineEdit_2)
        tmp_layer1.addWidget(self.label_3)
        tmp_layer1.addWidget(self.lineEdit_3)
        tmp_layer1.addWidget(self.label_33)
        tmp_layer1.addWidget(self.lineEdit_33)

        #layer 2
        tmp_layer2.addWidget(self.label_4)
        tmp_layer2.addWidget(self.lineEdit_4)
        tmp_layer2.addWidget(self.label_5)
        tmp_layer2.addWidget(self.lineEdit_5)
        tmp_layer2.addWidget(self.label_6)
        tmp_layer2.addWidget(self.lineEdit_6)
        tmp_layer2.addWidget(self.label_7)
        tmp_layer2.addWidget(self.lineEdit_7)

        #layer 3
        tmp_layer3.addWidget(self.label_8)
        tmp_layer3.addWidget(self.lineEdit_8)
        tmp_layer3.addWidget(self.label_9)
        tmp_layer3.addWidget(self.lineEdit_9)
        tmp_layer3.addWidget(self.label_10)
        tmp_layer3.addWidget(self.lineEdit_10)
        tmp_layer3.addWidget(self.label_11)
        tmp_layer3.addWidget(self.lineEdit_11)

        tmp_layer4.addWidget(self.pushButton)

        tmp_layer5 = QtWidgets.QHBoxLayout()
        tmp_layer5.addLayout(tmp_layer1)
        tmp_layer5.addLayout(tmp_layer2)
        tmp_layer5.addLayout(tmp_layer3)

        self.layout.addLayout(tmp_layer5, 0, 0)
        self.layout.addLayout(tmp_layer4, 1, 0)
        # tmp_layer4.addWidget(self.pushButton)

        self.MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.layout.setContentsMargins(20, 20, 20, 20)
        self.centralwidget.setLayout(self.layout)

        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Eine neue Sprache lernen"))
        self.label.setText(_translate("MainWindow", "Wort"))
        self.label_2.setText(_translate("MainWindow", "Bedeutung (Meaning)"))
        self.label_3.setText(_translate("MainWindow", "Dativ oder akkusativ"))
        self.label_33.setText(_translate("MainWindow", "Preposition"))
        self.label_4.setText(_translate("MainWindow", "Ich"))
        self.label_5.setText(_translate("MainWindow", "Du"))
        self.label_6.setText(_translate("MainWindow", "Sie Singular"))
        self.label_7.setText(_translate("MainWindow", "er-sie-es"))
        self.label_8.setText(_translate("MainWindow", "Wir"))
        self.label_9.setText(_translate("MainWindow", "Ihr"))
        self.label_10.setText(_translate("MainWindow", "Sie plural"))
        self.label_11.setText(_translate("MainWindow", "sie"))
        self.pushButton.setText(_translate("MainWindow", "Sparen"))
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.MainWindow.show()
        self.pushButton.clicked.connect(self.sparen_2)

    def phrase(self):
        self.layout = QtWidgets.QGridLayout()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(788, 973)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(60, 2, 80);")

        self.frame = QtWidgets.QFrame(self.centralwidget)

        self.frame.setGeometry(QtCore.QRect(-1, -1, 591, 571))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label.setObjectName("label")
        self.label.setStyleSheet(style_label)
        self.label.setAlignment(QtCore.Qt.AlignLeft)

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(160, 60, 401, 91))
        self.label_2.setObjectName("label2")
        self.label_2.setStyleSheet(style_label)
        self.label_2.setAlignment(QtCore.Qt.AlignLeft)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_1.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "margin-left: 40;"
                                      "margin-right: 40;"
                                      "margin-top: 20;"
                                      "margin-bottom: 20;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_1.setObjectName("lineEdit1")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 220, 571, 61))
        self.lineEdit_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";"
                                      "color: rgb(255, 255, 255);"
                                      "min-height: 35px;"
                                      "margin-left: 40;"
                                      "margin-right: 40;"
                                      "margin-top: 20;"
                                      "margin-bottom: 20;"
                                      "background-color: rgb(130, 130, 130);")
        self.lineEdit_2.setObjectName("lineEdit2")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 210, 331, 71))
        self.pushButton.setStyleSheet(style)
        self.pushButton.setObjectName("pushButton")

        tmp_layer1 = QtWidgets.QVBoxLayout()
        tmp_layer2 = QtWidgets.QVBoxLayout()
        tmp_layer3 = QtWidgets.QVBoxLayout()

        tmp_layer1.addWidget(self.label)
        tmp_layer1.addWidget(self.lineEdit_1)

        tmp_layer2.addWidget(self.label_2)
        tmp_layer2.addWidget(self.lineEdit_2)

        tmp_layer3.addWidget(self.pushButton)

        self.layout.addLayout(tmp_layer1, 1, 0)
        self.layout.addLayout(tmp_layer2, 2, 0)
        self.layout.addLayout(tmp_layer3, 3, 0)

        self.MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.layout.setContentsMargins(20, 20, 20, 20)
        self.centralwidget.setLayout(self.layout)

        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Eine neue Sprache lernen"))
        self.label.setText(_translate("MainWindow", "Wort"))
        self.label_2.setText(_translate("MainWindow", "Bedeutung (Meaning)"))
        self.pushButton.setText(_translate("MainWindow", "Sparen"))
        self.MainWindow.show()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
        self.pushButton.clicked.connect(self.sparen_3)

    def sparen_1(self):
        self.result_list.append(self.lineEdit_1.text())
        self.result_list.append(self.lineEdit_2.text())
        self.result_list.append(self.lineEdit_3.text())
        self.result_list.append(self.lineEdit_4.text())
        self.MainWindow.close()

    def sparen_2(self):
        self.result_list.append(self.lineEdit_1.text())
        self.result_list.append(self.lineEdit_2.text())
        self.result_list.append(self.lineEdit_3.text())
        self.result_list.append(self.lineEdit_33.text())
        self.result_list.append(self.lineEdit_4.text())
        self.result_list.append(self.lineEdit_5.text())
        self.result_list.append(self.lineEdit_6.text())
        self.result_list.append(self.lineEdit_7.text())
        self.result_list.append(self.lineEdit_8.text())
        self.result_list.append(self.lineEdit_9.text())
        self.result_list.append(self.lineEdit_10.text())
        self.result_list.append(self.lineEdit_11.text())
        self.MainWindow.close()

    def sparen_3(self):
        self.result_list.append(self.lineEdit_1.text())
        self.result_list.append(self.lineEdit_2.text())
        self.MainWindow.close()

    def sparen_4(self):
        self.result_list.append(self.lineEdit_1.text())
        self.result_list.append(self.lineEdit_2.text())
        self.result_list.append(self.lineEdit_3.text())
        self.MainWindow.close()

def get_values(ui):
    return ui.result_list

def main(ui):
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
