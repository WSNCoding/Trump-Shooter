from tkinter import *

def windowCode():
    import tkinter   #Local function import
    print('Called')
    root = tkinter.Tk()
    root.title("Game")# running a window
    root.geometry("300x300")
    canvas = tkinter.Canvas(root, width=100, height=100)

    frame = tkinter.Frame(root)

    frame.grid()
    lbl = Label(frame, text = "Press the button below to DO STUFF")#Labels
    lbl.grid()

    bttn = Button(frame, text="Click me")#Buttons
    bttn.grid()

    myImage = PhotoImage(file="GetAttatchment.png")
    canvas.create_image(0,0,image=myImage)

windowCode()

#C:\Users\Christopher1\Desktop\Trump-Shooter\Trump Shooter\scripts\tkinterButtons.py
