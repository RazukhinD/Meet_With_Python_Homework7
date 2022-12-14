import view
import model


def input_fist():
    number = view.input_expression()
    model.set_first(number)

def input_second():
    while True:
        number= view.input_expression()
        if model.get_oper()=='/' and number ==0:
            view.print_division_by_zero()
        else:
            model.set_second(number)
            break

def input_operation():
    oper=view.input_operation()
    model.set_operation(oper)

def solution():
    oper = model.get_oper()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper=='*':
        model.mult()
    elif oper == '/':
        model.division()
    result_string=f'{model.get_first()}{model.get_oper()}{model.get_second()}={model.get_result()}'
    view.print_to_console(result_string)
    model.set_first(model.get_result())


def start():
    input_fist()
    while True:
        input_operation()
        if model.get_oper()=='=':
            view.log_off()
            break
        input_second()
        if solution():
            break