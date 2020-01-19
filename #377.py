#Description:
#You have a 2-dimensional rectangular crate of size X by Y, and a bunch of boxes,
#each of size x by y. The dimensions are all positive integers.
#Given X, Y, x, and y, determine how many boxes can fit into a single crate if
#they have to be placed so that the x-axis of the boxes is aligned with the
#x-axis of the crate, and the y-axis of the boxes is aligned with the y-axis of
#the crate. That is, you can't rotate the boxes. The best you can do is to build
#a rectangle of boxes as large as possible in each dimension.

#For instance, if the crate is size X = 25 by Y = 18, and the boxes are size
#x = 6 by y = 5, then the answer is 12. You can fit 4 boxes along the x-axis
#(because 6*4 <= 25), and 3 boxes along the y-axis (because 5*3 <= 18), so in
#total you can fit 4*3 = 12 boxes in a rectangle.


from tkinter import *


def callback(event):
    InA=str(Inp1.get()).replace(',',' ')
    InB=str(Inp2.get()).replace(',',' ')
    A=list(map(int,InA.split()))
    B=list(map(int,InB.split()))
    a=A[0]//B[0]
    b=A[1]//B[1]
    print(a*b)
    L3.config(text="Answer: "+str(a*b))

master = Tk()
master.title("Reddit challenge #377")
master.geometry("350x130")

L1=Label(master, text="Input box size (coma or space separated)\n")
L1.grid(row=0)
Inp1=Entry(master)
Inp1.grid(row=0,column=1)
Inp1.focus_set()

L2=Label(master, text="Input crate size (coma or space separated)\n")
L2.grid(row=1)
Inp2=Entry(master)
Inp2.grid(row=1,column=1)

But=Button(master, text='Calculate')
But.grid(row=2)
But.bind('<Button-1>',callback)

L3=Label(master, text="Answer: ")
L3.grid(row=3)
mainloop()
