from tkinter import *

# text box that accepts a single line of user input
def submit():
    user = entry.get()
    print(user)
 #  entry.config(state=DISABLED)  # after submitting it will not let the user submit again

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=('Arial', 50),
              show='*')  # this will hide the txt u r entering

# entry.insert(0, 'Enter name')
entry.pack(side=LEFT)


submit_button = Button(window, text='submit',command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text='delete',command=delete)
delete_button.pack(side=RIGHT)

backspace = Button(window, text='backspace',command=backspace)
backspace.pack(side=RIGHT)

window.mainloop()