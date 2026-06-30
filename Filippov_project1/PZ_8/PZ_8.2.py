#Дана строка  отражающая продажи продукции по дням в кг. Преобразовать информацию из строки в словари, с использованием функции найти среднее значение продаж по каждому виду  продукции, результаты вывести на экран
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

s = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
words = s.split()

fruits = {}
current_fruit = None
for item in words:
    if item.isalpha():
        current_fruit = item
        fruits[current_fruit] = []
    else:
        fruits[current_fruit].append(int(item))

for fruit, numbers in fruits.items():
    avg = calculate_average(numbers)
    print(f"{fruit}: среднее = {avg:.2f}")
