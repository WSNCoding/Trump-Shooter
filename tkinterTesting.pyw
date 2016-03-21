import tkinter as tk
from tkinter import *
import time
root = tk.Tk()

TITLE="Testing"
HEIGHT=3000
WIDTH=3000
#Setup of window
root.title(TITLE)
#root.wm_iconbitmap("favicon.ico")
window = tk.Canvas(root,bg="blue",height=HEIGHT,width=WIDTH)

#Defining Widgets
class player():
    def __init__(self,window,x=0,y=0):
        self.x = x
        self.y = y
        self.img = tk.PhotoImage(file = 'drunk_trump.gif')
        self.player = window.create_image(self.x, self.y, image = self.img)
    def left(self,window):
        self.x=self.x-10
        print(self.x,self.y)
        window.coords(self.player,self.x,self.y)
    def right(self,window):
        self.x=self.x+10
        print(self.x,self.y)
        window.coords(self.player,self.x,self.y)
    def up(self,window):
        self.y=self.y-10
        print(self.x,self.y)
        window.coords(self.player,self.x,self.y)
    def down(self,window):
        self.y=self.y+10
        print(self.x,self.y)
        window.coords(self.player,self.x,self.y)
#Calling Widgets
square=player(window,x=100,y=100)

#Control Key Binds
up = "w";  down = "s";  left = "a";  right = "d"
def key(event):
    if event.char == left or event.keysym == 'Left':
       square.left(window)
    if event.char == right or event.keysym == 'Right':
        square.right(window)
    if event.char == up or event.keysym == 'Up':
       square.up(window)
    if event.char == down or event.keysym == 'Down':
        square.down(window)
window.focus_set()
window.bind("<Key>", key)
#Create program
window.pack()
root.mainloop()

