# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drivergui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
#
# https://www.youtube.com/watch?v=z33vwdHrAFM // link to pyqt tutorials
#
#Ian Holland

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import subprocess
from array import *
import serial
import serial.tools.list_ports

threads = [None,None,None,None]
# threads = [Relay,FRPS,MP-PT,MP-flow]
ports = ["none","none","none"]
# ports = [FRPS,MP-PT,MP-flow]

                
class Ui_MainWindow(object):
    buttons = [None,None,None,None]
    
    def newsourcecall(self):
        portlist = list(serial.tools.list_ports.comports())
        found = [0,0,0]
        for p in portlist:
            if((p.serial_number == "85235333035351303291") and (ports[2] == "none")):
                ports[2] = p.device
                if(port[2] != "None"):
                    self.MPFlowButton.setText("Start MP-Flow")
                found[2] = 1
             
            if((p.serial_number == "7543933333535110B091")):
                ports[1] = p.device
                if(port[1] != "None"):
                    self.MPPTButton.setText("Start MP-PT")
                found[1] = 1
        c = 0
        for i in found:
            if (i == 0):
                if(c == 0):
                    self.FRPSButton.setText("No FRPS")
                if(c == 1):
                    self.MPPTButton.setText("No MP-PT")
                if(c == 2):
                    self.MPFlowButton.setText("No MP-Flow")
            c = c+1    
    
    def relaycall(self):
        
        temp = self.RelayButton.text()
        
        if(temp == "Start Relay"):
            command = ["java","-jar", "relay.jar"]
            threads[0] = subprocess.Popen(command)
            self.RelayButton.setText("Stop Relay")
        else:
            threads[0].terminate()      
            self.RelayButton.setText("Start Relay")
        
            
    def FRPScall(self):
        temp = self.FRPSButton.text()
               
        if("Start" in temp):
            command = ["python","FR-Sensors_to-db.py",ports[0]]
            threads[1] = subprocess.Popen(command)      
            self.FRPSButton.setText( "Stop FRPS")
                  
        elif("Stop" in temp):
            threads[1].terminate()      
            self.FRPSButton.setText("Start FRPS")
                
    def MPPTcall(self):
               
        temp = self.MPPTbutton.text()
        if("Start" in temp):
            command = ["python","PT-MP_to-db.py",ports[1]]
            threads[2] = subprocess.Popen(command)
            self.MPPTbutton.setText("Stop MP-PT")
                     
        elif("Stop" in temp):
            threads[2].terminate() 
            self.MPPTbutton.setText("Start MP-PT")
                
    def MPflowcall(self):
               
        temp = self.MPFlowButton.text()
        if("Start" in temp):
            command = ["python","Flow-MP_to-db.py",ports[2]]
            threads[3] = subprocess.Popen(command)
            self.MPFlowButton.setText("Stop MP-Flow")
                    
        elif("Stop" in temp):
            threads[3].terminate()
            self.MPFlowButton.setText( "Start MP-Flow")
   
    def mstart():
        for b in buttons:
            temp = b.text()
            if("Start" in temp):
                if("Relay" in temp):
                    relaycall()
                    time.sleep(2)
                if("FRPS" in temp):
                    FRPScall()
                if("MP-PT" in temp):
                    MP_PTcall()
                if("MP Flow" in temp):
                    MPflowcall()                
            
    def mstop():
        for b in buttons:
            temp = b.text()
            if("Stop" in temp):
                if("Relay" in temp):
                    relaycall()
                if("FRPS" in temp):
                    FRPScall()
                if("MP-PT" in temp):
                    MP_PTcall() 
                if("MP Flow" in temp):
                    MPflowcall()
                    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 446)
        MainWindow.setMinimumSize(QtCore.QSize(600, 446))
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        
        self.RelayButton = QtWidgets.QPushButton(self.centralwidget)
        self.RelayButton.setMinimumSize(QtCore.QSize(131, 71))
        self.RelayButton.setMaximumSize(QtCore.QSize(262, 142))
        self.RelayButton.setFont(font)
        self.RelayButton.setObjectName("RelayButton")
        self.verticalLayout_11.addWidget(self.RelayButton)
        self.RelayButton.clicked.connect(self.relaycall)
        
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem)
        self.StartAll = QtWidgets.QPushButton(self.centralwidget)
        self.StartAll.setMinimumSize(QtCore.QSize(131, 71))
        self.StartAll.setMaximumSize(QtCore.QSize(262, 142))
        self.StartAll.setObjectName("StartAll")
        self.verticalLayout_11.addWidget(self.StartAll)
        self.StartAll.clicked.connect(self.mstart)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem1)
        self.FindSources = QtWidgets.QPushButton(self.centralwidget)
        self.FindSources.setMinimumSize(QtCore.QSize(131, 71))
        self.FindSources.setMaximumSize(QtCore.QSize(262, 142))
        self.FindSources.setObjectName("FindSources")
        self.verticalLayout_11.addWidget(self.FindSources)
        self.FindSources.clicked.connect(self.newsourcecall)
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 19, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem2)
        self.StopAll = QtWidgets.QPushButton(self.centralwidget)
        self.StopAll.setMinimumSize(QtCore.QSize(131, 71))
        self.StopAll.setMaximumSize(QtCore.QSize(262, 142))
        self.StopAll.setObjectName("StopAll")
        self.verticalLayout_11.addWidget(self.StopAll)
        self.StopAll.clicked.connect(self.mstop)
        
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_14.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_14)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        
        self.FRPSButton = QtWidgets.QPushButton(self.centralwidget)
        self.FRPSButton.setMinimumSize(QtCore.QSize(131, 71))
        self.FRPSButton.setMaximumSize(QtCore.QSize(262, 142))
        self.FRPSButton.setObjectName("FRPSButton")
        self.verticalLayout_12.addWidget(self.FRPSButton)
        self.FRPSButton.clicked.connect(self.FRPScall)
        
        spacerItem4 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem4)
        self.MPPTbutton = QtWidgets.QPushButton(self.centralwidget)
        self.MPPTbutton.setMinimumSize(QtCore.QSize(131, 71))
        self.MPPTbutton.setMaximumSize(QtCore.QSize(262, 142))
        self.MPPTbutton.setObjectName("MPPTbutton")
        self.verticalLayout_12.addWidget(self.MPPTbutton)
        self.MPPTbutton.clicked.connect(self.MPPTcall)
        
        spacerItem5 = QtWidgets.QSpacerItem(20, 19, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem5)
        self.MPFlowButton = QtWidgets.QPushButton(self.centralwidget)
        self.MPFlowButton.setMinimumSize(QtCore.QSize(131, 71))
        self.MPFlowButton.setMaximumSize(QtCore.QSize(262, 142))
        self.MPFlowButton.setObjectName("MPFlowButton")
        self.verticalLayout_12.addWidget(self.MPFlowButton)
        self.MPFlowButton.clicked.connect(self.MPflowcall)
        
        spacerItem6 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem6)
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setMinimumSize(QtCore.QSize(131, 71))
        self.pushButton_18.setMaximumSize(QtCore.QSize(262, 142))
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_12.addWidget(self.pushButton_18)
        
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setMinimumSize(QtCore.QSize(131, 71))
        self.pushButton_20.setMaximumSize(QtCore.QSize(262, 142))
        
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout_13.addWidget(self.pushButton_20)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem7)
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setMinimumSize(QtCore.QSize(131, 71))
        self.pushButton_22.setMaximumSize(QtCore.QSize(262, 142))
        
        self.pushButton_22.setObjectName("pushButton_22")
        self.verticalLayout_13.addWidget(self.pushButton_22)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem8)
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setMinimumSize(QtCore.QSize(131, 71))
        self.pushButton_19.setMaximumSize(QtCore.QSize(262, 142))
        
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_13.addWidget(self.pushButton_19)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem9)
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setMinimumSize(QtCore.QSize(131, 71))
        self.pushButton_21.setMaximumSize(QtCore.QSize(262, 142))
        
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout_13.addWidget(self.pushButton_21)
        self.horizontalLayout_2.addLayout(self.verticalLayout_13)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        buttons = [self.RelayButton,self.FRPSButton,self.MPPTbutton,self.MPFlowButton]
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Driver"))
        self.RelayButton.setText(_translate("MainWindow", "Start Relay"))
        self.StartAll.setText(_translate("MainWindow", "Start All"))
        self.FindSources.setText(_translate("MainWindow", "Find Sources"))
        self.StopAll.setText(_translate("MainWindow", "Stop All"))
        self.FRPSButton.setText(_translate("MainWindow", "No FRPS"))
        self.MPPTbutton.setText(_translate("MainWindow", "No MP-PT"))
        self.MPFlowButton.setText(_translate("MainWindow", "No MP-Flow"))
        self.pushButton_18.setText(_translate("MainWindow", "No Dummyone"))
        self.pushButton_20.setText(_translate("MainWindow", "No Dummytwo"))
        self.pushButton_22.setText(_translate("MainWindow", "No Dummythee"))
        self.pushButton_19.setText(_translate("MainWindow", "No Dummyfour"))
        self.pushButton_21.setText(_translate("MainWindow", "No Dummyfive"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

