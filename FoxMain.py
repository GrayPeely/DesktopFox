#import libraries 
from tkinter import *
from tkinter import ttk

from PIL import Image
from PIL import ImageTk

import time
import random
import os

eventNum = 1

foxPet = Tk()
foxPet.title("Desktop Pet V4")

screenH = foxPet.winfo_screenheight()
screenW = foxPet.winfo_screenwidth()

#Initial Position, middle of screen
x = screenW//2
y = screenH//2
xDirection = 1
yDirection = 1

#mouse offset for when dragging
offset_x = 0
offset_y = 0

#Movement Values - num of pixels moved, direction
#Postitive will be down (y) and right (x)
#Negative up (y) and left (x)
xMovement = 1
yMovement = 1

#just input for size of window for ease of access/flexibility in future
windowSizeNum = 128
windowSize = str(windowSizeNum) + "x" + str(windowSizeNum)

#test print
#print(str(x) + " + " + str(y))

foxPet.geometry(windowSize + "+" + str(x) + "+" + str(y))

foxPet.overrideredirect(True)
foxPet.configure(background='#FF00FF')
foxPet.wm_attributes('-transparentcolor', '#FF00FF')
foxPet.wm_attributes('-topmost', True)

#fix later, but get from images folder
sitFrames = [PhotoImage(file=os.path.join("Images", "fox sit" + str(i) + ".png")) for i in range(1, 3)]
walkFrames = [PhotoImage(file = os.path.join("Images", "fox walk" + str(i) + ".png")) for i in range(1, 3)]
carryFrames = [PhotoImage(file=f"Images/fox carry" + str(i) + ".png") for i in range(1, 3)]
placeholderImg = ImageTk.PhotoImage(Image.open(os.path.join("Images", "Shaeczar.jpg"))) #i hate you tkinter for not supporting jpgs by default
ballImg = PhotoImage(file=os.path.join("Images","ball.png"))


reversedwalkFrames = []


for frame in walkFrames:
    imageToFlip = ImageTk.getimage(frame)
    flipped = imageToFlip.transpose(Image.FLIP_LEFT_RIGHT)
    reversedwalkFrames.append(ImageTk.PhotoImage(flipped))

#sleepFrames = [PhotoImage(file=f"fox sit" + str(i) + ".png") for i in range(1, 3)]
frameNum = 0
frameWait = 0

displayImage = Label(foxPet,image = sitFrames[0])
#do not use .grid, creates extra space with white
#.pack positions leniently and doesnt create white pixels
displayImage.pack()


#create a ball object for fox to follow

ball = Toplevel()
ball.overrideredirect(True)
ball.configure(background='#FF00FF')
ball.wm_attributes('-transparentcolor', '#FF00FF')
ball.wm_attributes('-topmost', True)

ballX = random.randint(0, screenW - 64)
ballY = random.randint(0, screenH - 64)
ball.geometry("64x64"+"+"+str(ballX)+"+"+str(ballY))

ballLabel = Label(ball,image=ballImg)
ballLabel.pack()



def movement(moveX, moveY):
   # print("Moves")
    global x
    global y
    global xDirection
    global yDirection

    if(x+moveX > 0 and x+moveX< (screenW - windowSizeNum)):
        x = x+moveX
        #print("x movement")
    else:
        xDirection = -1*(xDirection)
    if(y+moveY > 0 and y+moveY < (screenH - windowSizeNum)):
        y = y+moveY
    else: 
        yDirection = -1*(yDirection)
    
    foxPet.geometry(windowSize + "+" + str(x) +"+" + str(y))
   #print(str(x) + " + " + str(screenW))


def anim():
    #print("Anim 1")
    global frameNum
    global eventNum
    global sitFrames
    global placeholderImg
    global frameWait

    savedImage = placeholderImg

    frameWait = frameWait + 1

    if(frameWait<4):
        return
    frameWait = 0

    if(eventNum == 1):

        #change image
        savedImage = sitFrames[frameNum]
     
        if(frameNum >= 1):
            frameNum = -1
    if(eventNum == 2 or eventNum == 3 or eventNum == 4):
        #reverse anim if he hits a wall (of the screen)
        #later please make up and down frames, 2 will be left/right, 3 up/down
        if xDirection == -1:
            savedImage = walkFrames[frameNum]
        else:
            savedImage = reversedwalkFrames[frameNum]
        #play image
      
        if(frameNum >= 1):
            frameNum = -1

    if(eventNum == 50):
        savedImage = carryFrames[frameNum]
        if(frameNum >= 1):
            frameNum = -1
        
    
    frameNum = frameNum + 1 
    displayImage.config(image=savedImage)
    #foxPet.after(333, anim)   


def event():
    global eventNum
       #NUMBER OF EVENTS!!! INCLUSIVE!!! CHOSES RANDOM!!!
    randomNum = random.randint(1,4)
    print("Event " + str(randomNum))
    #event 50 will be dragging
    if(eventNum != 50 and randomNum != eventNum):
        eventNum = randomNum
    else:
 
        randomNum = random.randint(1,4)
    foxPet.after(10000, event)

#behavior loop
def behavior():
    global eventNum
    global xDirection
    global yDirection
    global xMovement
    global yMovement

    #event 2 is left/right movement across screen
    if(eventNum == 2):
        movement(xDirection*5, yDirection*random.randint(0,2))
    #event 3 is up down movement across screen
    if(eventNum == 3):
        movement(xDirection*random.randint(0,2), yDirection*5)
    if(eventNum == 4):
        xMovement = 3
        yMovement = 3
        if(x<ballX):
            xDirection = 1
        if(x>ballX):
            xDirection = -1
        if(y<ballY):
            yDirection = 1
        if(y>ballY):
            yDirection = -1
        movement(xMovement*xDirection, yMovement*yDirection)
        print(xMovement*xDirection)

#
def dragOffset(event):
    global offset_x
    global offset_y
    offset_x = event.x
    offset_y = event.y
    print(str(offset_x) + " + " + str(offset_y))

#This function allows the fox to be dragged around the screen
def drag_handler(event):
    global x
    global y
    global eventNum

    x = x + (event.x - offset_x)
    y = y + (event.y - offset_y)
    eventNum = 50
    foxPet.geometry(windowSize + "+" + str(x) + "+" + str(y))

def drag_release(event):
    global eventNum

    # return to a normal event
    eventNum = random.randint(1, 4)

#one single loop so everything is synced well
def mainController():
    behavior()
    anim()
    foxPet.after(50, mainController)

#Dragging foxy! Binds mouse1 to the dragOffset function, see above
foxPet.bind("<Button-1>", dragOffset)
#Actual drag, see above
foxPet.bind("<B1-Motion>", drag_handler)
#when this is released, will return back to normal 
foxPet.bind("<ButtonRelease-1>", drag_release)

foxPet.after(50, mainController)
foxPet.after(10000, event)
foxPet.mainloop()