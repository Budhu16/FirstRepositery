# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtubeui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_youtubewindow(object):
    def setupUi(self, youtubewindow):
        youtubewindow.setObjectName("youtubewindow")
        youtubewindow.resize(700, 550)
        self.centralwidget = QtWidgets.QWidget(youtubewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 0, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 50, 681, 451))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 701, 521))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../IMAGES/relief_surface_sinuous_123145_1366x768.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.widget.raise_()
        youtubewindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(youtubewindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenus = QtWidgets.QMenu(self.menubar)
        self.menuMenus.setObjectName("menuMenus")
        youtubewindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(youtubewindow)
        self.statusbar.setObjectName("statusbar")
        youtubewindow.setStatusBar(self.statusbar)
        self.actionGO_BACK = QtWidgets.QAction(youtubewindow)
        self.actionGO_BACK.setObjectName("actionGO_BACK")
        self.actionExit = QtWidgets.QAction(youtubewindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenus.addAction(self.actionGO_BACK)
        self.menuMenus.addSeparator()
        self.menuMenus.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenus.menuAction())

        self.retranslateUi(youtubewindow)
        QtCore.QMetaObject.connectSlotsByName(youtubewindow)

    def retranslateUi(self, youtubewindow):
        _translate = QtCore.QCoreApplication.translate
        youtubewindow.setWindowTitle(_translate("youtubewindow", "MainWindow"))
        self.label.setText(_translate("youtubewindow", "Youtube..."))
        self.menuMenus.setTitle(_translate("youtubewindow", "Menu"))
        self.actionGO_BACK.setText(_translate("youtubewindow", "GoToMain!"))
        self.actionExit.setText(_translate("youtubewindow", "Exit!"))
from PyQt5 import QtWebEngineWidgets
