from random import choices
from xmlrpc.client import MAXINT

import read_from_file


def calc_distance(way, matrix) -> float:
    return sum(matrix[way[i]][way[i+1]] for i in range(len(way)-1)) + + matrix[way[-1]][way[0]]


def marcov(N, matrix) -> tuple:
    cur_state = 0
    way = [0]
    unvisited = set(range(N))
    unvisited.remove(cur_state)

    while unvisited:
        avaiable_states = list(unvisited)
        weights = [1 / matrix[cur_state][j] for j in avaiable_states]
        sum_weight = sum(weights)
        calc_weights = [w / sum_weight for w in weights]

        next_state = choices(avaiable_states, weights=calc_weights, k=1)[0]
        way.append(next_state)
        unvisited.remove(next_state)
        cur_state = next_state

    dist = calc_distance(way, matrix)
    return way, dist

def monte_carlo(matrix: list, iters: int) -> tuple:
    n: int = len(matrix)
    min_dist: int = MAXINT
    best_way = None

    for _ in range(iters):
        way, dist = marcov(n, matrix)
        if dist < min_dist:
            min_dist = dist
            best_way = way

    return best_way, min_dist


def main() -> None:
    matrices = read_from_file.main()
    iters = 10000

    for matrix in matrices:
        way, distance = monte_carlo(matrix, iters)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)


if __name__ == "__main__":
    main()