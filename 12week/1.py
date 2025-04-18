import sqlite3
import csv
import re

# Connection
conn = sqlite3.connect("phonebook.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

#Add user
def add_user():
    name = input("Name: ")
    phone = input("Number: ")
    email = input("Email: ")
    
    # Проверим, существует ли пользователь с таким именем
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    user = cursor.fetchone()
    
    if user:
        cursor.execute("UPDATE users SET phone = ? WHERE name = ?", (phone, name))
        print("🔄 Phone number updated for existing user.")
    else:
        cursor.execute("INSERT INTO users (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        print("✅ New user was added.")
    
    conn.commit()


#Add users
def add_users():
    print("How many users u will add?")
    num = int(input())
    for i in range(num):
        pattern = r"\d{12}"
        pattern2 = r".+@.+\..+"
        name = input("Name: ")
        phone = input("Number: ")
        check = re.search(pattern, phone)
        
        while not check:
            print("Incorrect phone number please try again")
            phone = input("Number: ")
            check = re.search(pattern, phone)
            
        email = input("Email: ")
        check2 = re.search(pattern2, email)
        
        while not check2:
            print("Incorrect email please try again")
            email = input("Email: ")
            check2 = re.search(pattern2, email)
        
        cursor.execute("INSERT INTO users (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        print("✅ New user was added.")
    
    conn.commit()
    

# Upload data from CSV file
def upload_from_csv():
    file_path = input("Enter the CSV file path: ")
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip header row if present
            for row in csvreader:
                if len(row) == 3:  # Ensure row has 3 columns
                    name, phone, email = row
                    cursor.execute("INSERT INTO users (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
            conn.commit()
            print("✅ Data uploaded from CSV.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Show all users
def show_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("\n📋 All Users:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Phone: {user[2]}, Email: {user[3]}")
    print()

# Show some users
def show_some_users():
    print("Enter number of users per page (LIMIT): ")
    num = int(input())
    print("Enter page number (starting from 1):")
    num2 = int(input())
    cursor.execute("SELECT * FROM users LIMIT ? OFFSET ?",((num, num2)))
    users = cursor.fetchall()
    print("\n📋 Limited Users:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Phone: {user[2]}, Email: {user[3]}")
    print()

# Show users by name (Filter example)
def show_users_by_name(name):
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Phone: {user[2]}, Email: {user[3]}")
    print()
    
# Show users by name (Filter example)
def show_users_by_phone(phone):
    cursor.execute("SELECT * FROM users WHERE phone = ?", (phone,))
    users = cursor.fetchall()
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Phone: {user[2]}, Email: {user[3]}")
    print()


# Update phone number
def update_user():
    email = input("Input your email to change your number: ")
    new_phone = input("New phone number: ")
    cursor.execute("UPDATE users SET phone = ? WHERE email = ?", (new_phone, email))
    conn.commit()
    print("🔁 Phone number was updated.")

# Delete user by phone
def delete_user_by_phone(phone):
    cursor.execute("DELETE FROM users WHERE phone = ?", (phone,))
    conn.commit()
    print("❌ User was deleted.")

# Delete user by name
def delete_user_by_name(name):
    cursor.execute("DELETE FROM users WHERE name = ?", (name,))
    conn.commit()
    print("❌ User was deleted.")

# Main menu
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
            if pattern.isalpha():
                show_users_by_name(pattern)
                show_users_by_phone(pattern)
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

# Run the menu
main_menu()

# Close connection on exit
conn.close()
