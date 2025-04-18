# Библиотеки для работы с PostgreSQL и для чтения CSV-файлов
import psycopg2 
import csv 

# Функция подключения к базе данных
def connect():
    try:
        conn = psycopg2.connect(
            dbname="phonebook",     # Имя базы данных
            user="postgres",        # Имя пользователя PostgreSQL
            password="2006",        # Пароль от PostgreSQL
            host="localhost",       # Локальный сервер
            port="5432"             # Стандартный порт PostgreSQL
        )
        return conn, conn.cursor()  # Возвращаем соединение и курсор для выполнения SQL
    except Exception as e:
        print("Database connection error:", e)
        exit()

# Ввод записи вручную через консоль
def insert_from_console(cur, conn):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    # Добавляем запись в таблицу
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()  # Сохраняем изменения в базе
    print("The entry has been added.")

# Загрузка данных из CSV-файла
def insert_from_csv(cur, conn, filename):
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)  # Пропускаем заголовок, если он есть
            for row in reader:
                if len(row) >= 2:
                    # Вставляем каждую строку (имя и номер)
                    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
            conn.commit()
            print("The CSV data has been successfully added.") # Данные из CSV успешно добавлены.
    except FileNotFoundError:
        print("The file was not found.") # Файл не найден.
    except Exception as e:
        print("Error when working with CSV:", str(e)) # Ошибка при работе с CSV:

# Обновление имени и/или номера по имени пользователя
def update_user(cur, conn, name, new_name=None, new_phone=None):
    if new_name:
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, name))
    conn.commit()
    print("The record has been updated.") # Запись была обновлена.

# Поиск по имени или телефону
def search_user(cur, value):
    cur.execute("SELECT * FROM phonebook WHERE username = %s OR phone = %s", (value, value))
    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No records were found.") # Записи не найдены.

# Удаление записи по имени или номеру
def delete_user(cur, conn, value):
    cur.execute("DELETE FROM phonebook WHERE username = %s OR phone = %s", (value, value))
    conn.commit()
    print("The record has been deleted (if found).") # Запись удалена (если была найдена).

# Показать все записи в таблице
def show_all(cur):
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    if rows:
        print("\n📋 All entries in the PhoneBook:") # Все записи в телефонной книге:
        for row in rows:
            print(row)
    else:
        print("The table is empty.") # Таблица пуста.

# Главное меню, где пользователь выбирает действия
def main():
    conn, cur = connect()  # Подключение к БД
    try:
        while True:
            print("\n--- Welcome to the PhoneBook! ---") # 
            print("1. Add an entry (manually)") # 1. Добавить запись (вручную)
            print("2. Add from CSV") # 2. Добавить из CSV
            print("3. Update the record") # 3. Обновить запись
            print("4. Find an entry") # 4. Найти запись
            print("5. Delete the entry") # 5. Удалить запись
            print("6. Show the entire table") # 6. Показать всю таблицу
            print("0. Exit") # 0. Выход

            choice = input("Select an action: ") # Выберите действие: 

            # Обработка выбора пользователя
            if choice == "1":
                insert_from_console(cur, conn)
            elif choice == "2":
                filename = input("Enter the name of the CSV file (for example, data.csv): ") # Введите имя CSV-файла (например, data.csv): 
                insert_from_csv(cur, conn, filename)
            elif choice == "3":
                name = input("Enter a name for the update: ") # Введите имя для обновления: 
                new_name = input("New name (or Enter to skip): ") # Новое имя (или Enter, чтобы пропустить): 
                new_phone = input("New number (or Enter to skip): ") # Новый номер (или Enter, чтобы пропустить):
                update_user(cur, conn, name, new_name if new_name else None, new_phone if new_phone else None)
            elif choice == "4":
                value = input("Enter a name or number to search for: ") # Введите имя или номер для поиска: 
                search_user(cur, value)
            elif choice == "5":
                value = input("Enter a name or number to delete: ") #  Введите имя или номер для удаления: 
                delete_user(cur, conn, value)
            elif choice == "6":
                show_all(cur)
            elif choice == "0":
                print("Exit the program.") # Выход из программы.
                break
            else:
                print("Wrong choice. Try again.") # Неверный выбор. Попробуйте снова.
    finally:
        cur.close()
        conn.close()  # Закрываем соединение с БД

# Запускаем программу, если файл выполняется как скрипт
if __name__ == "__main__":
    main()
