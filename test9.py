import tkinter as tk
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

def resetlabel():
    label1.config(text ="")
    label2.config(text="")
    label3.config(text="")
    label4.config(text="")
    label5.config(text="")
    label6.config(text="")
    label7.config(text="")
    label8.config(text="")
    label9.config(text="")
    label10.config(text="")
    label11.config(text="")
    label12.config(text="")

def readserial():
    global reply
    data = cmnd1
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        info = reply[reply.find(start)+len(start)+2:reply.rfind(end)]
        label1.config(text = info)
    time.sleep(0.1)

    data = cmnd2
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        info = reply[reply.find(start) + len(start) + 2:reply.rfind(end)]
        label2.config(text = info)
    time.sleep(0.1)

    data = cmnd3
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        info = reply[reply.find(start) + len(start) + 2:reply.rfind(end)]
        label3.config(text = info)
    time.sleep(0.1)

    data = cmnd4
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        info = reply[reply.find(start) + len(start) + 2:reply.rfind(end)]
        label4.config(text = info)
    time.sleep(0.1)

    data = cmnd5
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        info = reply[reply.find(start) + len(start) + 2:reply.rfind(end)]
        label5.config(text = info)
    time.sleep(0.1)

    data = cmnd6
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        info = reply[reply.find(start) + len(start) + 2:reply.rfind(end)]
        label6.config(text = info)
    time.sleep(0.1)

    name = name_var1.get()
    data = cmnd7+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        label7.config(text = reply)
    name_var1.set("")
    time.sleep(0.1)

    name = name_var2.get()
    data = cmnd8+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        label8.config(text = reply)
    name_var2.set("")
    time.sleep(0.1)

    name = name_var3.get()
    data = cmnd9+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        label9.config(text = reply)
    name_var3.set("")
    time.sleep(0.1)

    name = name_var4.get()
    data = cmnd10+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        label10.config(text = reply)
    name_var4.set("")
    time.sleep(0.1)

    name = name_var5.get()
    data = cmnd11+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        label11.config(text = reply)
    name_var5.set("")
    time.sleep(0.1)

    name = name_var6.get()
    data = cmnd12+","+name+"#"
    ser.write(data.encode())
    print("Command sent")
    time.sleep(2)
    if ser.in_waiting > 0:
        reply = ser.readline().decode()
        print("Reply from arduino = "+reply)
        label12.config(text = reply)
    name_var6.set("")

    #print("Invalid Command String")
    time.sleep(0.1)

root = tk.Tk()
root.title("Frame Testing")
root.config(bg = "darkgrey")
root.geometry("720x520")

name_var1 = tk.StringVar()
name_var2 = tk.StringVar()
name_var3 = tk.StringVar()
name_var4 = tk.StringVar()
name_var5 = tk.StringVar()
name_var6 = tk.StringVar()

frame1 = tk.Frame(root,bg = "lightgrey",width = 400, height=465)
frame1.place(x=30,y=35)

frame2 = tk.Frame(root,bg = "lightgrey", width= 250, height= 230)
frame2.place(x=450,y=35)

frame3 = tk.Frame(root,bg="lightgrey", width= 250, height= 190)
frame3.place(x=450,y=310)

Labeltext0 = tk.Label(root,text= "CALIBRATOR",font=("Helvetica", "15"),width=20,height=1,bg="darkgrey")
Labeltext0.place(x=280,y=6)

