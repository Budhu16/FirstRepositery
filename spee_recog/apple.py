# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apple.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_applewindow(object):
    def setupUi(self, applewindow):
        applewindow.setObjectName("applewindow")
        applewindow.resize(708, 537)
        self.centralwidget = QtWidgets.QWidget(applewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 50, 711, 461))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 10, 131, 31))
        self.label.setStyleSheet("font: 16pt \"Kristen ITC\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 711, 531))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../IMAGES/4k-wallpaper-adventure-climb-691668.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.widget.raise_()
        self.label.raise_()
        applewindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(applewindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 21))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        applewindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(applewindow)
        self.statusbar.setObjectName("statusbar")
        applewindow.setStatusBar(self.statusbar)
        self.actionGO_BACK = QtWidgets.QAction(applewindow)
        self.actionGO_BACK.setObjectName("actionGO_BACK")
        self.actionExit_2 = QtWidgets.QAction(applewindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuExit.addAction(self.actionGO_BACK)
        self.menuExit.addSeparator()
        self.menuExit.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(applewindow)
        QtCore.QMetaObject.connectSlotsByName(applewindow)

    def retranslateUi(self, applewindow):
        _translate = QtCore.QCoreApplication.translate
        applewindow.setWindowTitle(_translate("applewindow", "MainWindow"))
        self.label.setText(_translate("applewindow", "WELCOME"))
        self.menuExit.setTitle(_translate("applewindow", "Menu"))
        self.actionGO_BACK.setText(_translate("applewindow", "GoToMain!"))
        self.actionExit_2.setText(_translate("applewindow", "Exit!"))
from PyQt5 import QtWebEngineWidgets
