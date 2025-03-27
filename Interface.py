from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMessageBox
from matplotlib.patches import FancyArrowPatch

import sys
import os
import random
import time

from NearestNeighbor import nearest_neighbor as imported_nearest_neighbor
from MonteCarlo import monte_carlo as imported_monte_carlo
from BruteForce import bruteforce as imported_bruteforce
from Markov_chain import monte_carlo as imported_markov_chain


class MyInterface(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.matrix = None
        self.setWindowTitle("Построение маршрутов")
        self.setGeometry(700, 400, 300, 200)
        self.UI()

    def UI(self) -> None:
        centre = QtWidgets.QWidget(self)
        self.setCentralWidget(centre)

        main_layout = QtWidgets.QVBoxLayout()
        input_layout = QtWidgets.QHBoxLayout()
        button_layout = QtWidgets.QHBoxLayout()

        self.size_of_matrix_input = QtWidgets.QLineEdit()
        self.size_of_matrix_input.setPlaceholderText("Размерность матрицы")
        input_layout.addWidget(self.size_of_matrix_input)

        self.generate_files_button = QtWidgets.QPushButton("Сгенерировать файлы")
        self.generate_files_button.clicked.connect(self.generate_files)
        input_layout.addWidget(self.generate_files_button)
        main_layout.addLayout(input_layout)

        self.brute_force_button = QtWidgets.QPushButton("Полный перебор")
        self.brute_force_button.clicked.connect(lambda: self.select_file('brute_force'))
        button_layout.addWidget(self.brute_force_button)

        self.monte_carlo_button = QtWidgets.QPushButton("Монте Карло")
        self.monte_carlo_button.clicked.connect(lambda: self.select_file('monte_carlo'))
        button_layout.addWidget(self.monte_carlo_button)

        self.nearest_neighbor_button = QtWidgets.QPushButton("Ближайший сосед")
        self.nearest_neighbor_button.clicked.connect(lambda: self.select_file('nearest_neighbor'))
        button_layout.addWidget(self.nearest_neighbor_button)

        self.markov_chain_button = QtWidgets.QPushButton("Цепи Маркова")
        self.markov_chain_button.clicked.connect(lambda: self.select_file('markov_chain'))
        button_layout.addWidget(self.markov_chain_button)

        main_layout.addLayout(button_layout)
        centre.setLayout(main_layout)

    def generate_files(self) -> None:
        n = self.size_of_matrix_input.text()
        try:
            n = int(n)
            if n <= 1:
                raise ValueError
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Введите корректное целое число больше 1")
            return

        dir = "generated_files_for_interface"
        if not os.path.exists(dir):
            os.makedirs(dir)

        for i in range(3):
            filename = os.path.join(dir, f"cities_{i + 1}.txt")
            with open(filename, "w") as f:
                for _ in range(n):
                    x = random.uniform(0, 1000)
                    y = random.uniform(0, 1000)
                    f.write(f"{x} {y}\n")
        QtWidgets.QMessageBox.information(self, "Успешно",
                                          "Файлы сгенерированы.")

    def select_file(self, algorithm) -> None:
        options = QtWidgets.QFileDialog.Options()
        dir = os.path.join(os.getcwd(), "generated_files_for_interface")
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self,
            "Выберите файл с городами", dir,"Text Files (*.txt);;All Files (*)",
                                                        options=options)
        if file:
            self.run_algorithm(algorithm, file)

    def run_algorithm(self, algorithm, file) -> None:
        cities = []
        with open(file, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    x_str, y_str = parts[:2]
                    x, y = float(x_str), float(y_str)
                    cities.append((x, y))

        self.create_matrix(cities)

        if algorithm == 'brute_force':
            way, distance = self.brute_force()
        elif algorithm == 'nearest_neighbor':
            way, distance = self.nearest_neighbor()
        elif algorithm == 'monte_carlo':
            way, distance = self.monte_carlo()
        elif algorithm == 'markov_chain':
            way, distance = self.markov_chain()
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Что-то пошло не так)")
            return

        self.show_result(cities, way, distance, algorithm)

    def show_result(self, cities, way, distance, algorithm) -> None:
        fig, ax = plt.subplots()
        fig.canvas.manager.set_window_title(f"Алгоритм: {algorithm}")

        x_coords = [cities[i][0] for i in way] + [cities[way[0]][0]]
        y_coords = [cities[i][1] for i in way] + [cities[way[0]][1]]
        ax.scatter(x_coords[:-1], y_coords[:-1], color='blue', label='Города', zorder=2)

        for idx, (x, y) in enumerate(zip(x_coords[:-1], y_coords[:-1])):
            ax.annotate(str(idx + 1), (x, y), textcoords="offset points", xytext=(0, 5), color='b')

        for i in range(len(x_coords) - 1):
            start = (x_coords[i], y_coords[i])
            end = (x_coords[i + 1], y_coords[i + 1])
            arrow = FancyArrowPatch(start, end, arrowstyle='->', color='r', mutation_scale=10, lw=1.5)
            ax.add_patch(arrow)

        ax.set_title(f"Алгоритм: {algorithm}, Расстояние: %.5f" % (distance))
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()
        ax.grid(True)
        plt.show()

    def create_matrix(self, cities) -> list:
        self.matrix = self.distance_matrix(cities)
        return self

    def distance_matrix(self, way) -> list:
        n = len(way)
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                if i == j:
                    row.append(0)
                else:
                    row.append(self.distance(way[i], way[j]))
            matrix.append(row)
        return matrix

    def distance(self, city1, city2):
        return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

    def _time_decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            t = end - start

            msg = QMessageBox()
            msg.setWindowTitle("Время выполнения")
            msg.setText(str(t))
            msg.exec_()

            return result
        return wrapper

    @_time_decorator
    def brute_force(self):
        return imported_bruteforce(self.matrix)

    @_time_decorator
    def nearest_neighbor(self):
        return imported_nearest_neighbor(self.matrix)

    @_time_decorator
    def monte_carlo(self):
        return imported_monte_carlo(self.matrix, iters=10000)

    @_time_decorator
    def markov_chain(self):
        return imported_markov_chain(self.matrix, iters=10000)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyInterface()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()