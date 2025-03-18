from itertools import permutations
from xmlrpc.client import MAXINT

import read_from_file


def calc_distance(way, matrix) -> int:
    return sum(matrix[way[i]][way[i+1]] for i in range(len(way)-1)) + matrix[way[-1]][way[0]]


def bruteforce(matrix) -> tuple:
    n: int = len(matrix)
    cities = list(range(n))
    min_dist: int = MAXINT
    best_way = None

    for combination in permutations(cities):
        cur_dist = calc_distance(combination, matrix)
        if cur_dist < min_dist:
            min_dist = cur_dist
            best_way = combination

    return best_way, min_dist


def main() -> None:
    matrix = read_from_file.main()
    for matrix in matrix:
        way, distance = bruteforce(matrix)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)


if __name__ == "__main__":
    main()