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
    nameV = nameTv.get()
    versionV = versionTv.get()
    identifierV = identifierTv.get()
    descV = descTv.get()
    copyrightV = copyrightTv.get()

    setup = "from setuptools import setup\n\nAPP = ['"+pathPy+"']\nDATA_FILES = []\nOPTIONS = {'argv_emulation': True,\n\t'iconfile': '"+pathImg+"',\n\t'plist': {\n\n\t\t'CFBundleName': '"+nameV+"',\n\t\t'CFBundleDisplayName': '"+nameV+"',\n\t\t'CFBundleGetInfoString': '"+descV+"',\n\t\t'CFBundleIdentifier': '"+identifierV+"',\n\t\t'CFBundleVersion': '"+versionV+"',\n\t\t'CFBundleShortVersionString': '"+versionV+"',\n\t\t'NSHumanReadableCopyright': '"+copyrightV+"'\n\t}\n}\nsetup(\n\tapp=APP,\n\tdata_files=DATA_FILES,\n\toptions={'py2app': OPTIONS},\n\tsetup_requires=['py2app']\n)"

    setupFile = open("setup.py","w")
    setupFile.write(setup)
    setupFile.close()
    pwV = pwTv.get()
    os.system("echo '"+pwV+"' | sudo -S python setup.py py2app -A")
    os.system("rm setup.py")

def setPath():
    global pathPy
    pathPy = tkFileDialog.askopenfilename(filetypes=[("Python",".py")])

def setIcon():
    global pathImg
    pathImg = tkFileDialog.askopenfilename(filetypes=[("Icon",".icns")])

# Window

root = Tk()
root.configure(bg=backgroundColor)
root.title("Py2App Client")

browseLabel = Label(root, text="Browse your main script (.py)", bg=backgroundColor, fg=textColor)
browseLabel.pack(pady=labelPadY)
browse = Button(root, text="Browse", command=setPath, highlightbackground=backgroundColor)
browse.pack()

nameLabel = Label(root, text="App name", bg=backgroundColor, fg=textColor)
nameLabel.pack(pady=labelPadY)
nameTv = StringVar()
name = Entry(root, textvariable=nameTv, highlightbackground=backgroundColor)
name.pack()

versionLabel = Label(root, text="Bundle version", bg=backgroundColor, fg=textColor)
versionLabel.pack(pady=labelPadY)
versionTv = StringVar()
version = Entry(root, textvariable=versionTv, highlightbackground=backgroundColor)
version.pack()

identifierLabel = Label(root, text="Bundle identifier", bg=backgroundColor, fg=textColor)
identifierLabel.pack(pady=labelPadY)
identifierTv = StringVar()
identifier = Entry(root, textvariable=identifierTv, highlightbackground=backgroundColor)
identifier.pack()

descLabel = Label(root, text="Bundle description", bg=backgroundColor, fg=textColor)
descLabel.pack(pady=labelPadY)
descTv = StringVar()
desc = Entry(root, textvariable=descTv, highlightbackground=backgroundColor)
desc.pack()

copyrightLabel = Label(root, text="Copyright", bg=backgroundColor, fg=textColor)
copyrightLabel.pack(pady=labelPadY)
copyrightTv = StringVar()
copyright = Entry(root, textvariable=copyrightTv, highlightbackground=backgroundColor)
copyright.pack()

iconLabel = Label(root, text="App icon (.icns)", bg=backgroundColor, fg=textColor)
iconLabel.pack(pady=labelPadY)
icon = Button(root, text="Browse", command=setIcon, highlightbackground=backgroundColor)
icon.pack()

pwLabel = Label(root, text="Password", bg=backgroundColor, fg=textColor)
pwLabel.pack(pady=labelPadY)
pwTv = StringVar()
pw = Entry(root, textvariable=pwTv, highlightbackground=backgroundColor, show="•")
pw.pack()

make = Button(root, text="Build my app", command=build, highlightbackground=backgroundColor)
make.pack(pady=submitPadY)

root.mainloop()
