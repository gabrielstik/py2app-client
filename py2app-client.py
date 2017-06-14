# -*- coding: utf-8 -*-

import os
import sys
if sys.version_info < (3, 0):
    from Tkinter import *
else:
    from tkinter import *
import tkFileDialog

labelPadY = (20,0)
submitPadY = 20
backgroundColor = "#0000ff"
textColor = "#ffffff"

def build():
    try:
        pathImg
    except:
        pathImg = ''
    setup = "from setuptools import setup\n\nAPP = ['"+pathPy+"']\nDATA_FILES = []\nOPTIONS = {'argv_emulation': True,\n\t'iconfile': '"+pathImg+"'}\nsetup(\n\tapp=APP,\n\tdata_files=DATA_FILES,\n\toptions={'py2app': OPTIONS},\n\tsetup_requires=['py2app']\n)"
    setupFile = open("setup.py","w")
    setupFile.write(setup)
    setupFile.close()
    os.system("echo ' ' | sudo -S python setup.py py2app -A")
    os.system("rm setup.py")

def setPath():
    global pathPy
    pathPy = tkFileDialog.askopenfilename()

def setIcon():
    global pathImg
    pathImg = tkFileDialog.askopenfilename()

# Window

root = Tk()
root.configure(bg=backgroundColor)
root.title("Py2App Client")

browseLabel = Label(root, text="Browse .py", bg=backgroundColor, fg=textColor)
browseLabel.pack(pady=labelPadY)
browse = Button(root, text="Browse", command=setPath, highlightbackground=backgroundColor)
browse.pack()

nameLabel = Label(root, text="Name your app", bg=backgroundColor, fg=textColor)
nameLabel.pack(pady=labelPadY)
nameTv = StringVar()
name = Entry(root, textvariable=nameTv, highlightbackground=backgroundColor)
name.pack()
nameTv.set("My App")
nameV = nameTv.get()

iconLabel = Label(root, text="Set icon", bg=backgroundColor, fg=textColor)
iconLabel.pack(pady=labelPadY)
icon = Button(root, text="Browse", command=setIcon, highlightbackground=backgroundColor)
icon.pack()

make = Button(root, text="Build my app", command=build, highlightbackground=backgroundColor)
make.pack(pady=submitPadY)

root.mainloop()
