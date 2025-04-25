# -------------------- imports --------------------
import psycopg2                         # Библиотека для подключения к PostgreSQL
import csv                              # Модуль для работы с CSV-файлами
from psycopg2.extensions import register_adapter

# Регистрируем адаптер для list, чтобы можно было передавать списки в запросы как массивы PostgreSQL
register_adapter(list, psycopg2._psycopg.AsIs)

# -------------------- DB connect -----------------
def connect():
    try:
        # Подключение к базе данных phonebook
        conn = psycopg2.connect(
            dbname="phonebook",
            user="postgres",
            password="2006",
            host="localhost",
            port="5432"
        )
        return conn, conn.cursor()     # Возвращаем соединение и курсор
    except Exception as e:
        print("Database connection error:", e)
        exit()

# -------------------- CRUD wrappers --------------
def insert_from_console(cur, conn):
    # Добавление пользователя вручную через консоль
    name  = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("Done: inserted or updated.")

def insert_from_csv(cur, conn, filename):
    # Загрузка пользователей из CSV файла
    try:
        names, phones = [], []
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)        # Пропускаем заголовок
            for name, phone in reader:
                names.append(name)
                phones.append(phone)

        # Вызываем процедуру вставки множества пользователей
        cur.execute("CALL bulk_insert_users(%s::text[], %s::text[], NULL)", (names, phones))
        bad = cur.fetchone()[0]       # Получаем список ошибочных записей
        conn.commit()

        if bad:
            print("❗ Incorrect rows skipped:")
            for row in bad:
                print("  ", row)
        else:
            print("CSV loaded successfully.")
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print("Error when working with CSV:", str(e))

def update_user(cur, conn, name, new_name=None, new_phone=None):
    # Обновление имени и/или номера телефона пользователя
    if new_name:
        cur.execute("UPDATE phonebook SET username=%s WHERE username=%s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone=%s WHERE username=%s", (new_phone, name))
    conn.commit()
    print("The record has been updated.")

def search_user(cur, value):
    # Поиск пользователя по имени или телефону
    cur.execute("SELECT * FROM phonebook WHERE username=%s OR phone=%s", (value, value))
    for row in cur.fetchall():
        print(row) if row else print("No records were found.")

def delete_user(cur, conn, value):
    # Удаление пользователя по имени или телефону
    cur.execute("CALL delete_user_by_value(%s)", (value,))
    conn.commit()
    print("Deleted (if existed).")

def show_all(cur):
    # Отображение всех записей из phonebook
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print("\n📋 All entries:") if rows else print("The table is empty.")
    for r in rows:
        print(r)

def search_by_pattern(cur):
    # Поиск по шаблону (например, часть имени или телефона)
    pattern = input("Enter a search pattern (e.g. 'John'): ")
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    for r in rows:
        print(r) if rows else print("No matches found.")

def show_page(cur):
    # Постраничный вывод записей (пагинация)
    limit  = int(input("Limit: "))
    offset = int(input("Offset: "))
    cur.execute("SELECT * FROM get_page(%s,%s)", (limit, offset))
    rows = cur.fetchall()
    for r in rows:
        print(r) if rows else print("No rows on this page.")

# -------------------- main menu ------------------
def main():
    # Главное меню программы
    conn, cur = connect()
    try:
        while True:
            print("\n--- PhoneBook ---")
            print("1. Add an entry (manually)")
            print("2. Add from CSV")
            print("3. Update the record")
            print("4. Find an entry")
            print("5. Delete the entry")
            print("6. Show the entire table")
            print("7. Search by pattern")
            print("8. Show page (pagination)")
            print("0. Exit")

            choice = input("Select an action: ")

            if choice == "1":
                insert_from_console(cur, conn)
            elif choice == "2":
                file = input("CSV file name: ")
                insert_from_csv(cur, conn, file)
            elif choice == "3":
                name = input("Enter a name for the update: ")
                new_name  = input("New name (Enter to skip): ") or None
                new_phone = input("New phone (Enter to skip): ") or None
                update_user(cur, conn, name, new_name, new_phone)
            elif choice == "4":
                val = input("Name or phone to search: ")
                search_user(cur, val)
            elif choice == "5":
                val = input("Name or phone to delete: ")
                delete_user(cur, conn, val)
            elif choice == "6":
                show_all(cur)
            elif choice == "7":
                search_by_pattern(cur)
            elif choice == "8":
                show_page(cur)
            elif choice == "0":
                print("Good‑bye!")
                break
            else:
                print("Wrong choice. Try again.")
    finally:
        # Закрываем соединение с базой данных
        cur.close()
        conn.close()

# Точка входа в программу
if __name__ == "__main__":
    main()
