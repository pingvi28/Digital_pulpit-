def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiple(a, b):
    return a * b


def divide(a, b):
    return a / b


def foo_out(a, flag):
    def foo_inside(b):
        return a*b

    def foo_outside(b):
        return a+b

    return foo_inside if flag else foo_outside


if __name__ == "__main__": # если импортируем calc, этот участок кода не вызывается, иначе при запуске его напрямую
    # выводится эта строчка
    print("Запуск напрямую")

