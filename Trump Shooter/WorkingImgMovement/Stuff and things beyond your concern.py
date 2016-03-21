
import tkinter
from tkinter import *
import time


class game:

    i = 0
    timestart=time.clock()
    x=100
    y=100
    BulletX=100
    BulletY=100
    ShowBullet=0
    moveX=0
    moveY=0
    moveSpeed=10

    def __init__(self,view):
        global w
        global hotoimage
        global ghostimage
        global bulletimage
        self.i=33
        w = Canvas(view, width=800, height=600)
        w.pack()
        w.after(0,self.render) # INCREASE THE 0 TO SLOW IT DOWN
        w.create_line(0, 0, 50, 20, fill="#476042", width=3)

        hotoimage = PhotoImage(file="trumpy.gif")
        
        bulletimage =  PhotoImage(file="DollarBlast.gif")
        view.bind("<Key>", self.handleKeyPress)


    def render(self):
        global i
        w.update()
        self.i+=1
        if self.i%33==0:
            print ("%.02f FPS"%(self.i/(time.clock()-self.timestart)))
        self.UpdateGame()
        w.after(10,self.render)


    def UpdateGame(self):
        w.delete("all") # clear canvas
        # draw our items on the canvas
        w.create_image(self.x, self.y, image=hotoimage)
        w.create_image(300,300,image=ghostimage)

        # do we draw bullet
        if (self.ShowBullet==1):
            w.create_image(self.BulletX,self.BulletY,image=bulletimage)
            self.BulletY-=2
            if (self.BulletY<10):
                self.ShowBullet=0

        # move charactor is necasary
        if (self.moveY<0) & (self.y >0):
            self.moveY+=1
            self.y=self.y-2
        if(self.moveY>0) & (self.y < 600):
            self.moveY-=1
            self.y=self.y+2
        if (self.moveX<0) & (self.x > 0):
            self.moveX+=1
            self.x=self.x-2
        if(self.moveX>0) & (self.x < 800):
            self.moveX-=1
            self.x=self.x+2

    def f(self):
        return 'hello world'


    def handleKeyPress(self,event):

        if (event.char == "a") & (self.moveX>-self.moveSpeed):
            self.moveX-=self.moveSpeed
        if (event.char =="d") & (self.moveX<self.moveSpeed):
            self.moveX+=self.moveSpeed
        if (event.char=="w") & (self.moveY>-self.moveSpeed):
            self.moveY-=self.moveSpeed
        if (event.char=="x") & (self.moveY<self.moveSpeed):
            self.moveY+=self.moveSpeed
        if (event.char==" ") & (self.ShowBullet==0):
            self.ShowBullet=1
            self.BulletX=self.x
            self.BulletY=self.y-16
            print("Fire!")

        print("x "+str(self.moveX)+" y "+str(self.moveY))



class Application():
    def __init__(self, master):


        master.title('Hello, Tkinter!')
        master.geometry('800x640') # Size 800x600

        

        master.mainloop()



view = tkinter.Tk()
app = Application(view)

