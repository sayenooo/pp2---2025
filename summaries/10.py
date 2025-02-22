"""
Лекция L10: Databases

Темы:
  - Сохранение данных в базу данных.
  - Чтение данных из базы данных.
  - Обновление и удаление данных из базы данных.

В данном конспекте используется модуль sqlite3, встроенный в Python.
"""

import sqlite3

def create_connection(db_file):
    """
    Создает соединение с базой данных SQLite.

    Аргументы:
        db_file (str): Путь к файлу базы данных.
    
    Возвращает:
        Объект соединения (Connection) или None в случае ошибки.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Соединение с базой данных установлено.")
    except sqlite3.Error as e:
        print("Ошибка при подключении к базе данных:", e)
    return conn

def create_table(conn):
    """
    Создает таблицу 'users' если она не существует.

    Таблица 'users' содержит:
      - id: INTEGER PRIMARY KEY
      - name: TEXT NOT NULL
      - age: INTEGER
    """
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        conn.commit()
        print("Таблица 'users' создана или уже существует.")
    except sqlite3.Error as e:
        print("Ошибка при создании таблицы:", e)

def insert_data(conn, user):
    """
    Вставляет данные в таблицу 'users'.

    Аргументы:
        conn (sqlite3.Connection): Соединение с базой данных.
        user (tuple): Кортеж с данными пользователя (name, age).
    """
    try:
        sql_insert = "INSERT INTO users (name, age) VALUES (?, ?)"
        cursor = conn.cursor()
        cursor.execute(sql_insert, user)
        conn.commit()
        print(f"Данные вставлены: {user}")
    except sqlite3.Error as e:
        print("Ошибка при вставке данных:", e)

def read_data(conn):
    """
    Читает все данные из таблицы 'users' и выводит их на экран.
    """
    try:
        sql_select = "SELECT * FROM users"
        cursor = conn.cursor()
        cursor.execute(sql_select)
        rows = cursor.fetchall()
        print("Содержимое таблицы 'users':")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print("Ошибка при чтении данных:", e)

def update_data(conn, user_id, new_age):
    """
    Обновляет значение возраста для пользователя с заданным id.

    Аргументы:
        conn (sqlite3.Connection): Соединение с базой данных.
        user_id (int): Идентификатор пользователя.
        new_age (int): Новое значение возраста.
    """
    try:
        sql_update = "UPDATE users SET age = ? WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(sql_update, (new_age, user_id))
        conn.commit()
        print(f"Обновлен возраст пользователя с id {user_id}: новый возраст = {new_age}")
    except sqlite3.Error as e:
        print("Ошибка при обновлении данных:", e)

def delete_data(conn, user_id):
    """
    Удаляет данные пользователя с заданным id из таблицы 'users'.

    Аргументы:
        conn (sqlite3.Connection): Соединение с базой данных.
        user_id (int): Идентификатор пользователя.
    """
    try:
        sql_delete = "DELETE FROM users WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(sql_delete, (user_id,))
        conn.commit()
        print(f"Пользователь с id {user_id} удален.")
    except sqlite3.Error as e:
        print("Ошибка при удалении данных:", e)

def main():
    database = "example.db"

    # Создаем соединение с базой данных
    conn = create_connection(database)
    if conn is not None:
        # Создаем таблицу, если она не существует
        create_table(conn)

        # Вставка данных в таблицу
        insert_data(conn, ("Alice", 30))
        insert_data(conn, ("Bob", 25))

        # Чтение данных из таблицы
        read_data(conn)

        # Обновление данных: изменяем возраст пользователя с id 1
        update_data(conn, 1, 31)
        read_data(conn)

        # Удаление данных: удаляем пользователя с id 2
        delete_data(conn, 2)
        read_data(conn)

        # Закрываем соединение с базой данных
        conn.close()
    else:
        print("Не удалось установить соединение с базой данных.")

if __name__ == "__main__":
    main()
