import sqlite3   # Импорт модуля для работы с базой данных SQLite
import csv       # Импорт модуля для чтения CSV-файлов
import re        # Импорт модуля регулярных выражений для валидации данных

# Подключение к базе данных (если файл не существует — будет создан)
conn = sqlite3.connect("phonebook.db")
cursor = conn.cursor()

# Создание таблицы пользователей, если она ещё не существует
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,                 -- Уникальный ID (автоинкремент)
    name TEXT NOT NULL,                     -- Имя пользователя
    phone VARCHAR(20) NOT NULL UNIQUE,      -- Телефон (уникален)
    email TEXT NOT NULL UNIQUE,             -- Email (уникален)
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Дата и время создания записи
)
""")
conn.commit()  # Подтверждение изменений

# ✅ Добавление одного пользователя
def add_user():
    name = input("Name: ")
    phone = input("Number: ")
    email = input("Email: ")
    
    # Проверка: существует ли пользователь с таким именем
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    user = cursor.fetchone() #получить одну строку результат
    
    if user:
        # Если найден — обновить телефон
        cursor.execute("UPDATE users SET phone = ? WHERE name = ?", (phone, name))
        print("🔄 Phone number updated for existing user.")
    else:
        # Если не найден — добавить нового
        cursor.execute("INSERT INTO users (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        print("✅ New user was added.")
    
    conn.commit()

# ✅ Добавление нескольких пользователей с валидацией
def add_users():
    print("How many users u will add?")
    num = int(input())  # Ввод количества
    for i in range(num):
        pattern = r"\d{12}"           # Шаблон: 12 цифр (например, 87001112233)
        pattern2 = r".+@.+\..+"       # Шаблон простого email

        name = input("Name: ")
        phone = input("Number: ")
        check = re.search(pattern, phone)  # Проверка телефона
        
        while not check:
            print("Incorrect phone number please try again")
            phone = input("Number: ")
            check = re.search(pattern, phone)
            
        email = input("Email: ")
        check2 = re.search(pattern2, email)  # Проверка email
        
        while not check2:
            print("Incorrect email please try again")
            email = input("Email: ")
            check2 = re.search(pattern2, email)
        
        # Вставка в базу
        cursor.execute("INSERT INTO users (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        print("✅ New user was added.")
    
    conn.commit()  # Подтверждение

# ✅ Загрузка пользователей из CSV-файла
def upload_from_csv():
    file_path = input("Enter the CSV file path: ")
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Пропуск заголовков (если есть)
            for row in csvreader:
                if len(row) == 3:  # Проверка, что в строке 3 значения
                    name, phone, email = row
                    cursor.execute("INSERT INTO users (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
            conn.commit()
            print("✅ Data uploaded from CSV.")
    except Exception as e:
        print(f"❌ Error: {e}")

# ✅ Показать всех пользователей
def show_users():
    cursor.execute("SELECT * FROM users")  # Получить всех
    users = cursor.fetchall()
    print("\n📋 All Users:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Phone: {user[2]}, Email: {user[3]}")
    print()

# ✅ Показать пользователей с пагинацией (LIMIT + OFFSET)
def show_some_users():
    print("Enter number of users per page (LIMIT): ")
    limit = int(input())
    print("Enter page number (starting from 1):")
    page = int(input())
    
    offset = (page - 1) * limit  # Вычисление смещения

    cursor.execute("SELECT * FROM users LIMIT ? OFFSET ?", (limit, offset))
    users = cursor.fetchall()

    print("\n📋 Limited Users:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Phone: {user[2]}, Email: {user[3]}")
    print()

# ✅ Поиск по имени
def show_users_by_name(name):
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Phone: {user[2]}, Email: {user[3]}")
    print()
    
# ✅ Поиск по телефону
def show_users_by_phone(phone):
    cursor.execute("SELECT * FROM users WHERE phone = ?", (phone,))
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Phone: {user[2]}, Email: {user[3]}")
    print()

# ✅ Обновление телефона по email
def update_user():
    email = input("Input your email to change your number: ")
    new_phone = input("New phone number: ")
    cursor.execute("UPDATE users SET phone = ? WHERE email = ?", (new_phone, email))
    conn.commit()
    print("🔁 Phone number was updated.")

# ✅ Удаление пользователя по номеру
def delete_user_by_phone(phone):
    cursor.execute("DELETE FROM users WHERE phone = ?", (phone,))
    conn.commit()
    print("❌ User was deleted.")

# ✅ Удаление пользователя по имени
def delete_user_by_name(name):
    cursor.execute("DELETE FROM users WHERE name = ?", (name,))
    conn.commit()
    print("❌ User was deleted.")

# 📌 Главное меню
def main_menu():
    while True:
        print("\n📌 Menu:")
        print("1. Add user")
        print("2. Show all users")
        print("3. Update phone number of a user")
        print("4. Delete a user by phone")
        print("5. Upload users from CSV")
        print("6. Show a user")
        print("7. Add multiple users")
        print("8. Show limited users")
        print("0. Exit")

        choice = input("Choose action: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            show_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            phone = input("Enter the phone number to delete user: ")
            delete_user_by_phone(phone)
        elif choice == "5":
            upload_from_csv()
        elif choice == "6":
            pattern = input()
            if pattern.isalpha():  # Проверка: только буквы (проверка имени)
                show_users_by_name(pattern)
                show_users_by_phone(pattern)  # Можно было бы разделить
            else:
                print("Sorry, there is no match")
        elif choice == "7":
            add_users()
        elif choice == "8":
            show_some_users()
        elif choice == "0":
            print("👋 Exit...")
            break
        else:
            print("Wrong option, try again")

# ▶️ Запуск главного меню
main_menu()

# ❎ Закрытие соединения с базой данных при выходе
conn.close()
