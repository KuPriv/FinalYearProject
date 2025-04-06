import os
from pathlib import Path

from read_from_file import get_data_from_all_files, get_data_from_one_file


def UI():
    path = 'generated_files'

    n = int(input('Матрицы какой размерности берем? : '))
    if Path(path + f'/{n}').exists():
        get_data(n)
    else:
        print("Неверный ввод. Введите число папки, которая существует")
        list_of_dirs = os.listdir(path)
        list_of_dirs = [int(x) for x in list_of_dirs]
        print('Существующие папки:')
        print(sorted(list_of_dirs))
        UI()


def get_data(n) -> list | None:
    our_way = int(input('Читаем все файлы или один?\n1 - Все\n2 - Один\nВведите цифру: '))
    if our_way == 1:
        return get_data_from_all_files(n)
    elif our_way == 2:
        return read_one_file(n)


def read_one_file(n) -> list | None:
    file_n = int(input("Какой из файлов хотите прочитать? Число от 1 до 5: "))
    if file_n in (1, 2, 3, 4, 5):
        return get_data_from_one_file(n, file_n)
    else:
        print('Неверный ввод.')
        read_one_file(n)


def main() -> None:
    UI()


if __name__ == "__main__":
    main()
