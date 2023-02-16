import model
import view


def select(number):
    if number == 1:
        view.print_days(model.count_days())
    elif number == 2:
        view.print_number(model.calculate())
    elif number == 3:
        view.print_random_number(model.random_number())
