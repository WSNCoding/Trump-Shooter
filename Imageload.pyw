import tkinter
from tkinter import *

root =  tkinter.Tk()
canvas = tkinter.Canvas(width = 300, height = 300, bg='red')
img = "trump.gif" # nothuin
canvas.pack(expand = YES, fill = BOTH)
root.geometry = "300x300"

gif1 = tkinter.PhotoImage(file = 'trump.gif')#saves image
canvas.create_image(1,1, image = gif1 ,anchor = NW)#draws image
