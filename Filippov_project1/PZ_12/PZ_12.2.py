# 2. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.

matrix = [[3, 5, 7], [2, 4, 8], [6, 1, 9], [5, 3, 2], [8, 2, 6]]

averages = list(map(lambda row: sum(row) / len(row), [matrix[i] for i in range(len(matrix)) if (i + 1) % 2 != 0]))

print("Матрица:")
for row in matrix:
    print(row)

print("\nСреднее арифметическое строк с нечетным номером:", averages)
