import os
from tkinter import *
from random import choice

def cls():
    input("Čakám...")
    os.system('cls')

def uloha1():
    print(">>> Zadanie: vypočítaj celú časť z odmocniny zo zadaného čísla.")
    n = int(input("Zadajte číslo: "))
    print(f"Výsledok je: {int(n**(0.5))}")
    cls()
#uloha1()

def uloha2():
    print(">>> Zadanie: vypíš súčet všetkých čísel zo zadaného intervalu.")
    ints,x = sorted([int(j) for j in input("Zadajte hranice intervalu, rozdelené medzerou: ").split(" ")]),0
    while ints[0] <= ints[1]:
        x += ints[0]
        ints[0] += 1
    print(f"Výsledok je: {x}")
    cls()
#uloha2()

def uloha3():
    print(">>> Zadanie: vypíš počet čísel delitelných delitelom v zadanom intervale.")
    ints = [int(j) for j in input("Zadajtete vstup, formát [delitel interval koniec-intervalu]: ").split(" ")]
    divisor,ints,x = ints[0],sorted([ints[1],ints[2]]),0
    while ints[0] < ints[1]:
        if ints[0] % divisor == 0: x += 1
        ints[0] += 1
    print(x)
    cls()
#uloha3()

def uloha4():
    print(">>> Zadanie: vypíš cifry zadaného čísla pospiatku, potom vypíš ich ciferný súčet.")
    n,x,cs = int(input("Zadajte číslo: ")),0,0
    n = [int(a) for a in str(n)]
    n.reverse()
    while x < len(n):
        print(n[x])
        cs += n[x]
        x += 1

    # Našiel som požadované riešenie, ale nefungovalo pre všetky vstupy (napr. číslo: 1234. Výsledkom bolo číslo 9, nie 10.
    # Preto som použil vlastné riešenie, ktoré by malo fungovať pre všetky kladné celé čísla :)
    """while x < n:
        y = n % 10
        cs += y
        print(y)
        n //= 10
        x += 1""" 

    print(f"Výsledok je: {cs}")
    cls()
#uloha4()

# --------- Úloha č.5 --------- #

def randcolor():
    chars=["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    cc="#"
    for i in range(6):
        cc += choice(chars)
    return cc

def handle_entry_click(event):
    entry.delete(0, END)

def uloha5(event):
    n,x,y,z = [int(a) for a in entry.get()],775,50,1
    while z <= len(n):
        can.create_rectangle(x,y,x-40,y+70,fill=randcolor(),outline="")
        can.create_text(x-17,y+37,text=str(n[len(n)-z]), font="Arial 45 bold", fill="black")
        can.create_text(x-20,y+35,text=str(n[len(n)-z]), font="Arial 40 bold", fill="white")
        x -= 50
        z += 1

def create_canvas():
    print(">>> Zadanie: zadané číslo zobraz na canvase od prava do ľava, orámované obdĺžnikom.\nVytvoril sa canvas, číslo zadajtete do entry :)")
    global entry
    global can
    rt = Tk()
    can = Canvas(rt, width=800, height=200, bg="#2c3e50", bd=-2)
    can.pack()
    entry = Entry(bg="#34495e",justify=CENTER, font="Arial 14 bold",width=40)
    entry.insert(0, "> Zadajte číslo a stlačte enter <")
    entry.bind("<1>", handle_entry_click)
    entry.bind("<Return>", uloha5)
    entry.place(rely=0.9, relx=0.5, anchor=CENTER)
    rt.mainloop()
create_canvas()