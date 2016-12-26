# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setGeometry(QtCore.QRect(70, 40, 75, 23))
        self.openButton.setObjectName("openButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 91, 631, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.writeButton = QtWidgets.QPushButton(self.centralwidget)
        self.writeButton.setGeometry(QtCore.QRect(70, 370, 75, 23))
        self.writeButton.setObjectName("writeButton")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu_E = QtWidgets.QMenu(self.menubar)
        self.menu_E.setObjectName("menu_E")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionLOG = QtWidgets.QAction(MainWindow)
        self.actionLOG.setObjectName("actionLOG")
        self.actionAndroid = QtWidgets.QAction(MainWindow)
        self.actionAndroid.setObjectName("actionAndroid")
        self.menu_F.addAction(self.action)
        self.menu_E.addAction(self.actionLOG)
        self.menu_E.addAction(self.actionAndroid)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openButton.setText(_translate("MainWindow", "打开文件"))
        self.writeButton.setText(_translate("MainWindow", "写入代码"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_E.setTitle(_translate("MainWindow", "设置(&E)"))
        self.action.setText(_translate("MainWindow", "打开"))
        self.actionLOG.setText(_translate("MainWindow", "LOG文件路径"))
        self.actionAndroid.setText(_translate("MainWindow", "Android代码路径"))

