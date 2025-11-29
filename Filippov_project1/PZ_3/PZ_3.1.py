#Дано четырехзначное число. Проверить истинность высказывания "Данное число читается одинаково слева направо и справа налево"

number = int(input("Введите четырехзначное число"))
while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print("Число введено неверно")
        number = input("Введите четырехзначное число")

thous = number // 1000
hundr = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

if thous == units and hundr == tens:
    print("число читается одинаково справа налево")
else:
    print("Число не читается справа налево")
