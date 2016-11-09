from Tkinter import *
#import Tkinter as tk
#import pyHook, pythoncom, os, httplib, urllib, getpass, shutil, sys
gig = Tk()

gig.title('v 0.0.1')

photo = PhotoImage(file="cool.gif")
labelforimg = Label(image=photo)
labelforimg.pack(side=BOTTOM, fill=X)
labelforimg.grid(column=25, row=6)


usernamelabel = Label(gig, text='A line for test', font=("After Disaster", 23))
usernamelabel.pack(side=TOP, fill=X)
usernamelabel.grid(column=25, row=1, sticky=N)


usernamelabel3 = Label(gig, text='', font=("After Disaster", 23))
usernamelabel3.pack(side=TOP, fill=X)
usernamelabel3.grid(column=25, row=3, sticky=N)

var = StringVar()
var.set('xxxxxxxxxx')
enterusernpcname = Entry(gig, textvariable=var,)
enterusernpcname.pack(side=TOP, fill=X)
enterusernpcname.grid(column=25, row=2, sticky=N)

madeby2 = Label(gig, text='Made by sudoXch', font=("After Disaster", 21))
madeby2.pack(side=LEFT, fill=X)
madeby2.grid(column=25, row=5, sticky=N)

start = Button(gig, text='Start', bg='red')
start.pack(side=TOP, fill=X)
start.grid(column=25, row=4, sticky=N)

#gig.geometry('{}x{}'.format('140', '80'))

#root = Tk()
menuforset = Menu(gig)
gig.config(menu=menuforset)

submenuforset = Menu(menuforset, tearoff=0)
menuforset.add_cascade(label='Options', menu=submenuforset)
submenuforset.add_command(label='About us')
submenuforset.add_separator()
submenuforset.add_command(label='Exit')

editmenu = Menu(menuforset, tearoff=0)
menuforset.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Redo')


#statusforuser = Label(gig, text='Preparing to do nothing....', bd=1, relief=SUNKEN)
#statusforuser.pack(side=BOTTOM)


gig.geometry('{}x{}'.format('180', '286'))
gig.resizable(width=False, height=False)
gig.mainloop()
