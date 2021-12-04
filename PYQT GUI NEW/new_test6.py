import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtSerialPort
from PyQt5.QtWidgets import QDialog,QApplication, QStackedWidget, QMainWindow, QAction
import time
import serial

start = ','
end = '#'
global ser

reply = ""
cmnd1  = ":ACVOF,1#"
cmnd2  = ":ACVZ,1#"
cmnd3  = ":ACVM,1#"
cmnd4  = ":DCVOF,1#"
cmnd5  = ":DCVZ,1#"
cmnd6  = ":DCVM,1#"
cmnd7 = ":PF,1"
cmnd8 = ":ACW,1"
cmnd9 = ":DCW,1"
cmnd10 = ":EFP,1"
cmnd11 = ":ARSL,1"
cmnd12 = ":SVS,1"

class main_screen(QMainWindow):
    def __init__(self):
        super(main_screen, self).__init__()
        loadUi("main_window.ui", self)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.reset.clicked.connect(self.resetlabel)
        self.scan.clicked.connect(self.readserial)
        self.actionQuit.triggered.connect(lambda: self.QApplication.quit())
        #self.actionCOM4.triggered.connect(self.selectport)
        #port_list = []
        self.availableport()
    def availableport(self):
        try:
            for info in QtSerialPort.QSerialPortInfo.availablePorts():
                #self.portname_comboBox.addItem(info.portName())
                #port_list.append(info.portName())
                val1 = info.portName()
                #print(val1)
                self.port1 = QAction(val1,self)
                self.menuPort.addAction(self.port1)
            self.port1.triggered.connect(lambda: self.connectport(val1))
            #self.menuPort.addAction(info.portName())
        except:
            print("no port detected")
            self.label_16.setText("No Port Detected")
            self.label_16.setAlignment(QtCore.Qt.AlignCenter)

        #print(port_list)
        #self.COM4.triggered.connect(self.selectport)
        #self.menuPort.triggered.connect(self.availableport)
    def connectport(self, portN):
        try:
            global ser
            #ser = serial.Serial('COM4', 9600)
            ser = serial.Serial(portN, 9600)
            self.label_16.setText("Connected")
            self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        except:
            print("port not connected")
            self.label_16.setText("Not connected")
            self.label_16.setAlignment(QtCore.Qt.AlignCenter)

    def selectport(self):
        try:
            global ser
            ser = serial.Serial('COM4', 9600)
            self.label_16.setText("Connected")
            self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        except:
            print("not port connected")
            self.label_16.setText("Not connected")
            self.label_16.setAlignment(QtCore.Qt.AlignCenter)

    def resetlabel(self):
        self.label_1.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.progressBar.setValue(0)

    def readserial(self):
        try:
            global reply
            self.progressBar.setValue(0)
            data = cmnd1
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = " + reply)
                info = reply[reply.find(start) + len(start) + 2:reply.rfind(end)]
                self.label_1.setText(info)
                self.label_1.setAlignment(QtCore.Qt.AlignCenter)
            time.sleep(0.1)

            self.progressBar.setValue(8)
            data = cmnd2
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = "+reply)
                info = reply[reply.find(start) + len(start) + 2:reply.rfind(end)]
                self.label_2.setText(info)
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
            time.sleep(0.1)

            self.progressBar.setValue(16)
            data = cmnd3
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = "+reply)
                info = reply[reply.find(start) + len(start) + 2:reply.rfind(end)]
                self.label_3.setText(info)
                self.label_3.setAlignment(QtCore.Qt.AlignCenter)
            time.sleep(0.1)

            self.progressBar.setValue(24)
            data = cmnd4
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = "+reply)
                info = reply[reply.find(start) + len(start) + 2:reply.rfind(end)]
                self.label_4.setText(info)
                self.label_4.setAlignment(QtCore.Qt.AlignCenter)
            time.sleep(0.1)

            self.progressBar.setValue(32)
            data = cmnd5
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = "+reply)
                info = reply[reply.find(start) + len(start) + 2:reply.rfind(end)]
                self.label_5.setText(info)
                self.label_5.setAlignment(QtCore.Qt.AlignCenter)
            time.sleep(0.1)

            self.progressBar.setValue(40)
            data = cmnd6
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = "+reply)
                info = reply[reply.find(start) + len(start) + 2:reply.rfind(end)]
                self.label_6.setText(info)
                self.label_6.setAlignment(QtCore.Qt.AlignCenter)
            time.sleep(0.1)

            self.progressBar.setValue(48)
            data1 = self.data_field.text()
            data = cmnd7+","+data1+"#"
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = "+reply)
                self.label_7.setText(reply)
                self.label_7.setAlignment(QtCore.Qt.AlignCenter)
                #self.label_7.setAlignment(QtCore.Qt.AlignJustify)
            time.sleep(0.1)

            self.progressBar.setValue(56)
            data = cmnd8+","+data1+"#"
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = "+reply)
                self.label_8.setText(reply)
                self.label_8.setAlignment(QtCore.Qt.AlignCenter)
            time.sleep(0.1)

            self.progressBar.setValue(64)
            data = cmnd9+","+data1+"#"
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = "+reply)
                self.label_9.setText(reply)
                self.label_9.setAlignment(QtCore.Qt.AlignCenter)
            time.sleep(0.1)

            self.progressBar.setValue(72)
            data = cmnd10+","+data1+"#"
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = "+reply)
                self.label_10.setText(reply)
                self.label_10.setAlignment(QtCore.Qt.AlignCenter)
            time.sleep(0.1)

            self.progressBar.setValue(80)
            data = cmnd11+","+data1+"#"
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = "+reply)
                self.label_11.setText(reply)
                self.label_11.setAlignment(QtCore.Qt.AlignCenter)
            time.sleep(0.1)

            self.progressBar.setValue(88)
            data = cmnd12+","+data1+"#"
            ser.write(data.encode())
            print("Command sent")
            time.sleep(2)
            if ser.in_waiting > 0:
                reply = ser.readline().decode()
                print("Reply from arduino = "+reply)
                self.label_12.setText(reply)
                self.label_12.setAlignment(QtCore.Qt.AlignCenter)
            self.data_field.setText("")
            time.sleep(0.1)
            self.progressBar.setValue(100)
        except:
            print("port not selected")
            self.label_16.setText("Port Not Connected")
            self.label_16.setAlignment(QtCore.Qt.AlignCenter)



#main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Screen1 = main_screen()
    widget = QStackedWidget()
    widget.addWidget(Screen1)
    widget.setFixedHeight(319)
    widget.setFixedWidth(679)
    widget.setWindowTitle("Calibration Desk")
    widget.show()
    app.exec()