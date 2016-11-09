from Tkinter import *
import Tkinter
import tkMessageBox

def Link():
    print 'SHIT'

root = Tk()

menuforset = Menu(root)
root.config(menu=menuforset)

submenuforset = Menu(menuforset, tearoff=0)
menuforset.add_cascade(label='Options', menu=submenuforset)
submenuforset.add_command(label='About us', command=Link)
submenuforset.add_separator()
submenuforset.add_command(label='Exit', command=Link)

editmenu = Menu(menuforset, tearoff=0)
menuforset.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Redo', command=Link)


statusforuser = Label(root, text='Preparing to do nothing....', bd=1, relief=SUNKEN, anchor=W)
statusforuser.pack(side=BOTTOM, fill=X)


root.mainloop()