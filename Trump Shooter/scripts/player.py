from tkinter import *

def player():
    import tkinter  #Local function import
    root = tkinter.Tk()
    
    trump = PhotoImage("\textures\GetAttachment.jpg");
    label = Label(root, image=trump)
    label.pack()

    root.mainloop()
    
player()
