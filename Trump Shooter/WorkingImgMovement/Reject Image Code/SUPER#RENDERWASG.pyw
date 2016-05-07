
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
    moveSpeed = 5
    
    def makewin(self):      
        global root
        global window
        root = tk.Tk()
        window = tk.Canvas(root,width=800,height=600)
        root.geometry("800x600")
        window.pack()


    def __init__(self):
        print("Game Loaded...100%")
        self.makewin()
        print("Images being created, leo is the best by the way, JK")
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
#        window.update()
        window.after(10,self.renderandupdate)
        

    def update(self):
        window.create_image(self.playerposX, self.playerposY, image=trump)
        if (self.playerposY > 50) & (self.playerposY < 570):
            self.playerposY+=self.moveY

        if (self.playerposX > 0) & (self.playerposX < 800):
            self.playerposX+=self.moveX     
 
    def handleKeyPress(self,event):   #Movement request detection

        if event.char == "a" or event.keysym == 'Left' and self.playerposX > 0:
            self.moveX =- self.moveSpeed
        if event.char =="d" or event.keysym == 'Right' and self.playerposX < 800:
            self.moveX = self.moveSpeed
        if event.char =="w" or event.keysym == 'Up' and self.playerposY > 50:
            self.moveY =- self.moveSpeed
        if event.char =="s" or event.keysym == 'Down' and self.playerposY < 570:
            self.moveY = self.moveSpeed

    def handleKeyRelease(self,event):

        if event.char == "a" or event.keysym == 'Left' and self.playerposX > 0:
            self.moveX=0
        if event.char =="d" or event.keysym == 'Right':
            self.moveX=0
        if event.char=="w" or event.keysym == 'Up':
            self.moveY=0
        if event.char=="s" or event.keysym == 'Down':
            self.moveY=0

        print("Key released: "+event.char)



class makeimage():
    def loadsprite(imagename, image):
        imagename = PhotoImage(file="image")
    def drawimage(imagename,x,y):
        window.create_image(x,y, image = imagename)
    
print("Starting...3%")
print("Starting...7%")
print("Starting...9%")
print("Starting...14%")
print("Starting...19%")
print("Starting...25%")
print("Starting...29%")
print("Starting...33%")
print("Starting...37%")
print("Starting...41%")
print("Starting...48%")
print("Starting...51%")
print("Starting...52%")
print("Starting...54%")
print("Starting...57%")
print("Starting...59%")
print("Starting...60%")
print("Starting...63%")
print("Starting...67%")
print("Starting...70%")
print("Starting...72%")
print("Starting...75%")
print("Starting...78%")
print("Starting...80%")
print("Starting...84%")
print("Starting...89%")
print("Starting...93%")
print("Starting...96%")

Everything()
root.mainloop()
    
