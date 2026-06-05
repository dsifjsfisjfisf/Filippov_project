#Приложение выдача кредитов для некоторой организации БД должна содержать таблицу клиент со след структурой записи: ФИО клиента, ФИО сотрудника банка, срок кредита, процент кредита, сумма кредита.
import sqlite3

def create_connection():
    return sqlite3.connect('bank_credits.db')

def create_table():
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Клиент (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                фио_клиента TEXT NOT NULL,
                фио_сотрудника_банка TEXT NOT NULL,
                срок_кредита INTEGER NOT NULL,
                процент_кредита REAL NOT NULL,
                сумма_кредита REAL NOT NULL
            )
        ''')

def execute_query(query, params=()):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

def execute_commit(query, params=()):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.rowcount

def add_client(client_data):
    execute_commit('''
        INSERT INTO Клиент (фио_клиента, фио_сотрудника_банка, срок_кредита, процент_кредита, сумма_кредита)
        VALUES (?, ?, ?, ?, ?)
    ''', client_data)

def search_clients(search_by, search_value):
    queries = {
        '1': "SELECT * FROM Клиент WHERE фио_клиента LIKE ?",
        '2': "SELECT * FROM Клиент WHERE фио_сотрудника_банка LIKE ?",
        '3': "SELECT * FROM Клиент WHERE сумма_кредита > ?"
    }
    results = execute_query(queries.get(search_by, "SELECT * FROM Клиент WHERE 1=0"), (f'%{search_value}%',))
    return results

def delete_client(delete_by, delete_value):
    queries = {
        '1': "DELETE FROM Клиент WHERE id = ?",
        '2': "DELETE FROM Клиент WHERE фио_клиента = ?",
        '3': "DELETE FROM Клиент WHERE сумма_кредита < ?"
    }
    return execute_commit(queries.get(delete_by, "SELECT 1 WHERE 1=0"), (delete_value,))

def update_client(update_by, update_value, client_id):
    queries = {
        '1': "UPDATE Клиент SET срок_кредита = ? WHERE id = ?",
        '2': "UPDATE Клиент SET процент_кредита = ? WHERE id = ?",
        '3': "UPDATE Клиент SET сумма_кредита = ? WHERE id = ?"
    }
    return execute_commit(queries.get(update_by, "SELECT 1 WHERE 1=0"), (update_value, client_id))

def get_all_clients():
    return execute_query("SELECT * FROM Клиент")

def init_sample_data():
    sample_clients = [
        ('Иванов Иван Иванович', 'Петров Петр Петрович', 12, 15.5, 500000),
        ('Сидорова Анна Сергеевна', 'Смирнов Алексей Владимирович', 24, 12.0, 1000000),
        ('Козлов Дмитрий Николаевич', 'Иванова Елена Михайловна', 6, 18.5, 300000),
        ('Морозова Ольга Петровна', 'Петров Петр Петрович', 36, 10.0, 2000000),
        ('Васильев Сергей Андреевич', 'Смирнов Алексей Владимирович', 18, 14.0, 750000),
        ('Новикова Татьяна Павловна', 'Иванова Елена Михайловна', 24, 13.5, 850000),
        ('Федоров Артем Викторович', 'Петров Петр Петрович', 12, 16.0, 400000),
        ('Егорова Мария Владимировна', 'Смирнов Алексей Владимирович', 48, 9.5, 3000000),
        ('Андреев Павел Романович', 'Иванова Елена Михайловна', 6, 19.0, 250000),
        ('Павлова Светлана Максимовна', 'Петров Петр Петрович', 30, 11.0, 1500000)
    ]
    for client in sample_clients:
        add_client(client)

def display_table():
    clients = get_all_clients()
    print("\n" + "-"*80)
    print(f"{'ID':<3} {'ФИО клиента':<25} {'ФИО сотрудника':<25} {'Срок':<5} {'%':<6} {'Сумма':<10}")
    print("-"*80)
    for c in clients:
        print(f"{c[0]:<3} {c[1]:<25} {c[2]:<25} {c[3]:<5} {c[4]:<6.1f} {c[5]:<10.0f}")
    print("-"*80)

def safe_int(value):
    try:
        return int(value)
    except ValueError:
        print("Ошибка: нужно ввести целое число!")
        return None

def safe_float(value):
    try:
        return float(value)
    except ValueError:
        print("Ошибка: нужно ввести число!")
        return None

def main():
    create_table()
    
    if len(get_all_clients()) == 0:
        init_sample_data()
    
    while True:
        print("\n" + "="*60)
        print("БАНКОВСКАЯ СИСТЕМА - ВЫДАЧА КРЕДИТОВ")
        print("="*60)
        print("1. Показать всех клиентов")
        print("2. Добавить нового клиента")
        print("3. Поиск клиентов")
        print("4. Удалить клиента")
        print("5. Редактировать данные клиента")
        print("6. Выход")
        
        choice = input("\nВыберите действие: ")
        
        if choice == '1':
            display_table()
        
        elif choice == '2':
            fio_client = input("ФИО клиента: ")
            fio_employee = input("ФИО сотрудника банка: ")
            
            term = None
            while term is None:
                term = safe_int(input("Срок кредита (месяцев): "))
            
            percent = None
            while percent is None:
                percent = safe_float(input("Процент кредита: "))
            
            amount = None
            while amount is None:
                amount = safe_float(input("Сумма кредита: "))
            
            add_client((fio_client, fio_employee, term, percent, amount))
            print("Клиент добавлен!")
        
        elif choice == '3':
            print("\nИскать по:")
            print("1. ФИО клиента")
            print("2. ФИО сотрудника")
            print("3. Сумма кредита больше")
            search_choice = input("Выберите вариант: ")
            search_value = input("Введите значение: ")
            results = search_clients(search_choice, search_value)
            if results:
                print("\nНайденные клиенты:")
                for c in results:
                    print(f"ID: {c[0]}, {c[1]}, Сотрудник: {c[2]}, Срок: {c[3]}, %: {c[4]}, Сумма: {c[5]}")
            else:
                print("Ничего не найдено")
        
        elif choice == '4':
            print("\nУдалить по:")
            print("1. ID")
            print("2. ФИО клиента")
            print("3. Сумма кредита меньше")
            delete_choice = input("Выберите вариант: ")
            delete_value = input("Введите значение: ")
            
            if delete_choice == '1':
                delete_value = safe_int(delete_value)
                if delete_value is None:
                    continue
            elif delete_choice == '3':
                delete_value = safe_float(delete_value)
                if delete_value is None:
                    continue
            
            deleted = delete_client(delete_choice, delete_value)
            print(f"Удалено записей: {deleted}")
        
        elif choice == '5':
            display_table()
            client_id = safe_int(input("Введите ID клиента для редактирования: "))
            if client_id is None:
                continue
            
            print("\nЧто редактировать?")
            print("1. Срок кредита")
            print("2. Процент кредита")
            print("3. Сумму кредита")
            update_choice = input("Выберите вариант: ")
            
            new_value = None
            if update_choice == '1':
                new_value = safe_int(input("Новый срок кредита: "))
            elif update_choice == '2':
                new_value = safe_float(input("Новый процент: "))
            elif update_choice == '3':
                new_value = safe_float(input("Новая сумма: "))
            
            if new_value is not None:
                updated = update_client(update_choice, new_value, client_id)
                print(f"Обновлено записей: {updated}")
        
        elif choice == '6':
            print("До свидания!")
            break
        
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()
