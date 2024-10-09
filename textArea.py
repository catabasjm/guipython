# text widget = functions like a text area, you can enter multiple lines of text
from tkinter import *

def submit():
    input = text.get("1.0",END)  # 1.0--means first line
    print(input)

window = Tk()
text = Text(window,
            bg="light yellow",
            font=("Ink Free",25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="#9d03fc")
text.pack()

button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()