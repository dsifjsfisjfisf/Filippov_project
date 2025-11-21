#Даны  целые положительные числа N и K Используя только операции сложения и вычитания, найти частное от деления нацело N и K а также остаток от этого деления
N = input("Введите N: ")
K = input("Введите K: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("введено неверно")
        N = input("Введите N еще раз")

while type(K) != int:
    try:
        K = int(K)
    except ValueError:
        print("введено неверно")
        K = input("введите K еще раз")


quotient = 0
temp = N

while temp >= K:
    temp = temp - K
    quotient = quotient + 1

remainder = temp

print(f"Частное: {quotient}")
print(f"Остаток: {remainder}")