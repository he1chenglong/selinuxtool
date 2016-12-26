# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.py'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QInputDialog,QLineEdit,QFileDialog

from untitled  import Ui_MainWindow
import sys
import time
from avc2allow import analysisrule

class mywindow(QtWidgets.QWidget,Ui_MainWindow):

    analysis = analysisrule()
    rules=[]
    logdirectory = r'E:\0-双系统\lxc_log_tool\androidlog_2016\12\23100830-open se\host'
    androiddirectory = "W:\\temp_zz001_network\\android.host\\"

    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)


        self.action.triggered.connect(self.fileopen) #菜单的点击事件是triggered
        self.actionLOG.triggered.connect(self.logpath) #菜单的点击事件是triggered
        self.actionAndroid.triggered.connect(self.androidpath) #菜单的点击事件是triggered

        self.writeButton.clicked.connect(self.writerule)

        self.openButton.clicked.connect(self.fileopen)


    def writerule(self):
        print("start write")
        self.analysis.addrule(self.rules,self.androiddirectory)


    def logpath(self):
        self.logdirectory = QFileDialog.getExistingDirectory(self,"选取LOG文件夹","C:/")
        print(self.logdirectory)

    def androidpath(self):
        self.androiddirectory = QFileDialog.getExistingDirectory(self,"选取ANDROI文件夹","C:/")
        print(self.androiddirectory)

    # 文件打开 对话框的 例子
    def fileopen(self):
        directory=r'E:\0-双系统\lxc_log_tool\androidlog_2016\12\23100830-open se\host'

        fileName, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          self.logdirectory,
                                                          "All Files (*);;Text Files (*.txt)")
        print(fileName,filetype)
        self.rules=self.analysis.parser(fileName)
        self.textBrowser.setText("")

        for info in self.rules:
            print(info)
            print(type(info))
            self.textBrowser.append(info)

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())
