from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import os
from os import path
import sys

import urllib.request

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"main.ui"))


class MainApp(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handleUI()   
        self.handleButton() 
        


    def handleUI (self):
        self.setFixedSize(450,125)
        self.setWindowTitle("pydownloader")

    def handleButton(self):
        self.pushButton_2.clicked.connect(self.handleDownload)

    def handleBrowse(self):
        pass

    def handleDownload(self):
        url=self.lineEdit_2.text()
        saveLocation=self.lineEdit.text()
        urllib.request.urlretrieve(url,saveLocation,self.handleProgress)

        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')

        QMessageBox.information(self,"Download Completed","The download finished")
    
    def handleProgress(self,blockNum,blockSize,totalSize):
        pass



def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()