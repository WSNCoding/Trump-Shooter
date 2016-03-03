import tkinter as tkinter 
from tkinter import messagebox 
from tkinter import *
 
top = tkinter.Tk() 
top.title("TRUMP SHOOTER") 
#top.wm_iconbitmap("textures/favicon.ico") 
C = tkinter.Canvas(top, bg="blue", height=250, width=300)
frame = Frame(top, width=100, height=100)
def KEYTEST():
    print("HEY")
    
frame.bind("<Button-1>",KEYTEST())
forwardkey = "w"
def key(event):
    print("WOW")



def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame.bind("<Key-w>", key)
frame.bind("<Button-1>", callback)
frame.pack()

#coord = 10, 50, 240, 210 

top.mainloop() 

#trump = C.create_arc(coord, start=0, extent=150, fill="red") 


