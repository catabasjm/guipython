from tkinter import *

def click():
    print('you clicked the button!')

window = Tk()   # instantiate an instance of a window
window.geometry("1000x600")  # width by height
window.title("Jhana's GUI")

# icon = PhotoImage(file='')  # add image logo
# window.iconphoto(True, icon)  # to set the image in the topleft icon bar
window.config(background="#dd88f7")  # change bg color

photo = PhotoImage(file='bear.png')
label = Label(window,text='Welcome!',
              font=('Times',50,'bold'),
              fg='#d3d929',   # font color
              bg='black',   # font bg color
              relief=RAISED,  # border style,  ex. SUNKEN
              bd=10,  # border size
              padx=30,  # padding of sides
              pady=20,  # padding above and below
              image=photo,  # to show the photo in the window
              compound='top')  # for the text to show(since txt is overrided by the image)
                                # set to top, left, right or bottom of where image is

label.pack()  # places label at the top center of window
# label.place(x=0,y=0)  # places label at coordinates

# photo_btn = PhotoImage(file='.png')
button = Button(window,
                text='Click Here',
                command=click,  # it is without the (), it is called callback
                font=("Comic Sans", 15),
                fg='black',
                bg='yellow',
                activeforeground='green',  # this is the font color when btn is clicked
                activebackground='black',)
                # image=photo_btn,
                # compound=''  where you want the image of the btn, top, left, right, bottom
                # to disable button, state=DISABLED / ACTIVE

button.pack()
window.mainloop()  # place window on screen

