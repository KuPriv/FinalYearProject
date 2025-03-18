from random import shuffle
from xmlrpc.client import MAXINT

import read_from_file


def calc_distance(way, matrix) -> int:
    return sum(matrix[way[i]][way[i+1]] for i in range(len(way)-1)) + matrix[way[-1]][way[0]]


def monte_carlo(matrix, iters: int) -> tuple:
    n = len(matrix)
    cities = list(range(n))
    min_dist: int = MAXINT
    best_way = None

    for _ in range(iters):
        way = cities[:]
        # shuffle - из библиотеки random, работает быстрее, так как локальная область видимости
        shuffle(way)
        cur_dist = calc_distance(way, matrix)
        if cur_dist < min_dist:
            min_dist = cur_dist
            best_way = way

    return best_way, min_dist

def main() -> None:
    matrix = read_from_file.main()
    for matrix in matrix:
        way, distance = monte_carlo(matrix, iters=10000)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)


if __name__ == "__main__":
    main()