#Задача 24. Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
#Создайте классы "Мужчина" и "Женщина", которые наследуются от класса "Человек".
#Каждый класс должен иметь метод, который выводит информацию о поле объекта.


class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")

class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Мужчина")

    def show_gender(self):
        print(f"Пол: {self.gender}")

class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Женщина")

    def show_gender(self):
        print(f"Пол: {self.gender}")

print("Создание мужчины:")
name = input("Введите имя: ")
age = int(input("Введите возраст: "))
man = Man(name, age)

print("\nСоздание женщины:")
name = input("Введите имя: ")
age = int(input("Введите возраст: "))
woman = Woman(name, age)

print("\n" + "="*30)
man.display_info()
man.show_gender()

print()

woman.display_info()
woman.show_gender()
