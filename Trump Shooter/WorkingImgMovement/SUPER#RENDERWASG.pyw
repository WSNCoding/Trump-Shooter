
import time
import tkinter as tk
from tkinter import *


#player pos



#end of player pos

class Everything():

    timestart=time.clock()

    playerposX = 400
    playerposY = 250
    moveX = 0
    moveY = 0
    moveSpeed = 10
    
    def makewin(self):      
        global root
        global window
        root = tk.Tk()
        window = tk.Canvas(root,width=800,height=600)
        root.geometry("800x600")
        window.pack()


    def __init__(self):
        print("starting")
        self.makewin()
        print("images being created, leo is the best by the way")
        self.i=33

       
        
        global trump
        
        global bullet
        trump =  PhotoImage(file="trumpy.gif")
        bullet =  PhotoImage(file="DollarBlast.gif")

        #bindings
        root.bind("<Key>", self.handleKeyPress)
        root.bind("<KeyRelease>", self.handleKeyRelease)

        window.after(0,self.renderandupdate)


        global playerposX
        global playerposY
        window.mainloop()
        
    
    def renderandupdate(self):
        window.delete("all")
        self.i+=1
        if self.i%33==0:
            print ("%.02f FPS"%(self.i/(time.clock()-self.timestart)))

        self.update()
        window.update()
        window.after(10,self.renderandupdate)
        

    def update(self):
        window.create_image(self.playerposX, self.playerposY, image=trump)
        if (self.playerposY >50) & (self.playerposY<570):
            self.playerposY+=self.moveY

        if (self.playerposX > 0) & (self.playerposX < 800):
            self.playerposX+=self.moveX
        
 
    def handleKeyPress(self,event):

        if (event.char == "a"):
            self.moveX=-self.moveSpeed
        if (event.char =="d"):
            self.moveX=self.moveSpeed
        if (event.char=="w"):
            self.moveY=-self.moveSpeed
        if (event.char=="x"):
            self.moveY=self.moveSpeed

    def handleKeyRelease(self,event):

        if (event.char == "a"):
            self.moveX=0
        if (event.char =="d"):
            self.moveX=0
        if (event.char=="w"):
            self.moveY=0
        if (event.char=="x"):
            self.moveY=0

        print("Key released"+event.char)



class makeimage():
    def loadsprite(imagename, image):
        imagename = PhotoImage(file="image")
    def drawimage(imagename,x,y):
        window.create_image(x,y, image = imagename)
    


print("Starting...")
Everything()
root.mainloop()
    
