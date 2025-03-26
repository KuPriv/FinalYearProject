import read_from_file


def nearest_neighbor(matrix) -> tuple:
    print(matrix)
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
    matrices = read_from_file.main()
    for matrix in matrices:
        way, distance = nearest_neighbor(matrix)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)


if __name__ == "__main__":
    main()
