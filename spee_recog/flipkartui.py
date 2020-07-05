# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flipkartui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_flipwindow(object):
    def setupUi(self, flipwindow):
        flipwindow.setObjectName("flipwindow")
        flipwindow.resize(653, 497)
        self.centralwidget = QtWidgets.QWidget(flipwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 60, 631, 391))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 681, 481))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../IMAGES/altitude-clouds-daylight-1450082.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.widget.raise_()
        flipwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(flipwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenus = QtWidgets.QMenu(self.menubar)
        self.menuMenus.setObjectName("menuMenus")
        flipwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(flipwindow)
        self.statusbar.setObjectName("statusbar")
        flipwindow.setStatusBar(self.statusbar)
        self.actionGO_BACK = QtWidgets.QAction(flipwindow)
        self.actionGO_BACK.setObjectName("actionGO_BACK")
        self.actionExit = QtWidgets.QAction(flipwindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenus.addAction(self.actionGO_BACK)
        self.menuMenus.addSeparator()
        self.menuMenus.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenus.menuAction())

        self.retranslateUi(flipwindow)
        QtCore.QMetaObject.connectSlotsByName(flipwindow)

    def retranslateUi(self, flipwindow):
        _translate = QtCore.QCoreApplication.translate
        flipwindow.setWindowTitle(_translate("flipwindow", "MainWindow"))
        self.label.setText(_translate("flipwindow", "Filpkart.Com!"))
        self.menuMenus.setTitle(_translate("flipwindow", "Menu"))
        self.actionGO_BACK.setText(_translate("flipwindow", "GoToMain!"))
        self.actionExit.setText(_translate("flipwindow", "Exit!"))
from PyQt5 import QtWebEngineWidgets
