import tkinter as tk
import time
import serial

ser = serial.Serial('COM4',9600)
data = ':ACVOF,1#'
reply = ""
cmnd1  = ":ACVOF,1#"
cmnd2  = ":ACVZ,1#"
cmnd3  = ":ACVM,1#"
cmnd4  = ":ACVOF,2#"
cmnd5  = ":ACVZ,2#"
cmnd6  = ":ACVM,2#"
cmnd7  = ":DCVOF,1#"
cmnd8  = ":DCVZ,1#"
cmnd9  = ":DCVM,1#"
cmnd10 = ":DCVOF,2#"
cmnd11 = ":DCVZ,2#"
cmnd12 = ":DCVM,2#"
def readserial(cmnd_str):
    global reply
    if(cmnd_str == cmnd1):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label1.config(text = reply)
    elif(cmnd_str == cmnd2):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label2.config(text = reply)
    elif(cmnd_str == cmnd3):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label3.config(text = reply)
    elif(cmnd_str == cmnd4):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label4.config(text = reply)
    elif(cmnd_str == cmnd5):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label5.config(text = reply)
    elif(cmnd_str == cmnd6):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label6.config(text = reply)
    elif(cmnd_str == cmnd7):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label7.config(text = reply)
    elif(cmnd_str == cmnd8):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label8.config(text = reply)
    elif(cmnd_str == cmnd9):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label9.config(text = reply)
    elif(cmnd_str == cmnd10):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label10.config(text = reply)
    elif(cmnd_str == cmnd11):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label11.config(text = reply)
    elif(cmnd_str == cmnd12):
        data = cmnd_str
        ser.write(data.encode())
        print("Command sent")
        time.sleep(2)
        if ser.in_waiting > 0:
            reply = ser.readline().decode()
            print("Reply from arduino = "+reply)
            Label12.config(text = reply)
    else:
        print("Invalid Command String")
    time.sleep(0.5)
root = tk.Tk()
root.title("Auto Calibration Desk")
root.config(bg = "darkgrey")
root.geometry("1920x1080")

Label0 = tk.Label(text= "Value from Arduino (Read Only Label)",font=("Helvetica", "10"),width=30,height=3,bg="powderblue")
Label0.place(x=600,y=25)

Label1 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label1.grid(row = 2, column = 2, pady = 100, padx = 20)

Label2 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label2.grid(row = 2, column = 3, padx = 20)

Label3 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label3.grid(row = 2, column = 4, padx = 20)

Label4 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label4.grid(row = 2, column = 5, padx = 20)

Label5 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label5.grid(row = 2, column = 6, padx = 20)

Label6 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label6.grid(row = 2, column = 7, padx = 20)

# Button that will call the readserial function
button1 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd1: readserial(m) , height=2, width=10)
button1.place(x = 25, y = 175)

button2 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd2: readserial(m) , height=2, width=10)
button2.place(x = 273, y = 175)

button3 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd3: readserial(m) , height=2, width=10)
button3.place(x = 521 , y = 175)

button4 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd4: readserial(m) , height=2, width=10)
button4.place(x = 769, y = 175)

button5 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd5: readserial(m) , height=2, width=10)
button5.place(x = 1017, y = 175)

button6 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd6: readserial(m) , height=2, width=10)
button6.place(x = 1265, y = 175)

Label7 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label7.grid(row = 4, column = 2, padx = 20, pady = 100)

Label8 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label8.grid(row = 4, column = 3, padx = 20)

Label9 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label9.grid(row = 4, column = 4, padx = 20)

Label10 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label10.grid(row = 4, column = 5, padx = 20)

Label11 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label11.grid(row = 4, column = 6, padx = 20)

Label12 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label12.grid(row = 4, column = 7, padx = 20)

#creating buttons

button7 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd7: readserial(m) , height=2, width=10)
button7.place(x = 25, y = 430)

button8 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd8: readserial(m) , height=2, width=10)
button8.place(x = 273, y = 430)

button9 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd9: readserial(m)  , height=2, width=10)
button9.place(x = 521, y = 430)

button10 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd10: readserial(m)  , height=2, width=10)
button10.place(x = 769, y = 430)

button11 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd11: readserial(m) , height=2, width=10)
button11.place(x = 1017, y = 430)

button12 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= lambda m= cmnd12: readserial(m) , height=2, width=10)
button12.place(x = 1265, y = 430)

Label13 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label13.grid(row = 5, column = 2, padx = 20, pady =100)

Label14 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label14.grid(row = 5, column = 3, padx = 20)

Label15 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label15.grid(row = 5, column = 4, padx = 20)

Label16 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label16.grid(row = 5, column = 5, padx = 20)

Label17 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label17.grid(row = 5, column = 6, padx = 20)

Label18 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label18.grid(row = 5, column = 7, padx = 20)

root.mainloop()