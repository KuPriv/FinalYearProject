import sys
import time

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
def branch_and_bound(matrix: list) -> tuple:
    best_dist = sys.maxsize
    best_way = None
    n = len(matrix)

    def calc_lower_bound(node: int, unvisited: set[int], dist: int) -> int:
        lower_bound = dist

        if unvisited:
            lower_bound += min(matrix[node][j] for j in unvisited)

        for city in unvisited:
            min_dist = sys.maxsize
            for next_city in range(n):
                if next_city != city and (next_city in unvisited or next_city == 0):
                    min_dist = min(min_dist, matrix[city][next_city])

            if min_dist != sys.maxsize:
                lower_bound += min_dist

        return lower_bound


    def branch_and_bound_recursive(way: list, dist: int, unvisited: set) -> None:
        nonlocal best_dist, best_way

        if not unvisited:
            cost = dist + matrix[way[-1]][way[0]]
            if cost < best_dist:
                best_dist = cost
                best_way = way.copy()
            return

        node = way[-1]
        lower_bound = calc_lower_bound(node, unvisited, dist)

        if lower_bound >= best_dist:
            return

        for city in list(unvisited):
            new_cost = dist + matrix[way[-1]][city]
            if new_cost >= best_dist:
                continue

            way.append(city)
            unvisited.remove(city)
            branch_and_bound_recursive(way, new_cost, unvisited)
            unvisited.add(city)
            way.pop()

    branch_and_bound_recursive([0], 0, set(range(1, n)))

    return best_way, best_dist


def main() -> None:
    matrices, best_ways = [], []
    while not matrices:
        matrices = UI()

    for matrix in matrices:
        way, distance = branch_and_bound(matrix)
        best_ways.append(way)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)


if __name__ == "__main__":
    main()