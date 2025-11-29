#Даны координаты двух различных полей шахматной доски x1, y1, x2, y2 (целые числа лежащие в диапозоне 1-8) Проверить истинность высказывания: "Ладья за один ход может перейти с одного поля на другое"
x1 = int(input("Введите x1 от 1 до 8"))
y1 = int(input("Введите y1 от 1 до 8"))
x2 = int(input("Введите x2 от 1 до 8"))
y2 = int(input("Введите y2 от 1 до 8"))

while type(x1) != int:
    try:
        a = int(x1)
    except ValueError:
        print("координаты введены неверно")
        x1 = input("Введите x1 от 1 до 8")

while type(y1) != int:
    try:
        y1 = int(y1)
    except ValueError:
        print("координаты введены неверно")
        y1 = input("Введите y1 от 1 до 8")

while type(x2) != int:
    try:
        x2 = int(x2)
    except ValueError:
        print("координаты введены неверно")
        x2 = input("Введите x2 от 1 до 8")

while type(y2) != int:
    try:
        y2 = int(y2)
    except ValueError:
        print("координаты введены неверно")
        y2 = input("Введите y2 от 1 до 8")

if x1 == x2 and y1 == y2:
    print("Ладья стоит на месте")
elif x1 == x2 or y1 == y2:
    print("Ладья может за один ход перейти с одного поля на другое")
else:
    print("Ладья НЕ может за один ход перейти с одного поля на другое")

if x1 and y1 and x2 and y2 <= 0 or  x1 and y1 and x2 and y2 >= 9:
    print("Число должно быть в диапозоне от 1 до 8!")
