def input_expression():
    while True:
        try:
            expression = input('Введите число или пример: ')
            return eval(expression)
        except:
            print('Ошибка')

def input_operation():
    while True:
        operation = input('Введите действие: ')
        if operation in ['+','-','*','/','=']:
            return operation
        else:
            print("Введи конкретную операцию")

def print_to_console(value_txt):
    print(value_txt)

def log_off():
    print('До свидания')

def print_division_by_zero():
    print('На ноль делить нельзя')
