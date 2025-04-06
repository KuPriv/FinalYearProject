import math
import time
from random import choices
from xmlrpc.client import MAXINT

from UI import UI


def time_counter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return res
    return wrapper


@time_counter
def solution(matrix: list, iters: int) -> tuple:
    n: int = len(matrix)
    min_dist: int = MAXINT
    best_way = None

    for _ in range(iters):
        way, dist = markov_chain(matrix, n)
        if dist < min_dist:
            min_dist = dist
            best_way = way

    return best_way, min_dist


def markov_chain(matrix, n, alpha: float = 1.0) -> tuple:
    cur_state = 0
    way = [0]
    unvisited = set(range(n))
    unvisited.remove(cur_state)

    while unvisited:
        available_states = list(unvisited)
        weights = [math.exp(-alpha * matrix[cur_state][j]) for j in available_states]
        sum_weight = sum(weights)
        calc_weights = [w / sum_weight for w in weights]

        next_state = choices(available_states, weights=calc_weights, k=1)[0]
        way.append(next_state)
        unvisited.remove(next_state)
        cur_state = next_state

    dist = calc_distance(way, matrix)
    return way, dist


def calc_distance(way, matrix) -> int:
    return sum(matrix[way[i]][way[i+1]] for i in range(len(way)-1)) + + matrix[way[-1]][way[0]]


def main() -> None:
    matrices = UI()
    iters = 10000

    for matrix in matrices:
        way, distance = solution(matrix, iters)
        # print("Лучший маршрут:", way)
        # print("Кратчайшее расстояние:", distance)
        print(distance)


if __name__ == "__main__":
    main()