# radio button-- can only select one from a group

from tkinter import *

food = ['pizza', 'hamburger', 'hotdog']

def order():
    if(x.get()==0):
        print('you ordered pizza')
    elif(x.get()==1):
        print('you ordered hamburger')
    elif(x.get()==2):
        print('you ordered hotdog')
    else:
        print('hakdog')

window = Tk()

pizzaImage = PhotoImage(file='')
hamburgerImage = PhotoImage(file='')
hotdogImage = PhotoImage(file='')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # adds txt to radio buttons
                              variable=x,  # groups radio buttons together
                              value=index,  # assigns the radiobtn a different value
                              padx=20,
                              font=('Impact',50),
                              image=foodImages[index],  # adds images
                              compound='left',  # adds image and text
                              command=order  # def function
                              # indicatoron=0  # eliminates circle indicators
                              # width=375  # sets width of radio buttons
                              )


    radiobutton.pack(anchor=W)  # west, east, chuchcu

window.mainloop()