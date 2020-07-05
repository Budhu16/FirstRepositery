# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gmailui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gmailwindow(object):
    def setupUi(self, gmailwindow):
        gmailwindow.setObjectName("gmailwindow")
        gmailwindow.resize(654, 495)
        self.centralwidget = QtWidgets.QWidget(gmailwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 0, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 40, 631, 411))
        self.widget.setObjectName("widget")
        gmailwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(gmailwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenus = QtWidgets.QMenu(self.menubar)
        self.menuMenus.setObjectName("menuMenus")
        gmailwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(gmailwindow)
        self.statusbar.setObjectName("statusbar")
        gmailwindow.setStatusBar(self.statusbar)
        self.actionGO_BACK = QtWidgets.QAction(gmailwindow)
        self.actionGO_BACK.setObjectName("actionGO_BACK")
        self.actionExit = QtWidgets.QAction(gmailwindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenus.addAction(self.actionGO_BACK)
        self.menuMenus.addSeparator()
        self.menuMenus.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenus.menuAction())

        self.retranslateUi(gmailwindow)
        QtCore.QMetaObject.connectSlotsByName(gmailwindow)

    def retranslateUi(self, gmailwindow):
        _translate = QtCore.QCoreApplication.translate
        gmailwindow.setWindowTitle(_translate("gmailwindow", "MainWindow"))
        self.label.setText(_translate("gmailwindow", "Gmail.Com!"))
        self.menuMenus.setTitle(_translate("gmailwindow", "Menu"))
        self.actionGO_BACK.setText(_translate("gmailwindow", "GoToMain!"))
        self.actionExit.setText(_translate("gmailwindow", "Exit!"))
from PyQt5 import QtWebEngineWidgets
