from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import os
from os import path
import sys
from math import acos,cos,asin,sin,sqrt,pi

#Constants
R=6738
A_GEO=42164
rad=pi/180

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"main.ui"))


class MainApp(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handleUi()
        self.handleButton()

    
    def handleUi(self):
        self.setFixedSize(475,240)


    def cal (self):
        #Data
        try:
        
            EarthLatitude=float(self.lineEdit.text())
            EarthLongitude=float(self.lineEdit_2.text())
            satLongitude=float(self.lineEdit_3.text())

            #Calculate
            B=EarthLongitude - satLongitude

            if (B==0):
                Az='Irrelevant'
                El=90
                self.label_6.setText(Az)
                self.label_7.setText(str(round(El,3)))
                self.label_9.setText('')
                
            
            elif(EarthLatitude==0):
                if (B<0):
                    Az=90
                elif(B>0):
                    Az=270

                b=acos(cos(B*rad)*cos(EarthLatitude*rad))
                d=sqrt(R**2+A_GEO**2-2*R*A_GEO*cos(b))
                El=acos((A_GEO/d)*sin(b))*180/pi
                self.label_6.setText(str(round(Az,3)))
                self.label_7.setText(str(round(El,3)))
                
            else:
                b=acos(cos(B*rad)*cos(EarthLatitude*rad))
                A=asin(sin(abs(B)*rad)/sin(b))*180/pi
               
                if   (EarthLatitude<0 and B<0 ):
                    Az=A
                elif (EarthLatitude<0 and B>0 ):
                    Az=360-A
                elif (EarthLatitude>0 and B<0 ):
                    Az=180-A 
                elif (EarthLatitude>0 and B>0 ):
                    Az=180+A
              
                d=sqrt(R**2+A_GEO**2-2*R*A_GEO*cos(b))
                El=acos((A_GEO/d)*sin(b))*180/pi
                #Azimuth
                self.label_6.setText(str(round(Az,3)))

                #Elevation
                self.label_7.setText(str(round(El,3)))
        
        except:
            QMessageBox.about(self,"invalid values","Enter valid values  ")

        

    def handleButton(self):
        self.calculate.clicked.connect(self.cal)

    

def main():
    app=QApplication(sys.argv)
    window=MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()