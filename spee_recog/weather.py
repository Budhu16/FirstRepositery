# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WeatherWindow(object):
    def setupUi(self, WeatherWindow):
        WeatherWindow.setObjectName("WeatherWindow")
        WeatherWindow.resize(701, 485)
        self.centralwidget = QtWidgets.QWidget(WeatherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 50, 701, 391))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        WeatherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WeatherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenus = QtWidgets.QMenu(self.menubar)
        self.menuMenus.setObjectName("menuMenus")
        WeatherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WeatherWindow)
        self.statusbar.setObjectName("statusbar")
        WeatherWindow.setStatusBar(self.statusbar)
        self.actionGO_BACK = QtWidgets.QAction(WeatherWindow)
        self.actionGO_BACK.setObjectName("actionGO_BACK")
        self.actionExit = QtWidgets.QAction(WeatherWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenus.addAction(self.actionGO_BACK)
        self.menuMenus.addSeparator()
        self.menuMenus.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenus.menuAction())

        self.retranslateUi(WeatherWindow)
        QtCore.QMetaObject.connectSlotsByName(WeatherWindow)

    def retranslateUi(self, WeatherWindow):
        _translate = QtCore.QCoreApplication.translate
        WeatherWindow.setWindowTitle(_translate("WeatherWindow", "MainWindow"))
        self.label.setText(_translate("WeatherWindow", "Check Weather Here...."))
        self.menuMenus.setTitle(_translate("WeatherWindow", "Menu"))
        self.actionGO_BACK.setText(_translate("WeatherWindow", "GoToMain!"))
        self.actionExit.setText(_translate("WeatherWindow", "Exit!"))
from PyQt5 import QtWebEngineWidgets
