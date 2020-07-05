# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GOOGLE.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_googlescreen(object):
    def setupUi(self, googlescreen):
        googlescreen.setObjectName("googlescreen")
        googlescreen.resize(653, 523)
        self.centralwidget = QtWidgets.QWidget(googlescreen)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 80, 221, 41))
        self.pushButton.setStyleSheet("font: 14pt \"Ravie\";")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 160, 291, 81))
        self.label.setStyleSheet("font: 14pt \"Kristen ITC\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.google = QtWidgets.QLabel(self.centralwidget)
        self.google.setGeometry(QtCore.QRect(-20, 0, 701, 521))
        self.google.setText("")
        self.google.setPixmap(QtGui.QPixmap("../../IMAGES/stains_paint_colorful_144932_3840x2160.jpg"))
        self.google.setScaledContents(True)
        self.google.setObjectName("google")
        self.google.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        googlescreen.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(googlescreen)
        self.statusBar.setObjectName("statusBar")
        googlescreen.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(googlescreen)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMenus = QtWidgets.QMenu(self.menuBar)
        self.menuMenus.setObjectName("menuMenus")
        googlescreen.setMenuBar(self.menuBar)
        self.actionGoToMain = QtWidgets.QAction(googlescreen)
        self.actionGoToMain.setObjectName("actionGoToMain")
        self.actionExit = QtWidgets.QAction(googlescreen)
        self.actionExit.setObjectName("actionExit")
        self.actionGO_BACK = QtWidgets.QAction(googlescreen)
        self.actionGO_BACK.setObjectName("actionGO_BACK")
        self.actionExit_2 = QtWidgets.QAction(googlescreen)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuMenus.addAction(self.actionGO_BACK)
        self.menuMenus.addSeparator()
        self.menuMenus.addAction(self.actionExit_2)
        self.menuBar.addAction(self.menuMenus.menuAction())

        self.retranslateUi(googlescreen)
        QtCore.QMetaObject.connectSlotsByName(googlescreen)

    def retranslateUi(self, googlescreen):
        _translate = QtCore.QCoreApplication.translate
        googlescreen.setWindowTitle(_translate("googlescreen", "MainWindow"))
        self.pushButton.setText(_translate("googlescreen", "Press N Speak!"))
        self.label.setText(_translate("googlescreen", "Query Google ..."))
        self.menuMenus.setTitle(_translate("googlescreen", "Menu"))
        self.actionGoToMain.setText(_translate("googlescreen", "GoToMain!"))
        self.actionExit.setText(_translate("googlescreen", "Exit!"))
        self.actionGO_BACK.setText(_translate("googlescreen", "GoToMain!"))
        self.actionExit_2.setText(_translate("googlescreen", "Exit!"))
