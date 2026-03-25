#testing out image generation
from tkinter import *
from tkinter import ttk
import time

wSize = '100x100'
x = 0
y = 0
xDir = 1
yDir = 1
faceNum = 1



root = Tk()
root.title("Desktop Pet V2")
root.geometry(wSize+"+" + str(x) +"+" + str(y))

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.overrideredirect(True)
root.configure(background='#85625B')
root.wm_attributes('-transparentcolor', '#85625B')
root.wm_attributes('-topmost', True)

face1 = PhotoImage(file="v1.png")
face2 = PhotoImage(file="v2.png")
face3 = PhotoImage(file="v3.png")

#face selected
faceSelec = Label(image=face1)

faceSelec.grid()

def faceChange():
    global faceSelec
    global face1
    global face2
    global face3
    global faceNum

    if(faceNum == 1):
        faceNum = 2
        faceSelec.config(image=face2)
    elif (faceNum == 2):
        faceNum = 3
        faceSelec.config(image=face3)
    elif (faceNum == 3):
        faceNum = 1
        faceSelec.config(image=face1)

    root.after(1000, faceChange)

def move():
    global x
    global xDir
    global y
    global yDir
    global wSize
    global screen_height
    global screen_width

   
    x = x+(5*xDir)

    if(x>screen_width-100):
        xDir=-1
    elif(x<0):
        yDir=1
    
    y= y+(5*yDir)

    if(y>screen_height-100):
        yDir=-1
    elif(y<0):
        yDir=1

    root.geometry(wSize + "+" + str(x) +"+" + str(y))

    print("X: " + str(x) + " Y: " + str(y))
    #print(str(xDir) + " + " + str(yDir))


    root.after(100, move)

root.after(50, move)
root.after(1000, faceChange)

root.mainloop()
