#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image, ImageTk
from Tkinter import Tk, Label

root = Tk()

image = Image.open('/media/artem/OS/Users/Артем/Desktop/Project/tankr.jpg')
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.pack()

root.mainloop()	
