from pathlib import Path
name_folder = 'generated_files'

def main() -> list:
    matrix = get_data_from_file()
    return matrix


def get_data_from_file() -> list:
    count_of_files: int = count_files()
    matrix = []
    for i in range(count_of_files):
        with open(name_folder + fr'/{i + 1}.txt') as file:
            data = file.readlines()
            data = [list(map(int, line.rstrip().split())) for line in data]
            row = [number for number in data]
            matrix.append(row)
    return matrix


def count_files() -> int:
    # returns: количество файлов в папке generated_files
    folder = Path(name_folder)
    return len(list(folder.iterdir()))


if __name__ == "__main__":
    main()