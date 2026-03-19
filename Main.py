from tkinter import *
from tkinter import ttk

boopCount = 0.0
face = "0w0"

root = Tk()
root.title("Desktop Pet Iteration 1!")
root.geometry('350x200')

foxy = Label(root, text = face)
foxy.grid()

def faceChange():
    global boopCount
    global face
    if(boopCount%2==0):
        face = "0w0"
    else:
        face = "-w-"


def clicked():
    global boopCount 
    boopCount += 1.0
    faceChange()
    foxy.config(text=face)
    print(boopCount%2)

butn = Button(root, text="Boop!", fg="purple", command=clicked)

butn.grid(column=0, row=1)

root.mainloop()

print("running?")