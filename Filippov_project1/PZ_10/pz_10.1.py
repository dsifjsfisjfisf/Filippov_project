import random

numbers1 = [random.randint(-20, 20) for _ in range(10)]
numbers2 = [random.randint(-20, 20) for _ in range(10)]

with open('first.txt', 'w', encoding='utf-16le') as f:
    f.write(' '.join(map(str, numbers1)))

with open('second.txt', 'w', encoding='utf-16le') as f:
    f.write(' '.join(map(str, numbers2)))

multiples_3 = [x for x in numbers1 if x % 3 == 0]
product = 1
for x in multiples_3:
    product *= x
min_element = min(numbers1)

multiples_5 = [x for x in numbers2 if x % 5 == 0]
count = len(numbers2)
average = sum(numbers2) / count if count > 0 else 0

with open('result.txt', 'w', encoding='utf-16le') as f:
    f.write("Содержимое первого файла:\n")
    f.write(' '.join(map(str, numbers1)) + "\n")
    f.write("Элементы кратные 3: " + ' '.join(map(str, multiples_3)) + "\n")
    f.write("Произведение элементов: " + str(product) + "\n")
    f.write("Минимальный элемент: " + str(min_element) + "\n\n")
    
    f.write("Содержимое второго файла:\n")
    f.write(' '.join(map(str, numbers2)) + "\n")
    f.write("Элементы кратные 5: " + ' '.join(map(str, multiples_5)) + "\n")
    f.write("Количество элементов: " + str(count) + "\n")
    f.write("Среднее арифметическое элементов: " + str(average) + "\n")

print("Файлы созданы")
