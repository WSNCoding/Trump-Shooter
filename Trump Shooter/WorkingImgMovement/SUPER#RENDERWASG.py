
import time
import tkinter as tk
from tkinter import *


#player pos



#end of player pos

class Everything():


    playerposX = 100
    playerposY = 100

    def makewin(self):
        global root
        global window
        root = tk.Tk()
        window = tk.Canvas()
        root.geometry("300x300")
        window.pack()


    def __init__(self):
        print("starting")
        self.makewin()
        print("images being created, leo is the best by the way")
        global trump 
        global bullet
        trump =  PhotoImage(file="trumpy.gif")
        bullet =  PhotoImage(file="DollarBlast.gif")
        root.bind("<Key>", self.KeyHandler)
        window.after(0,self.renderandupdate) 

        global playerposX
        global playerposY
        
    def draw(self):       
        window.create_image(self.playerposX, self.playerposY, image=trump)
      

    def renderandupdate(self):
        window.delete("all")
        self.update()
        window.update()
        window.after(10,self.renderandupdate)
        

    def update(self):
        self.draw()


    def KeyHandler(self,event):
        if (event.char == "a") & (self.playerposX>0):
            self.playerposX = self.playerposX - 2
        if (event.char =="d") & (self.playerposX<300):
            self.playerposX = self.playerposX + 2
        if (event.char=="w") & (self.playerposY>300):
            self.playerposY = self.playerposY + 2
        if (event.char=="s") & (self.playerposY<0):
            self.playerposY = self.playerposY - 2
        #if (event.char==" ") & (self.ShowBullet==0):
         #   self.ShowBullet=1
          #  self.BulletX=self.x
           # self.BulletY=self.y-16
            #print("Fire!")

   


print("Starting...")
Everything()
    
    