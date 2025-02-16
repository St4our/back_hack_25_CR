import sqlite3

db_path = "database.db"  # Укажите путь к вашей базе

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Добавляем новый столбец cords в таблицу fighters
cursor.execute("ALTER TABLE fighters ADD COLUMN cords TEXT;")

conn.commit()
conn.close()

print("Миграция завершена: добавлен столбец cords")
