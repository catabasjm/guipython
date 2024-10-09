# listbox = A listing of selectable text items within it's own container

def submit():

    food = []

    for index in listbox.curselection():   # adding or iterating multiple times
        food.insert(index,listbox.get(index))  # curselection()--current selection

    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())  # used when adding the size of the list box will adjust or change

def delete():
    for index in reversed(listbox.curselection()):  # deleting multiple items on list, the reversed()--deletes start at the last index
        listbox.delete(index)

    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg='#fcba03',
                  font=('Constantia',35),
                  width=12,
                  selectmode=MULTIPLE)  # can select multiple items for the list box
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())  # follows the size of the items in list box

entryBox = Entry(window)
entryBox.pack()

frame = Frame(window)
frame.pack()

submitButton = Button(frame,text="submit",command=submit)
submitButton.pack(side=LEFT)

addButton = Button(frame,text="add",command=add)
addButton.pack(side=LEFT)

deleteButton = Button(frame,text="delete",command=delete)
deleteButton.pack(side=LEFT)

window.mainloop()