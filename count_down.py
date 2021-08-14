from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

global endTime

def quit(*args):
    root.destroy()

def cant_wait():
    timeLeft = endTime - datetime.datetime.now()
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)

    txt.set(timeLeft)
    if(timeLeft.seconds != 0):
        root.after(1000, cant_wait)
    else:
        root.configure(background='red')
        lbl.configure(background='red')

root = Tk()
root.attributes("-fullscreen",False)
root.configure(background='black')
root.bind("x", quit)
root.after(1000, cant_wait)

endTime = datetime.datetime(2021,8,6,6,4)
fnt = font.Font(family='Helvetica',size=90,weight='bold')
txt = StringVar()
lbl = ttk.Label(root,textvariable=txt,font=fnt,foreground='white',background='black')
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()