from tkinter import *
from tkinter import colorchooser  # this is a submodule

def click():
    color = colorchooser.askcolor()  # assign color to a variable
    colorHex = color[1]         # assigns element at index 1 to a variable
    window.config(bg=colorHex)  # change background color
#   window.config(bg=colorchooser.askcolor()[1]) # creates the same thing but only 1 line of code

window = Tk()
window.geometry("420x420")

button = Button(text='click me',command=click)
button.pack()

window.mainloop()