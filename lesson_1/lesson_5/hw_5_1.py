"""1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

with open("data_file.txt", "w") as file_obj:
    p_string = ' '
    while p_string != '':
        p_string = input("Введите данные: ")
        file_obj.writelines(f'{p_string}\n')