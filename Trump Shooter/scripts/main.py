#Library imports
import os
from tkinter import *
#Modular imports
from player import *
import tkinterButtons as btns
import player as plyr
#Define mainloop
def main():
  print('Running main.py')
  btns.windowCode()
  plyr.player()

if __name__=='__main__':
  main()
