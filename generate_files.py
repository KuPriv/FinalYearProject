import os
import sys
from pathlib import Path
from random import randint


def write_in_file():
    matrix_size: int = get_matrix_size()
    dir_name: str = 'generated_files/' + str(matrix_size)
    if Path(dir_name).exists():
        print('Папка уже существует. Не трожь.')
        sys.exit()
    os.makedirs(dir_name, exist_ok=True)
    count_of_files: int = 5
    type_of_matrix: int = choose_type_of_matrix()

    for number_of_file in range(count_of_files):
        try:
            with open(f'{dir_name}/{number_of_file + 1}.txt', mode='w+', encoding='utf-8') as file:
                # можно генерировать симметричную и ассиметричная матрицу
                matrix: list[list[int]] = generate_matrix(matrix_size, type_of_matrix)
                for line_index in range(len(matrix)):
                    line_to_str: list[str] = [str(n) for n in matrix[line_index]]
                    line_to_str: str = " ".join (line_to_str)

                    file.write(line_to_str + '\n')

        except Exception as e:
            print(f'Ошибка: {e}')


def get_matrix_size() -> int:
    n = int(input("Введите размерность: "))
    return n


def choose_type_of_matrix() -> int | None:
    info: int = type_selection_of_matrix()
    if info == 1:
        return 1
    elif info == 2:
        return 2
    else:
        print("Вводить только цифры '1' и '2' ")
        choose_type_of_matrix()


def generate_matrix(matrix_size: int, type_of_matrix: None | int) -> list[list[int]]:
    if type_of_matrix == 1:
        return generate_asymmetrical_matrix(matrix_size)
    else:
        return generate_symmetrical_matrix(matrix_size)


def type_selection_of_matrix() -> int:
    return int(input('Какой тип матрицы?\n1 - Ассиметричная\n2 - Симметричная\nВведите цифру: '))


def generate_asymmetrical_matrix(n: int) -> list[list[int]]:
    return [[randint(1, 101) if i != j else 0 for i in range(n)] for j in range(n)]


def generate_symmetrical_matrix(n: int) -> list[list[int]]:
    matrix: list[list[int]] = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            temp = randint(1, 101)
            if i != j:
                matrix[i][j], matrix[j][i] = temp, temp

    return matrix


def main():
    write_in_file()


if __name__ == "__main__":
    main()