import random
from tkinter import *
import tkinter as tk
from random import randint
root = Tk()
root.geometry("350x450")
root.iconbitmap(default="iconeTama.ico")
root.configure(background="#ffb6c1")

status = random.randint(1, 10)

v1 = "Dino-idle.gif"


imagem = PhotoImage(file="C:/Users/Andrey/PycharmProjects/Tamagochi_Interface/rex_1.png")


class DinoPet():
    def __init__(self, master=None):
        self.label1 = Frame(master)
        self.label1 = tk.Label(root, image=imagem, background="#000000")
        self.label1.imagem = imagem
        self.label1.pack()

        self.status = Frame(master)
        self.status.place(x=45, y=180)

        self.label2 = Frame(master)
        self.label2.place(x=80, y=220)

        self.label3 = Frame(master)
        self.label3.place(x=150, y=220)

        self.label4 = Frame(master)
        self.label4.place(x=210, y=220)

        self.label5 = Frame(master)
        self.label5.place(x=45, y=280)

        self.label6 = Frame(master)
        self.label6.place(x=125, y=280)

        self.label7 = Frame(master)
        self.label7.place(x=225, y=280)

        self.label8 = Frame(master)
        self.label8.place(x=125, y=350)


#inserindo informações na interface
        self.msg = Label(self.status, padx=6, pady=10, background="#000000",fg="#ffffff")
        self.msg["text"] = ""
        self.msg.pack()

        self.contador1 = status
        self.fome = Label(self.label2, padx=6, pady=10, background="#FF0000")
        self.fome["text"] = "Fome"
        self.fome["padx"] = 10
        self.fome.pack()

        self.contador2 = status
        self.humor = Label(self.label3,padx=6, pady=10, background="#FF0000")
        self.humor["text"] = "Triste"
        self.humor.pack()

        self.contador3 = 10
        self.energia = Label(self.label4, padx=6, pady=10, background="#008000")
        self.energia["text"] = "Energia"
        self.energia.pack()

        self.comer = Button(self.label5, padx=10, pady=15, background="#FF0000", fg="#FFFFFF")
        self.comer["text"] = "Food"
        self.comer["font"] = ("Arial", "12", "bold")
        self.comer["command"] = self.Comer
        self.comer.pack()

        self.brincar = Button(self.label6, padx=10, pady=15, background="#ffc222", fg="#FFFFFF")
        self.brincar["text"] = "Brincar"
        self.brincar["font"] = ("Arial", "12", "bold")
        self.brincar["command"] = self.Brincar
        self.brincar.pack()

        self.dormir = Button(self.label7, padx=10, pady=15, background="#FFFFFF", fg="#000000")
        self.dormir["text"] = "Dormir"
        self.dormir["font"] = ("Arial", "12", "bold")
        self.dormir["command"] = self.Dormir
        self.dormir.pack()

        self.sair = Button(self.label8, padx=10, pady=15, background="#000000", fg="#FFFFFF")
        self.sair["text"] = "    Sair   "
        self.sair["font"] = ("Arial", "12", "bold")
        self.sair["command"] = root.destroy
        self.sair.pack()

#definindo ações nos botoes
    def Comer(self):
        self.msg["text"] = ""
        self.contador1 += 1
        self.fome["text"] = f"     {self.contador1}   "
        if self.contador1 >= 5:
            self.fome["text"] = "Cheio"
            self.fome["background"] = "#008000"
        elif self.contador1 <5:
            self.fome["background"] = "#FF0000"


    def Brincar(self):
        self.msg["text"] = ""
        self.contador2 += 1
        self.humor["text"] = f"     {self.contador2}   "
        self.contador1 -= 1
        self.contador3 -= 2
        if self.contador3 < 2:
            self.energia["text"] = "Sono"
            self.energia["background"] = "#FF0000"
        elif self.contador3 < 0:
            self.contador3 += 1
        else:
            self.energia["text"] = "Energia"
            self.energia["background"] = "#008000"

        if self.contador1 >= 5:
            self.fome["text"] = "Cheio"
        elif self.contador1 < 0:
            self.contador1 += 1
            self.fome["text"] = "Fome"
            self.fome["background"] = "#FF0000"
        else:
            self.fome["text"] = "Fome"
            self.fome["background"] = "#FF0000"

        if self.contador2 >= 7:
            self.humor["text"] = "Feliz"
            self.humor["background"] = "#008000"

    def Dormir(self):
        self.msg["text"] = "Dormindo"
        self.contador3 += 1
        self.contador2 -= 1
        self.contador1 -= 1

        if self.contador3 >= 7:
            self.energia["text"] = "Energia"
            self.energia["background"] = "#00F000"

        if self.contador1 >= 5:
            self.fome["text"]="Cheio"
        elif self.contador1 < 0:
            self.contador1 += 1
            self.fome["text"] = "Fome"
            self.fome["background"] = "#FF0000"
        else:
            self.fome["text"] = "Fome"
            self.fome["background"] = "#FF0000"

        if self.contador2 >= 7:
            self.humor["text"] = "Feliz"
            self.humor["background"] = "#008000"
        elif self.contador2<0:
            self.contador2 +=1
            self.humor["text"] = "Triste"
            self.humor["background"] = "#FF0000"
        else:
            self.humor["text"] = "Triste"
            self.humor["background"] = "#FF0000"




DinoPet(root)
root.mainloop()
