#Дано целые числа A и B (A < B) Вывести все целые числа от A до B включительно; при этом число A должно выводиться 1 раз, число A+1 должно выводиться 2 раза и т.д
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