Labeltext1 = tk.Label(frame1,text= "Label1",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext1.place(x=23,y=0)

Labeltext2 = tk.Label(frame1,text= "Label2",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext2.place(x=23,y=75)

Labeltext3 = tk.Label(frame1,text= "Label3",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext3.place(x=23,y=150)

Labeltext4 = tk.Label(frame1,text= "Label4",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext4.place(x=23,y=225)

Labeltext5 = tk.Label(frame1,text= "Label5",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext5.place(x=23,y=300)

Labeltext6 = tk.Label(frame1,text= "Label6",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext6.place(x=23,y=375)

Labeltext7 = tk.Label(frame1,text= "Label7",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext7.place(x=213,y=0)

Labeltext8 = tk.Label(frame1,text= "Label8",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext8.place(x=213,y=75)

Labeltext9 = tk.Label(frame1,text= "Label9",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext9.place(x=213,y=150)

Labeltext10 = tk.Label(frame1,text= "Label10",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext10.place(x=213,y=225)

Labeltext11 = tk.Label(frame1,text= "Label11",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext11.place(x=213,y=300)

Labeltext12 = tk.Label(frame1,text= "Label12",font=("Helvetica", "10"),width=20,height=2,bg="lightgrey")
Labeltext12.place(x=213,y=375)

label1 = tk.Label(frame1, text= reply, anchor = "n", bg = "darkgrey",width=20, height=2)
label1.place(x=30,y=30)

label2 = tk.Label(frame1, text= reply , anchor = "n", bg = "darkgrey",width=20, height=2)
label2.place(x=30,y=105)

label3 = tk.Label(frame1, text= reply, anchor = "n", bg = "darkgrey",width=20, height=2)
label3.place(x=30,y=180)

label4 = tk.Label(frame1, text= reply, anchor = "n", bg = "darkgrey",width=20, height=2)
label4.place(x=30,y=255)

label5 = tk.Label(frame1, text= reply , anchor = "n", bg = "darkgrey",width=20, height=2)
label5.place(x=30,y=330)

label6 = tk.Label(frame1, text= reply , anchor = "n", bg = "darkgrey",width=20, height=2)
label6.place(x=30,y=405)

label7 = tk.Label(frame1, text= reply , anchor = "n", bg = "darkgrey",width=20, height=2)
label7.place(x=220,y=30)

label8 = tk.Label(frame1, text= reply, anchor = "n", bg = "darkgrey",width=20, height=2)
label8.place(x=220,y=105)

label9 = tk.Label(frame1, text= reply , anchor = "n", bg = "darkgrey",width=20, height=2)
label9.place(x=220,y=180)

label10 = tk.Label(frame1, text= reply , anchor = "n", bg = "darkgrey",width=20, height=2)
label10.place(x=220,y=255)

label11 = tk.Label(frame1, text= reply , anchor = "n", bg = "darkgrey",width=20, height=2)
label11.place(x=220,y=330)

label12 = tk.Label(frame1, text= reply , anchor = "n", bg = "darkgrey",width=20, height=2)
label12.place(x=220,y=405)

button1 = tk.Button(frame2, text='Scan',font = ("Helvetica","10"), fg='black', bg='grey',command= readserial, height=3, width=15)
button1.place(x = 62, y = 130)

button2 = tk.Button(frame3, text='Reset',font = ("Helvetica","10"), fg='black', bg='grey', command= resetlabel, height=3, width=15)
button2.place(x = 62, y = 100)

name_var1 = tk.StringVar()

name_entry1 = tk.Entry(frame3, textvariable=name_var1, font=('calibre', 10, 'normal'), bg = "MistyRose2")
name_entry1.place(x= 85, y = 20, width = 120, height = 35)

Labeltext13 = tk.Label(frame3,text= "Enter Data",font=("Helvetica", "10"),width=7,height=2,bg="lightgrey")
Labeltext13.place(x=10,y=20)

clicked = tk.StringVar()
options = [
    "0",
    "1",
    "2",
    "3"
]
drop = tk.OptionMenu( frame2 , clicked, *options )
drop.config( bg = "MistyRose2")
drop.place(x= 100, y=35, width = 100, height = 35)

Labeltext14 = tk.Label(frame2,text= "Channel",font=("Helvetica", "10"),width=7,height=2,bg="lightgrey")
Labeltext14.place(x=40,y=35)

root.mainloop()