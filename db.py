import sqlite3
import config

# Подключение к базе данных
conn = sqlite3.connect(config.DB)
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



# # Функция для отправки гороскопа
# async def send_horoscope():
#     # Получение текущей даты и времени
#     current_time = datetime.now()
#
#     # Получение всех пользователей из базы данных
#     cursor.execute('SELECT id, sign FROM users')
#     users = cursor.fetchall()
#
#     for user in users:
#         user_id = user[0]
#         sign = user[1]
#
#         # Отправка гороскопа пользователю
#         await bot.send_message(user_id, f"Ваш гороскоп на сегодня ({current_time.strftime('%Y-%m-%d')}): ...")
#
#     # Планирование повторной отправки гороскопа через 24 часа
#     next_time = current_time + timedelta(days=1)
#     dp.loop.call_later(86400, send_horoscope)