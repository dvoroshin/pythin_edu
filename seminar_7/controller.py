import view
import model_menu
from tkinter import *
from tkinter import ttk


def click_button_count_days():
    print()


def click_button_calculate():
    print()

def start():
    # view.create_menu()
    # select()

    root = Tk()
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    ttk.Label(frm, text='Калькулятор').grid(row=0, column=0)
    ttk.Button(frm, text='Вычислить сколько дней до начала лета', command=click_button_count_days).grid(
        row=1, column=1)
    ttk.Button(frm, text='Вычислить 2 + 2').grid(row=2, column=1)
    ttk.Button(frm, text='Рандомное число').grid(row=3, column=1)
    ttk.Button(frm, text='Выход').grid(row=0, column=1)

    root.mainloop()


def select():
    view.input_item()
    number_item = int(input())
    model_menu.select(number_item)


start()
