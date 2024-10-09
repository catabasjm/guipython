from tkinter import *

def doSomething(event):
    #print("You pressed: " + event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>",doSomething)  # (event, function)
# <Return>--Enter <Up> <Down> w,a,s,d

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()