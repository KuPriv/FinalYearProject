from pathlib import Path

name_folder = 'generated_files'


def get_data_from_all_files(n: int) -> list:
    count_of_files: int = count_files(n)
    matrix = []
    for i in range(count_of_files):
        with open(name_folder + fr'/{n}/{i + 1}.txt') as file:
            data = file.readlines()
            data = [list(map(int, line.rstrip().split())) for line in data]
            row = [number for number in data]
            matrix.append(row)
    return matrix


def get_data_from_one_file(n: int, file_n: int) -> list:
    matrix = []
    with open(name_folder + fr'/{n}/{file_n}.txt') as file:
        data = file.readlines()
        data = [list(map(int, line.rstrip().split())) for line in data]
        row = [number for number in data]
        matrix.append(row)
    return matrix


def count_files(n: int) -> int:
    # returns: количество файлов в папке generated_files/n, n - номер папки
    folder = Path(name_folder + f'/{n}')
    return len(list(folder.iterdir()))


def main() -> None:
    ...


if __name__ == "__main__":
    main()