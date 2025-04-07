import time
from xmlrpc.client import MAXINT

from Chain_MonteCarlo import chain_monte_ui
from UI import UI


def time_counter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return res
    return wrapper


best_distance = MAXINT
best_way = None


@time_counter
def branch_and_bound(matrix: list) -> tuple:
    global best_distance, best_way

    best_distance = MAXINT
    best_way = None
    n = len(matrix)
    unvisited = set(range(1, n))
    branch_and_bound_recursive([0], 0, unvisited, matrix, n)
    return best_way, best_distance


def branch_and_bound_recursive(way: list, distance: int, unvisited: set, matrix: list, n: int) -> None:
    global best_distance, best_way

    if not unvisited:
        sum_cost = distance + matrix[way[-1]][way[0]]
        if sum_cost < best_distance:
            best_distance = sum_cost
            best_way = way.copy()
        return

    lower_dist = distance
    if unvisited:
        lower_dist += min(matrix[way[-1]][j] for j in unvisited)
    for i in unvisited:
        lower_dist += min(matrix[i][k] for k in range(n) if k != i)

    if lower_dist >= best_distance:
        return

    for city in list(unvisited):
        new_cost = distance + matrix[way[-1]][city]
        way.append(city)
        unvisited.remove(city)
        branch_and_bound_recursive(way, new_cost, unvisited, matrix, n)
        unvisited.add(city)
        way.pop()


def main() -> None:
    matrices = UI()
    for matrix in matrices:
        way, distance = branch_and_bound(matrix)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)

    chain_monte_ui(matrices)


if __name__ == "__main__":
    main()