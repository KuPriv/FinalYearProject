import time


def time_counter(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return res
    return wrapper


def calc_distance(route, matrix) -> int:
    return sum(matrix[route[i]][route[i+1]] for i in range(len(route)-1)) + matrix[route[-1]][route[0]]


@time_counter
def chain_method(matrix, iters: int = 1000) -> tuple:
    n = len(matrix)
    route = list(range(n))
    best_dist = calc_distance(route, matrix)
    improved = True
    iteration = 0

    while improved and iteration < iters:
        improved = False
        iteration += 1
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                new_route = route[:i] + route[i:j+1][::-1] + route[j+1:]
                new_dist = calc_distance(new_route, matrix)
                if new_dist < best_dist:
                    route = new_route
                    best_dist = new_dist
                    improved = True
                    break
            if improved:
                break

    return route, best_dist


def chain_monte_ui(matrices) -> None:
    s = str(input("'Хотите улучшить решение?\nВведите 'Да' или 'Нет': "))
    if s.lower() == 'да':
        main(matrices)
    elif s.lower() == 'нет':
        print('Пока')
    else:
        print('Некорректный ввод.')
        chain_monte_ui(matrices)


def main(matrices) -> None:
    print('С учетом выполнения цепного метода, полученные решения:')
    for matrix in matrices:
        way, distance = chain_method(matrix, iters=1000)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)