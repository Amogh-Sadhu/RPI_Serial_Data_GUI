import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog,QApplication, QStackedWidget
import time
import serial

start = ','
end = '#'


ser = serial.Serial('COM4',9600)
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



class main_screen(QDialog):
    def __init__(self):
        super(main_screen, self).__init__()
        loadUi("auto_calibrator.ui", self)
        self.reset.clicked.connect(self.resetlabel)
        self.scan.clicked.connect(self.readserial)

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

    def readserial(self):
        global reply
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

        data1 = self.data_field.text()
        data = cmnd7+","+data1+"#"
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            #reply = "abhijeet"
            print("Reply from arduino = "+reply)
            self.label_7.setText(reply)
            self.label_7.setAlignment(QtCore.Qt.AlignCenter)
            #self.label_7.setAlignment(QtCore.Qt.AlignJustify)

        #self.data_field.setText("")
        time.sleep(0.1)

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

#main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Screen1 = main_screen()
    widget = QStackedWidget()
    widget.addWidget(Screen1)
    widget.setFixedHeight(270)
    widget.setFixedWidth(679)
    widget.setWindowTitle("Calibration desk")
    widget.show()
    app.exec()