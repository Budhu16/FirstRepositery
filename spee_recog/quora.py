# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quora.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuoraWindow(object):
    def setupUi(self, QuoraWindow):
        QuoraWindow.setObjectName("QuoraWindow")
        QuoraWindow.resize(702, 443)
        self.centralwidget = QtWidgets.QWidget(QuoraWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 291, 61))
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 100, 691, 361))
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 711, 431))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../IMAGES/hills_trees_fog_145436_3840x2160.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.widget.raise_()
        self.label.raise_()
        QuoraWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QuoraWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 21))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        QuoraWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QuoraWindow)
        self.statusbar.setObjectName("statusbar")
        QuoraWindow.setStatusBar(self.statusbar)
        self.actionGO_BACK = QtWidgets.QAction(QuoraWindow)
        self.actionGO_BACK.setObjectName("actionGO_BACK")
        self.actionExit = QtWidgets.QAction(QuoraWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuExit.addAction(self.actionGO_BACK)
        self.menuExit.addSeparator()
        self.menuExit.addAction(self.actionExit)
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(QuoraWindow)
        QtCore.QMetaObject.connectSlotsByName(QuoraWindow)

    def retranslateUi(self, QuoraWindow):
        _translate = QtCore.QCoreApplication.translate
        QuoraWindow.setWindowTitle(_translate("QuoraWindow", "MainWindow"))
        self.menuExit.setTitle(_translate("QuoraWindow", "Menu"))
        self.actionGO_BACK.setText(_translate("QuoraWindow", "GoToMain!"))
        self.actionExit.setText(_translate("QuoraWindow", "Exit!"))
from PyQt5 import QtWebEngineWidgets
