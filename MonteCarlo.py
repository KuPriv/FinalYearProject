import time
from random import shuffle
from xmlrpc.client import MAXINT

import read_from_file


def calc_distance(way, matrix) -> int:
    return sum(matrix[way[i]][way[i+1]] for i in range(len(way)-1)) + matrix[way[-1]][way[0]]


def time_counter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return res
    return wrapper


@time_counter
def monte_carlo(matrix, iters: int) -> tuple:
    n = len(matrix)
    cities = list(range(n))
    min_dist: int = MAXINT
    best_way = None

    for _ in range(iters):
        way = cities[:]
        # shuffle - из библиотеки random, работает быстрее, так как локальная область видимости
        shuffle(way)
        way[way.index(0)], way[0] = way[0], way[way.index(0)]
        cur_dist = calc_distance(way, matrix)
        if cur_dist < min_dist:
            min_dist = cur_dist
            best_way = way

    return best_way, min_dist

def main() -> None:
    matrices = read_from_file.main()
    for matrix in matrices:
        way, distance = monte_carlo(matrix, iters=10000)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)


if __name__ == "__main__":
    main()