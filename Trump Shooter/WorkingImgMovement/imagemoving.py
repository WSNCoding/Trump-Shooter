import tkinter as tk
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
        self.img = tk.PhotoImage(file = 'trumpy.gif')
        self.player = window.create_image(self.x, self.y, image = self.img)
    def left(self,window):
        self.x=self.x-10
        print(self.x,self.y)
        window.coords(self.player,self.x,self.y)
    def right(self,window):
        self.x=self.x+10
        window.coords(self.player,self.x,self.y)
    def up(self,window):
        self.y=self.y-10
        window.coords(self.player,self.x,self.y)
    def down(self,window):
        self.y=self.y+10
        window.coords(self.player,self.x,self.y)
#Calling Widgets
square=player(window,x=100,y=100)

#Control Key Binds
up = "w";  down = "s";  left = "a";  right = "d"
def key(event):
    if event.char == left:
       square.left(window)
    if event.char == right:
        square.right(window)
    if event.char == up:
       square.up(window)
    if event.char == down:
        square.down(window)
    if event.keysym == left: 
       square.left(window) 
    if event.keysym == right: 
        square.right(window) 
    if event.keysym == up: 
       square.up(window) 
    if event.keysym == down:
        square.down(window)
window.focus_set()
window.bind("<Key>", key)
#Create program
window.pack()
root.mainloop()

