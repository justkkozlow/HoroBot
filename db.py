import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('horo.db')
cursor = conn.cursor()

# Создание таблицы для хранения информации о пользователях
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        sign TEXT
    )
''')
conn.commit()


# Функция сохранения знака зодиака пользователя в базе данных
def save_zodiac_sign(user_id, sign):
    # Проверка наличия связки user_id и sign в базе данных
    cursor.execute('SELECT id, sign FROM users WHERE id=? AND sign=?', (user_id, sign))
    existing_data = cursor.fetchone()

    if existing_data:
        # Если связка уже существует, пропустить сохранение
        return

    # Сохранение информации о выбранном знаке зодиака в базе данных
    cursor.execute('''
        INSERT INTO users (id, sign) VALUES (?, ?)
        ON CONFLICT (id) DO UPDATE SET sign=excluded.sign
    ''', (user_id, sign))
    conn.commit()
