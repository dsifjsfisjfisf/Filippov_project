#Приложение выдача кредитов для некоторой организации БД должна содержать таблицу клиент со след структурой записи: ФИО клиента, ФИО сотрудника банка, срок кредита, процент кредита, сумма кредита.
import sqlite3 as sq
import os

DB = "credits.db"

# Данные для заполнения таблицы
CREDITS_DATA = [
    ("Иванов Иван Иванович", "Петров Петр Петрович", 12, 15.5, 500000),
    ("Сидорова Анна Сергеевна", "Смирнов Алексей Владимирович", 24, 12.0, 1000000),
    ("Козлов Дмитрий Николаевич", "Иванова Елена Михайловна", 6, 18.5, 300000),
    ("Морозова Ольга Петровна", "Петров Петр Петрович", 36, 10.0, 2000000),
    ("Васильев Сергей Андреевич", "Смирнов Алексей Владимирович", 18, 14.0, 750000),
    ("Новикова Татьяна Павловна", "Иванова Елена Михайловна", 24, 13.5, 850000),
    ("Федоров Артем Викторович", "Петров Петр Петрович", 12, 16.0, 400000),
    ("Егорова Мария Владимировна", "Смирнов Алексей Владимирович", 48, 9.5, 3000000),
    ("Андреев Павел Романович", "Иванова Елена Михайловна", 6, 19.0, 250000),
    ("Павлова Светлана Максимовна", "Петров Петр Петрович", 30, 11.0, 1500000)
]

def init_db():
    if os.path.exists(DB):
        os.remove(DB)
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE Клиент (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            фио_клиента TEXT NOT NULL,
            фио_сотрудника_банка TEXT NOT NULL,
            срок_кредита INTEGER NOT NULL,
            процент_кредита REAL NOT NULL,
            сумма_кредита REAL NOT NULL
        )""")
        cur.executemany("INSERT INTO Клиент (фио_клиента, фио_сотрудника_банка, срок_кредита, процент_кредита, сумма_кредита) VALUES (?,?,?,?,?)", CREDITS_DATA)

def show_all():
    with sq.connect(DB) as con:
        for row in con.cursor().execute("SELECT * FROM Клиент"):
            print(row)

def search_by_client_name():
    name = input("Введите ФИО клиента: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Клиент WHERE фио_клиента LIKE ?", (f"%{name}%",))
        for row in cur:
            print(row)

def search_by_employee_name():
    name = input("Введите ФИО сотрудника банка: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Клиент WHERE фио_сотрудника_банка LIKE ?", (f"%{name}%",))
        for row in cur:
            print(row)

def search_by_amount():
    try:
        amount = float(input("Минимальная сумма кредита: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Клиент WHERE сумма_кредита > ?", (amount,))
            for row in cur:
                print(row)
    except ValueError:
        print("Некорректная сумма.")

def edit_interest():
    try:
        cid = int(input("ID клиента: "))
        new_interest = float(input("Новый процент: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("UPDATE Клиент SET процент_кредита = ? WHERE id = ?", (new_interest, cid))
            print("Обновлено." if cur.rowcount else "Не найдено.")
    except ValueError:
        print("Некорректный ввод.")

def edit_amount():
    try:
        cid = int(input("ID клиента: "))
        new_amount = float(input("Новая сумма: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("UPDATE Клиент SET сумма_кредита = ? WHERE id = ?", (new_amount, cid))
            print("Обновлено." if cur.rowcount else "Не найдено.")
    except ValueError:
        print("Некорректный ввод.")

def edit_term():
    try:
        cid = int(input("ID клиента: "))
        new_term = int(input("Новый срок (месяцев): "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("UPDATE Клиент SET срок_кредита = ? WHERE id = ?", (new_term, cid))
            print("Обновлено." if cur.rowcount else "Не найдено.")
    except ValueError:
        print("Некорректный ввод.")

def delete_by_id():
    try:
        cid = int(input("ID клиента: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Клиент WHERE id = ?", (cid,))
            print(f"Удалено: {cur.rowcount}")
    except ValueError:
        print("Некорректный ID.")

def delete_by_name():
    name = input("ФИО клиента: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Клиент WHERE фио_клиента = ?", (name,))
        print(f"Удалено: {cur.rowcount}")

def delete_by_amount():
    try:
        amount = float(input("Удалить клиентов с суммой меньше: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Клиент WHERE сумма_кредита < ?", (amount,))
            print(f"Удалено: {cur.rowcount}")
    except ValueError:
        print("Некорректная сумма.")

def add_client():
    try:
        name = input("ФИО клиента: ")
        employee = input("ФИО сотрудника: ")
        term = int(input("Срок (месяцев): "))
        interest = float(input("Процент: "))
        amount = float(input("Сумма: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Клиент (фио_клиента, фио_сотрудника_банка, срок_кредита, процент_кредита, сумма_кредита) VALUES (?,?,?,?,?)",
                        (name, employee, term, interest, amount))
            print("Клиент добавлен.")
    except ValueError:
        print("Некорректный ввод.")

def main():
    if not os.path.exists(DB):
        init_db()
        print("База данных создана и заполнена.")
    else:
        print("База данных уже существует.")

    while True:
        print("\n" + "="*50)
        print("ПРИЛОЖЕНИЕ ВЫДАЧА КРЕДИТОВ")
        print("="*50)
        print("1. Показать всех клиентов")
        print("2. Поиск по ФИО клиента")
        print("3. Поиск по ФИО сотрудника")
        print("4. Поиск по минимальной сумме")
        print("5. Редактировать процент (по ID)")
        print("6. Редактировать сумму (по ID)")
        print("7. Редактировать срок (по ID)")
        print("8. Удалить по ID")
        print("9. Удалить по ФИО")
        print("10. Удалить по сумме меньше")
        print("11. Добавить клиента")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        if choice == '1':
            show_all()
        elif choice == '2':
            search_by_client_name()
        elif choice == '3':
            search_by_employee_name()
        elif choice == '4':
            search_by_amount()
        elif choice == '5':
            edit_interest()
        elif choice == '6':
            edit_amount()
        elif choice == '7':
            edit_term()
        elif choice == '8':
            delete_by_id()
        elif choice == '9':
            delete_by_name()
        elif choice == '10':
            delete_by_amount()
        elif choice == '11':
            add_client()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
