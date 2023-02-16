import view
import model_menu
import tkinter

def start():
    view.create_menu()
    select()


def select():
    view.input_item()
    number_item = int(input())
    model_menu.select(number_item)
