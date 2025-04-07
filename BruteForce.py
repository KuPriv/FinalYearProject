import time
from itertools import permutations
from xmlrpc.client import MAXINT

from Chain_MonteCarlo import chain_monte_ui
from UI import UI


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
    matrices = UI()
    for matrix in matrices:
        way, distance = bruteforce(matrix)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)

    chain_monte_ui(matrices)


if __name__ == "__main__":
    main()