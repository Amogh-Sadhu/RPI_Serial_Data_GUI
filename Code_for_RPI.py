import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
data = ':ACVOF,1#'
while True:
    ser.write(data.encode())
    print("Command sent")
    reply = ser.readline().decode()
    print("Response from arduino")
    print(reply)
    time.sleep(2)
