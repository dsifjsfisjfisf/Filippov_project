a = input("Введите первое число")
b = input("Введите второе число")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("введено неверно")
        a = input("Введите a еще раз")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("введено неверно")
        b = input("введите b еще раз")

k = 1
while a <= b:
    print((str(a) + " ") * k)
    a += 1
    k += 1