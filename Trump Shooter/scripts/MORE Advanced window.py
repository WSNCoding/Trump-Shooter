import tkinter as tkinter 
from tkinter import messagebox 
 
 
top = tkinter.Tk() 
top.title("TRUMP SHOOTER") 
top.wm_iconbitmap("textures/favicon.ico") 
C = tkinter.Canvas(top, bg="blue", height=250, width=300) 
 
 
coord = 10, 50, 240, 210 
 
 
trump = C.create_arc(coord, start=0, extent=150, fill="red") 
 
C.pack() 
top.mainloop()