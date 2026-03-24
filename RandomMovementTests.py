#Import tkinter, python's built in gui editor
from tkinter import *
from tkinter import ttk
#Import time for delays & such for events
import time
#Import random for events randomly happening
import random

windowSize = "100x100"

x = 50
y = 50
xMovement = 5
yMovement = 5

faceNum = 1

foxPet = Tk()
foxPet.title("Desktop Pet V3")
foxPet.geometry(windowSize + "+" + str(x) + "+" + str(y))

screenWidth = foxPet.winfo_screenwidth
screenHeight = foxPet.winfo_screenheight

foxPet.overrideredirect(True)
foxPet.configure(background='#85625B')
foxPet.wm_attributes('-transparentcolor', '#85625B')
foxPet.wm_attributes('-topmost', True)

faceImage_1 = PhotoImage(file="v1.png")
faceImage_2 = PhotoImage(file="v2.png")
faceImage_3 = PhotoImage(file="v3.png")

face = Label(image=faceImage_1)
face.grid()

def faceChange():
    global face
    global faceImage_1
    global faceImage_2
    global faceImage_3
    global faceNum
    #print("FACE CHANGE 1")
    if(faceNum == 1):
        face.config(image=faceImage_1)
    if(faceNum == 2):
        face.config(image=faceImage_2)
    if(faceNum == 3):
        face.config(image=faceImage_3)
    foxPet.after(500, faceChange)

def geometryChange():
    global x
    global y
    global windowSize

    foxPet.geometry(windowSize + "+" + str(x) +"+" + str(y))

def movement():
    global x
    global y
    global xMovement
    global yMovement
    global faceNum

    #print("movement 1")

    if(4 > random.randint(1,6)):
        if(random.randint(1,2) == 1):
            xMovement = 5
            faceNum = 1
            print("movement 2")
        else:
            if(x>0):
                xMovement = -5
            faceNum = 2
            print("movement 3")

        x = x+xMovement

    if(4 > random.randint(1,6)):
        if(random.randint(1,2) == 1):
            yMovement = 5
            
        else:
            if(y>0):
                yMovement = -5
            

        y = y+yMovement
        geometryChange()
    foxPet.after(25, movement)
    

foxPet.after(25, movement)
foxPet.after(500, faceChange)
foxPet.mainloop()
