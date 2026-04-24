# 1. В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива.

import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = [[random.randint(-20, 20) for _ in range(cols)] for _ in range(rows)]

print("Матрица:")
for row in matrix:
    print(row)

negatives = list(filter(lambda x: x < 0, [num for row in matrix for num in row]))

print("\nОтрицательные элементы:", negatives)
print("Размер полученного массива:", len(negatives))
