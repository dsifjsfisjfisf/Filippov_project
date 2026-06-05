#Создайте класс "Компьютер" с атрибутом "марка", "процессор", и "Оперативная память", напишите метод который выводит информацию о ПК в формате "Марка: марка, Процессор, Оперативная память: память".
class Computer:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram
    
    def display_info(self):
        print(f"Марка: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.ram}")

def get_input(field):
    return input(f"Введите {field}: ")

def create_computer(data):
    return Computer(*data)

def display_computer(computer):
    computer.display_info()
    return computer

data = list(map(get_input, ["марку компьютера", "процессор", "оперативную память"]))
pc = create_computer(data)
display_computer(pc)
