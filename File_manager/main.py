# Файловый менеджер на питоне, 2 задание
# Кашаповаа Диляра, 11-001, 19.10
import sys
import os

# просмотр теĸущей папĸи
def pwd():
    print(os.getcwd())


# переход в другую папĸу
def cd(filename):
    try:
        os.chdir(filename)
    except OSError:
        print("Incorrect file path")


# Создание нового файла == new (доп параметр для создания сразу содержимого)
def touch(filename, text=None):
    # открыли файл для чтения и сохранили в переменную f
    with open(filename, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# вывод содержимого файла
def cat(filepath):
    if os.path.isfile(filepath):
        file = filepath
    else:
        file = os.path.join(os.getcwd(), filepath)
    try:
        with open(file, "r") as f:
            for line in f:
                print(line)
    except FileNotFoundError:
        print("Can't find file")


# Создание папки
def create_folder(filename):
    try:
        os.mkdir(filename)
    except FileExistsError:
        print("Такая папка уже есть")


def ls(file_only=True):
    resul = os.listdir()
    if file_only:
        resul = [f for f in resul if os.path.isfile(f)]
    print(*resul)


def rm(filename):
    try:
        if os.path.isdir(filename):
            os.rmdir(filename)
        else:
            os.remove(filename)
    except FileNotFoundError:
        print("Can't find file")


if __name__ == '__main__':
    while True:
        command = str(input(os.getcwd() + "> "))

        # разделение на команду и путь
        command = command.split(" ")

        if command[0] == "pwd":
            pwd()

        if command[0] == "touch":
            try:
                touch(command[1])
            except IndexError:
                print("You didn't show the way [cd *file path*]")

        if command[0] == "cd":
            try:
                cd(command[1])
            except IndexError:
                print("You didn't show the way [cd *file path*]")

        if command[0] == "cat":
            try:
                cat(command[1])
            except IndexError:
                print("You didn't show the way [cat *file path*]")

        if command[0] == "ls":
            ls()

        if command[0] == "dir":
            ls(False)

        if command[0] == "rm":
            try:
                rm(command[1])
            except IndexError:
                print("You didn't show the way [rm *file path*]")

        if command[0] == "exit":
            sys.exit()
