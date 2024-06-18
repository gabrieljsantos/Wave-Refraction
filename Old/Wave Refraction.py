from tkinter import *
from tkinter import ttk
import tkinter as tk

simulation = tk.Tk()
simulation.geometry('800x550')
simulation.title('Wave Refraction')


w = Canvas(simulation, width=800, height=500)
w.pack()
"""
def Estrela():
    points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
    w.create_polygon(points, outline="gray", fill=c2.get(), width=2)
"""
"""
def Casa():
    points = [96, 336, 288, 336, 288, 192, 192, 96, 96, 192, 96, 336]
    porta = [163.2, 336, 163.2, 278.4, 211.2, 278.4, 211.2, 336, 163.2, 336]
    telhado = [295,192,192,96,88,192]
    w.create_polygon(points, outline="black", fill=c1.get(), width=3)
    w.create_polygon(porta, outline="black", fill='brown', width=3)
    w.create_oval(170, 200, 210, 240, outline="brown", fill="blue", width=3)
    w.create_polygon(telhado, outline = "brown", fill="red", width=3)
"""
def wave():
    points = [0,338,600,338]
    w.create_polygon(points, outline="green", fill='yellow', width=5)
def Refraction1():
    position = 100
    angulo = 0


#c1 = ttk.Combobox(master, values=('Yellow','Blue', 'Teal' ,'Brown','Orange','Gold', 'Tan', 'Purple', 'Olive', 'Aqua'),width=10)
#c1.place(x=550, y=110)
#c1.set("Yellow")
#Label_7 = tk.Label(master, text="House Color",font=('Arial',11),padx=0).place(x=550, y=80)

#c2 = ttk.Combobox(master, values=('Yellow','Violet','Blue','Brown','Orange','Gray', 'Salmon', 'Pink', 'OliveDrab'),width=10)
#c2.place(x=550, y=220)
#c2.set("Blue")
#Label_8 = tk.Label(master, text="Star Color",font=('Arial',11),padx=0).place(x=550, y=190)


#tk.Button(master, text='Star',font=('Arial',14), command=Estrela).place(x=80, y=440)
#tk.Button(master, text='House',font=('Arial',14), command=Casa).place(x=140, y=440)
#tk.Button(master, text='Grass',font=('Arial',14), command=Grama).place(x=220, y=440)

wave()
mainloop()