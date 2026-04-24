# 1. В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива.

matrix = [[3, -5, 7], [-2, 4, -8], [6, -1, 9]]

negatives = list(filter(lambda x: x < 0, [num for row in matrix for num in row]))

print("Матрица:", matrix)
print("Отрицательные элементы:", negatives)
print("Размер полученного массива:", len(negatives))
