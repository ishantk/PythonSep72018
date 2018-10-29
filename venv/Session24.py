from tkinter import *

def show():
    print("This is show")

def exit():
    print("This is exit")

# A GUI Object i.e. a Window
window = Tk()

# Add Menu in UI
menu = Menu(window)
window.config(menu=menu)

fMenu = Menu(menu)
menu.add_cascade(label="File", menu=fMenu)

fMenu.add_command(label="New", command=show)
fMenu.add_command(label="Open")
fMenu.add_command(label="Save")
fMenu.add_command(label="Exit", command=exit)

fEdit = Menu(menu)
menu.add_cascade(label="Edit", menu=fEdit)

fEdit.add_command(label="Cut")
fEdit.add_command(label="Copy")
fEdit.add_command(label="Paste")

fHelp = Menu(menu)
menu.add_cascade(label="Help", menu=fHelp)

lblWelcome = Label(window, text="Welcome to Auribises")
lblWelcome.pack()

btnSubmit = Button(window, text="Submit", command=show)
btnSubmit.pack()

window.mainloop()

# Application -> Create a Notepad with Menu Items