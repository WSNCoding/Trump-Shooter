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
    def __init__(self,window,x=0,y=0,size=100):
        self.size = size
        self.x = x
        self.y = y
        self.player = window.create_rectangle((x,y,x+size,y+size),fill="red")
    def left(self,window):
        self.x=self.x-10
        window.coords(self.player,self.x,self.y,self.x+self.size,self.y+self.size)
        window.pack()
    def right(self,window):
        self.x=self.x+10
        window.coords(self.player,self.x,self.y,self.x+self.size,self.y+self.size)
        window.pack()
    def up(self,window):
        self.y=self.y-10
        window.coords(self.player,self.x,self.y,self.x+self.size,self.y+self.size)
        window.pack()
    def down(self,window):
        self.y=self.y+10
        window.coords(self.player,self.x,self.y,self.x+self.size,self.y+self.size)
        window.pack()
#Calling Widgets
square=player(window,x=100,y=100,size=300)

#Control Key Binds
up = 'UIp';  down = 'Down';  left = 'Left';  right = 'Right'
def key(event):
    print("Pressed:", repr(event.char))
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
