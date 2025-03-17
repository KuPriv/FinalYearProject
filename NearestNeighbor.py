import read_from_file


def nearest_neighbor(matrix):
    n = len(matrix)
    visited = [False] * n
    visited[0] = True
    way = [0]

    for _ in range(n - 1):
        last_city = way[-1]
        nearest_city = min([(i, matrix[last_city][i]) for i in range(n)
                            if not visited[i]], key=lambda x: x[1])[0]
        way.append(nearest_city)
        visited[nearest_city] = True

    way.append(0)
    distance = sum(matrix[way[i]][way[i+1]] for i in range(n))
    return way, distance


def main() -> None:
    matrix = read_from_file.main()
    for matrix in matrix:
        way, distance = nearest_neighbor(matrix)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)


if __name__ == "__main__":
    main()
