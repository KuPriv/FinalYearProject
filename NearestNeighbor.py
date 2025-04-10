import time

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


@time_counter
def nearest_neighbor(matrix: list) -> tuple:
    n = len(matrix)
    visited = [False] * n
    visited[0] = True
    way = [0]

    for _ in range(n - 1):
        last_city = way[-1]
        nearest_city = [(i, matrix[last_city][i]) for i in range(n) if not visited[i]]
        nearest_city = min(nearest_city, key= lambda x: x[1])[0]
        way.append(nearest_city)
        visited[nearest_city] = True

    distance = sum(matrix[way[i]][way[i+1]] for i in range(n - 1)) + matrix[way[-1]][way[0]]
    return way, distance


def main() -> None:
    matrices = []
    while not matrices:
        matrices = UI()

    for matrix in matrices:
        way, distance = nearest_neighbor(matrix)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)

    chain_monte_ui(matrices)


if __name__ == "__main__":
    main()
