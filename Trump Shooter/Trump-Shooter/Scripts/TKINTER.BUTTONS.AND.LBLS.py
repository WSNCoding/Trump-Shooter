import tkinter as tkinter
from tkinter import *

root = tkinter.Tk()
root.title("Ollie")# running a window
root.geometry("300x300")
canvas = tkinter.Canvas(root, width=100, height=100)

frame = Frame(root)

frame.grid()
lbl = Label(frame, text = "wolkj")#Labels
lbl.grid()

bttn = Button(frame, text="Hi")#Buttons
bttn.grid()
