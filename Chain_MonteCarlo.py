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
def chain_method(matrix, best_way, iters: int = 100000) -> tuple:
    n = len(matrix)
    best_dist = calc_distance(best_way, matrix)
    improved = True
    iteration = 0

    while improved and iteration < iters:
        improved = False
        iteration += 1
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                new_way = best_way[:i] + best_way[i:j+1][::-1] + best_way[j+1:]
                new_dist = calc_distance(new_way, matrix)
                if new_dist < best_dist:
                    best_way = new_way
                    best_dist = new_dist
                    improved = True
                    break
            if improved:
                break

    return best_way, best_dist


def chain_monte_ui(matrices, best_ways) -> None:
    s = str(input("'Хотите улучшить решение?\nВведите 'Да' или 'Нет': "))
    if s.lower() == 'да':
        main(matrices, best_ways)
    elif s.lower() == 'нет':
        print('Пока')
    else:
        print('Некорректный ввод.')
        chain_monte_ui(matrices, best_ways)


def main(matrices, best_ways) -> None:
    print('С учетом выполнения цепного метода, полученные решения:')
    for i in range(len(matrices)):
        matrix, best_way = matrices[i], best_ways[i]
        way, distance = chain_method(matrix, best_way)
        print("Лучший маршрут:", way)
        print("Кратчайшее расстояние:", distance)