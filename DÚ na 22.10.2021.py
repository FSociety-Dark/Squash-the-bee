from tkinter import *
from random import choice
import os

def cls():
    input("Čakám...")
    os.system('cls')

def uloha1():
    root = Tk()
    root.title("The Worm")
# ------ Variables ------- #
    can_width =                          400 #  <<-----------------------<<----------- ! Zmena dĺžky canvasu !
    height,border,side,add = int(can_width/3),int(can_width/15),10,5
    position = border
    color = ["#fd79a8","#fab1a0","#e17055","#ff7675","#ea8685","#f78fb3","#e66767","#f8a5c2","#f3a683"]
# ------ Canvas ------- #
    can = Canvas(root, width=can_width, height=int(can_width*0.5), bg="#2c3e50", bd=-2)
    can.pack()
    print("Canvas bol vytvorený. Prvý variable rozťahuje canvas = dlhšia postupnosť")
    Label(text="Pripomínalo mi to červíka... :D",font=("Arial",16,"bold"),bg="#2c3e50",fg="white").place(relx=0.5,rely=0.15,anchor=CENTER)
# ------ Logic ------- #
    while True:
        if position+side+border < can_width:
            head = can.create_rectangle(position, height, position+side, height-side, fill=choice(color),outline="")
            position += side
            side += add
        else:
            can.itemconfig(head, fill="#eb4d4b",outline="#c23616",width=2)
            coords = can.coords(head)
            position -= side
            side -= add
            x1,x2,y1,y2 = coords[0],coords[2],coords[1],coords[3]

            # Orientation
            # x1,x2 = left,right
            # y1,y2 = top,down
            # + = down, - = up

            can.create_line(x1+(side/3),y1+(side/10),x1+(side/4),y1-(side/2.5), width=side/10, fill="#c0392b")
            can.create_line(x2-(side/3),y1+(side/10),x2-(side/4),y1-(side/2.5), width=side/10, fill="#c0392b")
            can.create_arc(x1+(side/4),y1+(side/2),x2-(side/4),y2-(side/10),extent=-180,fill="red",outline="")
            can.create_oval(x1+(side/3.5),y1+(side/5),x1+(side/2.4),y1+(side/2.6),fill="white",outline="black",width=2)
            can.create_oval(x2-(side/3.5),y1+(side/5),x2-(side/2.4),y1+(side/2.6),fill="white",outline="black",width=2)
            can.create_oval(x1+(side/2.9),y1+(side/5),x1+(side/2.5),y1+(side/2.6),fill="black")
            can.create_oval(x2-(side/3.5),y1+(side/5),x2-(side/2.8),y1+(side/2.6),fill="black")
            break

    root.mainloop()
uloha1()

def uloha2():
    pass




uloha2()