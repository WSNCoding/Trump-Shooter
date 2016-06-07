
import time
import tkinter as tk
from tkinter import *


#player pos



#end of player pos
class Everything:

    timestart=time.clock()
    Bullets = []
    playerposX = 400
    playerposY = 250
    moveX = 0
    moveY = 0
    moveSpeed = 5
    num = 0
    MaxBullets = 4

    
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

        global bulletimg
        
        global trump
        
        trump =  PhotoImage(file="trumpy.gif")
        bulletimg =  PhotoImage(file="DollarBlast.gif")

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
        #if self.i%33==0:
        #    print ("%.02f FPS"%(self.i/(time.clock()-self.timestart)))

        self.updatewindow()
        window.update()
        window.after(10,self.renderandupdate)
   

    def updatewindow(self):
        window.create_image(self.playerposX, self.playerposY, image=trump)


        #bullet logicality

        for singleBullet in self.Bullets:
            if (singleBullet.visible):
                window.create_image(singleBullet.xpos,singleBullet.ypos,image=bulletimg)
                singleBullet.moveBullet()
            else:
                self.Bullets.remove(singleBullet)

        
        if (self.playerposY > 510) & (self.moveY>0):
            self.moveY=0
            print("going ina direction called up")
        if (self.playerposY < 100) & (self.moveY<0):
            self.moveY=0

        if (self.playerposX > 710) & (self.moveX>0):
            self.moveX=0
            
        if (self.playerposX < 70) & (self.moveX<0):
            self.moveX=0      

        self.playerposY+=self.moveY
        self.playerposX+=self.moveX  
 
    def handleKeyPress(self,event):

        if (event.char == "a"):
            self.moveX=-self.moveSpeed
        if (event.char =="d"):
            self.moveX=self.moveSpeed
        if (event.char=="w"):
            self.moveY=-self.moveSpeed
        if (event.char=="s"):
            self.moveY=self.moveSpeed
        if (event.char == "A"):
            self.moveX=-self.moveSpeed
        if (event.char =="D"):
            self.moveX=self.moveSpeed
        if (event.char=="W"):
            self.moveY=-self.moveSpeed
        if (event.char=="S"):
            self.moveY=self.moveSpeed

        if (event.char==" "):
            if(self.Bullets.__len__() < self.MaxBullets):            
                self.Bullets.append(bullet(self.playerposX , self.playerposY))
                print("Fire!"+str(self.Bullets.__len__()))

    def handleKeyRelease(self,event):

        if (event.char == "a"):
            self.moveX=0
        if (event.char =="d"):
            self.moveX=0
        if (event.char=="w"):
            self.moveY=0
        if (event.char=="s"):
            self.moveY=0
        if (event.char == "A"):
            self.moveX=0
        if (event.char =="D"):
            self.moveX=0
        if (event.char=="W"):
            self.moveY=0
        if (event.char=="S"):
            self.moveY=0

        print("Key released"+event.char)



class makeimage():
    def loadsprite(imagename, image):
        imagename = PhotoImage(file="image")
    def drawimage(imagename,x,y):
        window.create_image(x,y, image = imagename)
    





class bullet:
    xpos=0
    ypos=0
    visible=False
    BulletSpeed = 8
    
    def __init__(self, x,y):
        self.ypos = y
        self.xpos = x
        self.visible = True
        self.lasttime = time.clock()
        self.newtime = 0

    def moveBullet(self):
        self.newtime = time.clock()
        if (self.newtime-self.lasttime)>0.005:
            self.ypos-=self.BulletSpeed
            self.lasttime=self.newtime
            if (self.ypos < 10):
                self.visible=False


















print("Starting...")
Everything()
root.mainloop()
    
