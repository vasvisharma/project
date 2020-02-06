#!/usr/bin/env python
# coding: utf-8

# In[40]:


import tkinter
from tkinter import *
import tkinter.filedialog


from tkinter import messagebox
import tkinter.colorchooser
from tkinter.colorchooser import askcolor

import datetime

import webbrowser

from tkinter.filedialog import askopenfilename, asksaveasfilename



def newFile():
    root.title("Untitled")
    file=None
    text.delete(1.0,END) 
    

def line1():

    lin = "_" * 60

    text.insert(INSERT,lin)

    
def line2():

    lin = "*" * 120

    text.insert(INSERT,lin)
    
def line3():

    lin = "~" * 60

    text.insert(INSERT,lin)
    
def date():

    data = datetime.date.today()

    text.insert(INSERT,data)

   
def normal():

    text.config(font = ("Arial", 10))



def bold():

    text.config(font = ("Arial", 10, "bold"))



def underline():

    text.config(font = ("Arial", 10, "underline"))



def italic():

    text.config(font = ("Arial",10,"italic"))

    

def font():

    (triple,color) = askcolor()

    if color:

       text.config(foreground=color)
    



def kill():

    root.destroy()



def about():

    pass



def opn():

    text.delete(1.0 , END)

    file = open(askopenfilename() , 'r')

    if file != '':

        txt = file.read()

        text.insert(INSERT,txt)

    else:

        pass

    

def save():

    filename = asksaveasfilename()

    if filename:

        alltext = text.get(1.0, END)                      

        open(filename, 'w').write(alltext) 

def cut(): 
    root.focus_get().event_generate("<<Cut>>") 


def copy():

    text.clipboard_clear()

    text.clipboard_append(text.selection_get()) 



def paste():

    try:

        teext = text.selection_get(selection='CLIPBOARD')

        text.insert(INSERT, teext)

    except:

        tkMessageBox.showerror("Error")



def clear():

    sel = text.get(SEL_FIRST, SEL_LAST)

    text.delete(SEL_FIRST, SEL_LAST)



def clearall():

    text.delete(1.0 , END)



def background():

    (triple,color) = askcolor()

    if color:

       text.config(background=color)

       

def about():

    ab = Toplevel(root)

    txt = " This is a notepad editor version 5.2            "

    la = Label(ab,text=txt,foreground='blue')

    la.pack()

    

def web():

    webbrowser.open('http://www.google.com')


def FontCourier():
    global text
    text.config(font="Courier")
    
def helvetica():
    global text
    text.config(font="Helvetica")
    
def sanserif():
    global text
    text.config(font="Comic Sans MS")


root = Tk()
thisTextArea=Text(root)
root.title("notepad")

menu = Menu(root)



filemenu = Menu(root,tearoff=0)

root.config(menu = menu)

menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="open", command=opn)
filemenu.add_command(label="save", command=save)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=kill)



modmenu = Menu(root,tearoff=0)

menu.add_cascade(label="Edit",menu = modmenu)
modmenu.add_command(label="Cut", command = cut)

modmenu.add_command(label="Copy", command = copy)

modmenu.add_command(label="paste", command=paste)

modmenu.add_separator()

modmenu.add_command(label = "Clear", command = clear)

modmenu.add_command(label = "Clear all", command = clearall)





insmenu = Menu(root,tearoff=0)

menu.add_cascade(label="Insert",menu= insmenu)

insmenu.add_command(label="Date",command=date)

insmenu.add_command(label="Normal-Line",command=line1)
insmenu.add_command(label="Star-Line",command=line2)
insmenu.add_command(label="Stylish-Line",command=line3)





        

formatmenu = Menu(menu,tearoff=0)

menu.add_cascade(label="Format",menu = formatmenu)

formatmenu.add_cascade(label="Font color", command = font)

formatmenu.add_separator()

formatmenu.add_radiobutton(label='Normal',command=normal)

formatmenu.add_radiobutton(label='Bold',command=bold)

formatmenu.add_radiobutton(label='Underline',command=underline)

formatmenu.add_radiobutton(label='Italics',command=italic)

formatmenu.add_command(label="Background", command=background)
formatmenu.add_separator()
formatmenu.add_radiobutton(label="font style:Courier",command=FontCourier)
formatmenu.add_radiobutton(label="font style:Helvetica",command=helvetica)
formatmenu.add_radiobutton(label="font style: Comic Sans MS",command=sanserif)


helpmenu = Menu(menu,tearoff=0)

menu.add_cascade(label="more", menu=helpmenu)

helpmenu.add_command(label="About", command=about)


text = Text(root, height=100, width=100, font = ("Arial", 10))




scroll = Scrollbar(root, command=text.yview)

scroll.config(command=text.yview)                  

text.config(yscrollcommand=scroll.set)           

scroll.pack(side=RIGHT, fill=Y)

text.pack()



root.resizable(0,0)

root.mainloop()


# In[36]:


from tkinter import *
master = Tk() 
#Label(master, text='First Name').grid(row=0) 
#Label(master, text='Last Name').grid(row=1) 
e1 = Entry(master) 
#e2 = Entry(master) 
e1.grid(row=0, column=1) 
#e2.grid(row=1, column=1) 
mainloop() 


# In[ ]:




