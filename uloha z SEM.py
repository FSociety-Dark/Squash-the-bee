import tkinter
root = tkinter.Tk()
canvas = tkinter.Canvas(root, bg='white', width=800, height=200)
canvas.pack()

n = 5
x = 10

# Varianta 1
for i in range(n):
    canvas.create_rectangle(x,70,x+30,130,fill="pink")
    x += 35
    canvas.create_rectangle(x,70,x+30,130,fill="green")
    x += 35


"""
# Varianta 2
for i in range(n):
    canvas.create_rectangle(x,70,x+30,130,fill="pink")
    x += 35
    canvas.create_rectangle(x,70,x+30,130,fill="green")
    x += 35
    canvas.create_rectangle(x,70,x+30,130,fill="red")
    x += 35
"""

"""
# Varianta 3
for i in range(n):
    canvas.create_rectangle(x,70,x+30,130,fill="pink")
    x += 35
    canvas.create_rectangle(x,70,x+30,130,fill="green")
    x += 35
    canvas.create_rectangle(x,70,x+30,130,fill="red")
    x += 35
    canvas.create_rectangle(x,70,x+30,130,fill="yellow")
    x += 35
"""

"""
# Varianta 4
for i in range(n):
    canvas.create_rectangle(x,70,x+30,130,fill="pink")
    x += 35
    canvas.create_rectangle(x,70,x+30,130,fill="green")
    x += 35
    canvas.create_rectangle(x,70,x+30,130,fill="red")
    x += 35
    canvas.create_rectangle(x,70,x+30,130,fill="yellow")
    x += 35
    canvas.create_rectangle(x,70,x+30,130,fill="blue")
    x += 35
"""

root.mainloop()