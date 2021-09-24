import tkinter as tk
from typing import Text
import serial
import time

from serial.serialutil import Timeout   
def serialdatacheck(): 
    Label3.config(text=" ")
    time.sleep(2)
    global arduino
    if (arduino.in_waiting>0):
        return arduino.readline().decode()

    else:
        return "Error- Saurav chutya"

def check_data():
    Label1.config(text = serialdatacheck())    

def parse_data():
    data = str(serialdatacheck())
    names_list = data.split("-")
    names_list = [x.replace("\r\n","") for x in names_list]
    names_list = list(filter(None,names_list))
    Label2.config(text = names_list)  

root = tk.Tk() 
root.geometry("600x400")

Label1 = tk.Label(
    text=" ",
    width=25,
    height=3,
    bg="white"
)
Label2 = tk.Label(
    text=" ",
    width=25,
    height=3,
    bg="white"
)
Label3 = tk.Label(
    text=" ",
    width=20,
    height=3,
)

try:
    global arduino
    arduino = serial.Serial('COM5',9600, timeout=1)
    Label3.config(text="")
except:
    Label3.config(text="No port found \n connect arduino properly")

button1 = tk.Button(
    text = "Check data",
    width=10,
    height=2,
    command=check_data
)
button2 = tk.Button(
    text = "Parse Data",
    width=10,
    height=2,
    command=parse_data
)
button1.place(x=160,y=250)
button2.place(x=350,y=250)
Label1.place(x=100,y=100)
Label2.place(x=300,y=100)
Label3.place(x=240,y=20)
root.title("serial data transfer")
root.mainloop()
