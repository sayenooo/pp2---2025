import sqlite3
import csv

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

# Add user
def add_user():
    name = input("Name: ")
    phone = input("Number: ")
    email = input("Email: ")
    cursor.execute("INSERT INTO users (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    print("✅ User was added.")

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

# Show users by name (Filter example)
def show_users_by_name(name):
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
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
        elif choice == "0":
            print("👋 Exit...")
            break
        else:
            print("Wrong option, try again")

# Run the menu
main_menu()

# Close connection on exit
conn.close()
