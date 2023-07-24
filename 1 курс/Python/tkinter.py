from tkinter import *
from random import randint
n = randint(1, 100)

def Raschet(event):
    a = otvet.get()
    if a == '1' and n % 2 == 1:
        otvet2.set('Правильно!')
    elif a == '2' and n % 2 == 0:
        otvet2.set('Правильно!')
    else:
        otvet2.set('Неправильно!')

root = Tk()
root.geometry('500x120')
root.title('Чёт или нечет?')
root.resizable(False, False)

nadp1 = Label(root, text = 'Чёт или нечет?', font = 'Times 15 bold')
nadp2 = Label(root, text = 'Компьютер загадал целое число', font = 'Times 14')
ramka = Frame(root)
nadp3 = Label(ramka, text = 'Какое оно - четное (введите 2) или нечетное (введите 1)?', font = 'Arial 12')
otvet = StringVar()
pole1 = Entry(ramka, width = 5, textvariable = otvet)
otvet2 = StringVar()
pole2 = Entry(root, width = 20, textvariable = otvet2)

nadp1.pack()
nadp2.pack()
ramka.pack()
nadp3.grid(row = 0, column = 0)
pole1.grid(row = 0, column = 1)
pole2.pack()

pole1.bind('<Return>', Raschet)

root.mainloop()

root = Tk()
root.geometry('500x70')
root.title('Чет или нечет?')
root.resizable(False, False)

nadp4 = Label(root, text = 'Чёт или нечет?', font = 'Times 15 bold')
nadp5 = Label(root, text = 'Компьютер загадал:', font = 'Times 14')
