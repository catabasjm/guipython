# canvas =  widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
#canvas.create_line(0,0,500,500,fill="blue",width=5)  # topleft to right bottom
#canvas.create_line(0,500,500,0,fill="red",width=5)  #topright to left bottom
#canvas.create_rectangle(100,50,500,250,fill="purple")  # left, top, right, bottom

#points = [250,0,500,500,0,500]  # x,y,x,y,x,y
#canvas.create_polygon(points,fill="yellow",outline="black",width=5)

canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,width=5)  # top, left, height, width, start=degrees(counterclockwise)
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill="white",width=10)  # width makes line thicker (x,y,x,y)
canvas.pack()

window.mainloop()