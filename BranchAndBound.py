import time
from xmlrpc.client import MAXINT

import read_from_file


def time_counter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return res
    return wrapper


@time_counter
def branch_and_bound_tsp(matrix: list) -> tuple:
    n = len(matrix)
    min_dist: int = MAXINT
    best_way = None

    def solve(row: list | int, visited: set, dist: int, way: list) -> None:
        nonlocal min_dist, best_way
        if len(way) == n:
            dist += matrix[row][0]

            if dist < min_dist:
                min_dist = dist
                best_way = way + [0]
            return

        for next_row in range(n):
            if next_row not in visited:
                solve(next_row, visited | {next_row}, dist + matrix[row][next_row], way + [next_row])

    solve(0, {0}, 0, [0])
    return best_way, min_dist


def main() -> None:
    matrices = read_from_file.main()
    for matrix in matrices:
        way, distance = branch_and_bound_tsp(matrix)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)


if __name__ == "__main__":
    main()