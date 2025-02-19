import os
from random import randint

def generate_array() -> list[list[int]]:
    n: int = initialize()
    arr: list[list[int]] = [[randint(1, 101) if i != j else 0 for i in range(n)] for j in range(n)]

    return arr


def initialize() -> int:
    n = int(input("Введите размерность: "))
    return n


def write_in_file():
    for number_of_file in range(3):
        try:
            with open(f'{number_of_file + 1}.txt', mode='w+', encoding='utf-8') as file:
                arr_to_write: list[list[int]] = generate_array()
                for line_index in range(len(arr_to_write)):
                    line_to_str: list[str] = [str(n) for n in arr_to_write[line_index]]
                    line_to_str: str = " ".join (line_to_str)

                    file.write(line_to_str + '\n')

        except Exception as e:
            print(f'Ошибка: {e}')


def main():
    write_in_file()


if __name__ == "__main__":
    main()