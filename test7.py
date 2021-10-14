import tkinter as tk
import time
import serial

ser = serial.Serial('COM4',9600)
reply = ""
cmnd1  = ":ACVOF,1#"
cmnd2  = ":ACVZ,1#"
cmnd3  = ":ACVM,1#"
cmnd7  = ":DCVOF,1#"
cmnd8  = ":DCVZ,1#"
cmnd9  = ":DCVM,1#"
cmnd13 = ":PF,1"
cmnd14 = ":ACW,1"
cmnd15 = ":DCW,1"
cmnd16 = ":EFP,1"
cmnd17 = ":ARSL,1"
cmnd18 = ":SVS,1"

def click(event):
    name_entry1.config(state = tk.NORMAL)
    name_entry1.delete(0, tk.END)

    name_entry2.config(state = tk.NORMAL)
    name_entry2.delete(0, tk.END)

    name_entry3.config(state = tk.NORMAL)
    name_entry3.delete(0, tk.END)

    name_entry4.config(state = tk.NORMAL)
    name_entry4.delete(0, tk.END)

    name_entry5.config(state = tk.NORMAL)
    name_entry5.delete(0, tk.END)

    name_entry6.config(state = tk.NORMAL)
    name_entry6.delete(0, tk.END)

def readserial():
    global reply
    data = cmnd1
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label1.config(text = reply)
    time.sleep(0.1)

    data = cmnd2
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label2.config(text = reply)
    time.sleep(0.1)

    data = cmnd3
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label3.config(text = reply)
    time.sleep(0.1)

    data = cmnd7
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label7.config(text = reply)
    time.sleep(0.1)

    data = cmnd8
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label8.config(text = reply)
    time.sleep(0.1)

    data = cmnd9
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label9.config(text = reply)
    time.sleep(0.1)

    name = name_var1.get()
    data = cmnd13+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label13.config(text = reply)
    name_var1.set("")
    time.sleep(0.1)

    name = name_var2.get()
    data = cmnd14+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label14.config(text = reply)
    name_var2.set("")
    time.sleep(0.1)

    name = name_var3.get()
    data = cmnd15+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label15.config(text = reply)
    name_var3.set("")
    time.sleep(0.1)

    name = name_var4.get()
    data = cmnd16+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label16.config(text = reply)
    name_var4.set("")
    time.sleep(0.1)

    name = name_var5.get()
    data = cmnd17+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label17.config(text = reply)
    name_var5.set("")
    time.sleep(0.1)

    name = name_var6.get()
    data = cmnd18+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        Label18.config(text = reply)
    name_var6.set("")

    #print("Invalid Command String")
    time.sleep(0.1)

root = tk.Tk()
root.title("Auto Calibration Desk")
root.config(bg = "darkgrey")
root.geometry("1920x1080")

name_var1 = tk.StringVar()
name_var2 = tk.StringVar()
name_var3 = tk.StringVar()
name_var4 = tk.StringVar()
name_var5 = tk.StringVar()
name_var6 = tk.StringVar()

Label0 = tk.Label(text= "Value from Arduino (Read Only Label)",font=("Helvetica", "10"),width=30,height=3,bg="powderblue")
Label0.place(x=600,y=25)

Label1 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label1.grid(row = 2, column = 2, pady = 100, padx = 20)

Label2 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label2.grid(row = 2, column = 3, padx = 20)

Label3 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label3.grid(row = 2, column = 4, padx = 20)

# Button that will call the readserial function
button1 = tk.Button(root, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',
                    command= readserial , height=2, width=10)
button1.place(x = 25, y = 175)

Label7 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label7.grid(row = 4, column = 2, padx = 20, pady = 100)

Label8 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label8.grid(row = 4, column = 3, padx = 20)

Label9 = tk.Label(text= reply,font=("Helvetica", "10"),width=25,height=3,bg="white")
Label9.grid(row = 4, column = 4, padx = 20)

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

# creating a entry for input
name_entry1 = tk.Entry(root, textvariable=name_var1, font=('calibre', 10, 'normal'), bg = "powderblue")
name_entry1.place(x= 30, y = 670, width = 175, height = 35)
name_entry1.insert(0,"Enter Data")
name_entry1.config(state = tk.DISABLED)
name_entry1.bind("<Button-1>",click)

name_entry2 = tk.Entry(root, textvariable=name_var2, font=('calibre', 10, 'normal'), bg = "powderblue")
name_entry2.place(x= 278, y = 670, width = 175, height = 35)
name_entry2.insert(0,"Enter Data")
name_entry2.config(state = tk.DISABLED)
name_entry2.bind("<Button-1>",click)

name_entry3 = tk.Entry(root, textvariable=name_var3, font=('calibre', 10, 'normal'), bg = "powderblue")
name_entry3.place(x= 526, y = 670, width = 175, height = 35)
name_entry3.insert(0,"Enter Data")
name_entry3.config(state = tk.DISABLED)
name_entry3.bind("<Button-1>",click)

name_entry4 = tk.Entry(root, textvariable=name_var4, font=('calibre', 10, 'normal'), bg = "powderblue")
name_entry4.place(x= 774, y = 670, width = 175, height = 35)
name_entry4.insert(0,"Enter Data")
name_entry4.config(state = tk.DISABLED)
name_entry4.bind("<Button-1>",click)

name_entry5 = tk.Entry(root, textvariable=name_var5, font=('calibre', 10, 'normal'), bg = "powderblue")
name_entry5.place(x= 1022, y = 670, width = 175, height = 35)
name_entry5.insert(0,"Enter Data")
name_entry5.config(state = tk.DISABLED)
name_entry5.bind("<Button-1>",click)

name_entry6 = tk.Entry(root, textvariable=name_var6, font=('calibre', 10, 'normal'), bg = "powderblue")
name_entry6.place(x= 1270, y = 670, width = 175, height = 35)
name_entry6.insert(0,"Enter Data")
name_entry6.config(state = tk.DISABLED)
name_entry6.bind("<Button-1>",click)

root.mainloop()