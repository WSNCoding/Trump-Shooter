import tkinter as tkinter
from tkinter import *

def windowCode():
    root = tkinter.Tk()
    root.title("Game")# running a window
    root.geometry("300x300")
    canvas = tkinter.Canvas(root, width=100, height=100)

    frame = Frame(root)

    frame.grid()
    lbl = Label(frame, text = "Press the button below to DO STUFF")#Labels
    lbl.grid()

    bttn = Button(frame, text="Click me")#Buttons
    bttn.grid()
