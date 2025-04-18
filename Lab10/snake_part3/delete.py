import sqlite3

conn = sqlite3.connect("snake_game.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM user_score")  # Удаляет все результаты
cursor.execute("DELETE FROM user")        # Удаляет всех пользователей
conn.commit()

conn.close()
print("Все пользователи и их результаты удалены.")