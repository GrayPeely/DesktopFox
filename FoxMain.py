#import libraries 
from tkinter import *
from tkinter import ttk

import time
import random

eventNum = 1

foxPet = Tk()
foxPet.title("Desktop Pet V4")

screenH = foxPet.winfo_screenheight()
screenW = foxPet.winfo_screenwidth()

#Initial Position, middle of screen
x = screenW//2
y = screenH//2

#Movement Values - num of pixels moved, direction
#Postitive will be down (y) and right (x)
#Negative up (y) and left (x)
xMovement = 1
yMovement = 1

windowSize = "128x128"

#test print
#print(str(x) + " + " + str(y))

foxPet.geometry(windowSize + "+" + str(x) + "+" + str(y))

foxPet.overrideredirect(True)
foxPet.configure(background='#FF00FF')
foxPet.wm_attributes('-transparentcolor', '#FF00FF')
foxPet.wm_attributes('-topmost', True)

sitFrames = [PhotoImage(file=f"fox sit" + str(i) + ".png") for i in range(1, 3)]
frameNum = 0

displayImage = Label(image = sitFrames[0])
#do not use .grid, creates extra space with white
#.pack positions leniently and doesnt create white pixels
displayImage.pack()

def anim():
    print("Anim")
    global frameNum
    global eventNum
    global sitFrames

    if(eventNum == 1):

        savedImage = sitFrames[frameNum]
        displayImage.config(image=savedImage)

        if(frameNum >= 1):
            frameNum = -1
    frameNum = frameNum + 1 
    foxPet.after(333, anim)


def event():
    global eventNum
    print("Event 1")
    eventNum = random.randint(1,1)
    foxPet.after(10000, event)

foxPet.after(100, anim)
foxPet.after(10000, event)
foxPet.mainloop()