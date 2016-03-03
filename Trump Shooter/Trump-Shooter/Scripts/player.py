import tkinter as tkinter
from tkinter import *

def player():

    root = Tk()
    
    trump = PhotoImage("\textures\GetAttachment.jpg");
    label = Label(root, image=trump)
    label.pack()

    root.mainloop()
    
player()
