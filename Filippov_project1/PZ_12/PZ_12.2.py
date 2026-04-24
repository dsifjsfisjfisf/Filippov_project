# 2. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.

import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = [[random.randint(-20, 20) for _ in range(cols)] for _ in range(rows)]

print("Матрица:")
for i, row in enumerate(matrix):
    print(f"Строка {i+1}: {row}")

averages = list(map(lambda i: sum(matrix[i]) / len(matrix[i]), filter(lambda i: (i + 1) % 2 != 0, range(len(matrix)))))

print("\nСреднее арифметическое строк с нечетным номером:", averages)
