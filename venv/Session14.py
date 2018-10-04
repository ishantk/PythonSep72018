from tkinter import *


# User defined Function, Any Name of your choice
def onClick():
    name = entryName.get()
    price = entryPrice.get()

    print(name," : ",price)


# Tk is a window i.e. a GUI. Its kind of a frame with which user will interact !!
window = Tk()

#Textual View
lblTitle = Label(window, text="Add Products")

# pack is to add the Label into the window
lblTitle.pack()

lblName = Label(window, text="Enter Product's Name")
lblName.pack()

entryName = Entry(window)
entryName.pack()

lblPrice = Label(window, text="Enter Product's Price")
lblPrice.pack()

entryPrice = Entry(window)
entryPrice.pack()

btnAdd = Button(window,text="Add Product", command=onClick)
btnAdd.pack()

# Show the GUI
window.mainloop()