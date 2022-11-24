def find_max(*args):
    resul = -121210203
    for arg in args:
        if arg > resul:
            resul = arg

    return resul


print(f"Max in : {find_max(5, 3, 8, 10, 3)}")
