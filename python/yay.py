from math import sin, cos
from tkinter import *


x=0

def dot_print():
	global x

	y1=x*x*cos(x)
	y2=cos(x)*sin(x)*10

	cvs.create_oval(25*x+10,25*y1+100,25*x+10,25*y1+100,width=1,outline="red")
	cvs.create_oval(25*x+10,25*y2+100,25*x+10,25*y2+100,width=1,outline="blue")
	x=x+0.03

	root.after(5, dot_print)
root=Tk()
cvs = Canvas(root,width=600,height=200,bg="#fff")

cvs.pack()

cvs.create_line(10,0,10,200,width=2,arrow="both",fill="grey")

cvs.create_line(10,100,600,100,width=2,arrow="last",fill="grey")

dot_print()

root.mainloop()