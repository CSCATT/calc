# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calc_v2.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(636, 396)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 92, 613, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.pushButtonC = QPushButton(self.verticalLayoutWidget)
        self.pushButtonC.setObjectName(u"pushButtonC")
        self.pushButtonC.setStyleSheet(u"background-color: rgb(255, 62, 14);\n"
"font: 16pt \"Impact\";\n"
"")

        self.horizontalLayout.addWidget(self.pushButtonC)

        self.pushButtonRise = QPushButton(self.verticalLayoutWidget)
        self.pushButtonRise.setObjectName(u"pushButtonRise")
        self.pushButtonRise.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 16pt \"Elephant\";")

        self.horizontalLayout.addWidget(self.pushButtonRise)

        self.pushButtonDiv = QPushButton(self.verticalLayoutWidget)
        self.pushButtonDiv.setObjectName(u"pushButtonDiv")
        self.pushButtonDiv.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 16pt \"Elephant\";")

        self.horizontalLayout.addWidget(self.pushButtonDiv)

        self.pushButtonSum = QPushButton(self.verticalLayoutWidget)
        self.pushButtonSum.setObjectName(u"pushButtonSum")
        self.pushButtonSum.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 16pt \"Elephant\";")

        self.horizontalLayout.addWidget(self.pushButtonSum)

        self.pushButtonMinus = QPushButton(self.verticalLayoutWidget)
        self.pushButtonMinus.setObjectName(u"pushButtonMinus")
        self.pushButtonMinus.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 16pt \"Elephant\";")

        self.horizontalLayout.addWidget(self.pushButtonMinus)

        self.pushButtonXZ = QPushButton(self.verticalLayoutWidget)
        self.pushButtonXZ.setObjectName(u"pushButtonXZ")
        self.pushButtonXZ.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 16pt \"Elephant\";")

        self.horizontalLayout.addWidget(self.pushButtonXZ)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_7 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.504975, fy:0.494, stop:0 rgba(195, 235, 52, 190), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 11pt \"Orbitron\";")

        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.504975, fy:0.494, stop:0 rgba(195, 235, 52, 190), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 11pt \"Orbitron\";")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.504975, fy:0.494, stop:0 rgba(195, 235, 52, 190), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 11pt \"Orbitron\";")

        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_1 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setEnabled(True)
        self.pushButton_1.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.504975, fy:0.494, stop:0 rgba(195, 235, 52, 190), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 11pt \"Orbitron\";")

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_percent = QPushButton(self.verticalLayoutWidget)
        self.pushButton_percent.setObjectName(u"pushButton_percent")
        self.pushButton_percent.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 16pt \"Elephant\";")

        self.gridLayout.addWidget(self.pushButton_percent, 4, 0, 1, 1)

        self.pushButton_result = QPushButton(self.verticalLayoutWidget)
        self.pushButton_result.setObjectName(u"pushButton_result")
        self.pushButton_result.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 16pt \"Elephant\";")

        self.gridLayout.addWidget(self.pushButton_result, 3, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.504975, fy:0.494, stop:0 rgba(195, 235, 52, 190), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 11pt \"Orbitron\";")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.504975, fy:0.494, stop:0 rgba(195, 235, 52, 190), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 11pt \"Orbitron\";")

        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.504975, fy:0.494, stop:0 rgba(195, 235, 52, 190), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 11pt \"Orbitron\";")

        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.504975, fy:0.494, stop:0 rgba(195, 235, 52, 190), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 11pt \"Orbitron\";")

        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.504975, fy:0.494, stop:0 rgba(195, 235, 52, 190), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 11pt \"Orbitron\";")

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_zero = QPushButton(self.verticalLayoutWidget)
        self.pushButton_zero.setObjectName(u"pushButton_zero")
        self.pushButton_zero.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.504975, fy:0.494, stop:0 rgba(195, 235, 52, 190), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 11pt \"Orbitron\";")

        self.gridLayout.addWidget(self.pushButton_zero, 3, 1, 1, 1)

        self.pushButton_dot = QPushButton(self.verticalLayoutWidget)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        self.pushButton_dot.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 16pt \"Elephant\";")

        self.gridLayout.addWidget(self.pushButton_dot, 3, 2, 1, 1)

        self.pushButton_upper = QPushButton(self.verticalLayoutWidget)
        self.pushButton_upper.setObjectName(u"pushButton_upper")
        self.pushButton_upper.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 16pt \"Elephant\";")

        self.gridLayout.addWidget(self.pushButton_upper, 4, 1, 1, 1)

        self.pushButton_log = QPushButton(self.verticalLayoutWidget)
        self.pushButton_log.setObjectName(u"pushButton_log")
        self.pushButton_log.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"font: 16pt \"Elephant\";")

        self.gridLayout.addWidget(self.pushButton_log, 4, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(12, 11, 611, 71))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButtonC.setText(QCoreApplication.translate("Dialog", u"C", None))
        self.pushButtonRise.setText(QCoreApplication.translate("Dialog", u"*", None))
        self.pushButtonDiv.setText(QCoreApplication.translate("Dialog", u"/", None))
        self.pushButtonSum.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.pushButtonMinus.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.pushButtonXZ.setText(QCoreApplication.translate("Dialog", u"<", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.pushButton_1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.pushButton_percent.setText(QCoreApplication.translate("Dialog", u"%", None))
        self.pushButton_result.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.pushButton_zero.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.pushButton_dot.setText(QCoreApplication.translate("Dialog", u".", None))
        self.pushButton_upper.setText(QCoreApplication.translate("Dialog", u"^", None))
        self.pushButton_log.setText(QCoreApplication.translate("Dialog", u"log", None))
    # retranslateUi

