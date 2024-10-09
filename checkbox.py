from tkinter import *

def display():
    if(x.get()):
        print('you agree')
    else:
        print('you dont agree')

window = Tk()

# x = IntVar()  # returns 1 0r 0 if(x.get() == 1)
# x = StringVar() returns string if(x.get() == "YES")
x = BooleanVar()  # returns True or False

# checkbox_image  = PhotoImage(file='.png')

check_box = Checkbutton(window,
                        text='Agree',
                        variable=x,
                        onvalue=True,
                        offvalue=False,
                        command=display,
                        font=('Arial',20))
                       # fg='',
                       # bg='',
                       # activebackground='',
                       # activeforeground='',
                       # padx=25,
                       # pady=10,
                       # image=checkbox_image,
                       # compound='left')

# you can add image into the Checkbutton()

check_box.pack()

window.mainloop()