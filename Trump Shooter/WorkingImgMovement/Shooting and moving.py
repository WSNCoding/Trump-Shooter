import tkinter as tk
import time as Time
root = tk.Tk()

TITLE="Testing"
HEIGHT=3000
WIDTH=3000

window = tk.Canvas(root,bg="blue",height=HEIGHT,width=WIDTH)



#Defining Widgets
class player():
    count = 1
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
        if self.y == 0:
            
            window.coords(self.player,self.x+30,self.y)

    def Shoot(self,window):
        bulletX = self.x
        bulletY = self.y

        self.dolla = tk.PhotoImage(file = 'DollarBlast.gif')
        bullet = window.create_image(self.bulletX, self.bulletY, image = self.dolla)
        while self.bulletY < 3030:
            self.bulletY = self.bullet+1
            moveBullet(window)

        count = 0


    def moveBullet(self,window):
        window.coords(bullet,bulletX,bulletY)
        
        print("You shooted dolla")
        #for self.count in range(0,300):
            #self.bulletY=self.bulletY+1

           # window.coords(self.bullet,self.bulletX,self.bulletY)
          #  self.count = self.count + 1
        #if self.count == 301:
         #   self.count = 0
            
#Control Key Binds
up = "w";  down = "s";  left = "a";  right = "d"; space = "space"
#Calling Widgets
square = player(window,x=100,y=100)

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
    if event.keysym == space:
        square.Shoot(window)



       
window.focus_set()
window.bind("<Key>", key)
#Create program
window.pack()
#moved stuff due to blocks


#Setup of window
root.title(TITLE)
#root.wm_iconbitmap("favicon.ico")





root.mainloop()

