import psycopg2
import csv
import re
from config import load_config

# Создание таблиц, если не существует
def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(20),
            surename VARCHAR(20),
            identity CHAR,
            phone VARCHAR UNIQUE,
            job VARCHAR(100),
            salary VARCHAR,
            email TEXT NOT NULL UNIQUE,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

# Добавление пользователя
def add(cursor,conn):
    print("name:")
    name = input()
    print("surename")
    surename = input()
    print("identity:")
    identity = input()
    if identity not in ('f', 'm'):
        while identity not in ('f', 'm'):
            print("pls, type a valid form (f or m)")
            identity = input()
    print("phone number:")
    phone = input()
    pattern1 = r"^77\d{9}$"
    check1 = re.search(pattern1, phone)
    if len(phone)!=11:
        print("pls, there should be 11 digits")
    if not check1:
        while not check1:
            phone = input()
            check1 = re.search(pattern1, phone)
            if not check1:
                print("pls, type a valid form 12 digits, starting from 77")
                
    print("job:")
    job = input()
    print("salary:")
    salary = input()
    print("email:")
    email = input()
    pattern2 = r".+\@.+\..+"
    check2 = re.search(pattern2, email)
    if not check2:
        while not check2:
           email = input()
           check2 = re.search(pattern2, email)
           if not check2:
            print("pls, input a valid form of email")
    
    cursor.execute("SELECT * FROM users WHERE name = %s AND surename = %s",(name,surename))
    user = cursor.fetchone()
    if user:
        cursor.execute("UPDATE users SET phone = %s  WHERE name = %s AND surename = %s",(phone,name,surename))
        print(f"user {name} {surename} added with phone {phone}.")
    else:
        cursor.execute("INSERT INTO users (name, surename, identity, phone, job, salary, email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (name, surename, identity, phone, job, salary, email))
        print(f"new user was added successfully.")
    print("\t")
    conn.commit()


def add_m(cursor,conn):
    print("enter number, how many users u will input?")
    num = int(input())
    for i in range(num):
        print("name:")
        name = input()
        print("surename")
        surename = input()
        print("identity:")
        identity = input()
        if identity not in ('f', 'm'):
            while identity not in ('f', 'm'):
                print("pls, type a valid form (f or m)")
                identity = input()
        print("phone number:")
        phone = input()
        pattern1 = r"^77\d{9}$"
        check1 = re.search(pattern1, phone)
        if len(phone)!=11:
            print("pls, there should be 11 digits")
        if not check1:
            while not check1:
                phone = input()
                check1 = re.search(pattern1, phone)
                if not check1:
                    print("pls, type a valid form 12 digits, starting from 77")
        print("job:")
        job = input()
        print("salary:")
        salary = input()
        print("email:")
        email = input()
        pattern2 = r".+\@.+\..+"
        check2 = re.search(pattern2, email)
        if not check2:
            while not check2:
                email = input()
                check2 = re.search(pattern2, email)
                if not check2:
                    print("pls, input a valid form of email")
    
        cursor.execute("SELECT * FROM users WHERE name = %s AND surename = %s",(name,surename))
        user = cursor.fetchone()
        if user:
            cursor.execute("UPDATE users SET phone = %s  WHERE name = %s AND surename = %s",(phone,name,surename))
            print(f"user {name} {surename} added with phone {phone}.")
        else:
            cursor.execute("INSERT INTO users (name, surename, identity, phone, job, salary, email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (name, surename, identity, phone, job, salary, email))
            print(f"new user was added successfully.")
        print("\t")
    conn.commit()
    
# Загрузка из CSV
def upload(cursor, conn):
    path = input("enter the CSV file path: ")
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропустить заголовок
        for row in reader:
            if len(row) == 7:  # Убедиться, что в строке 7 значений
                name, surename, identity, phone, job, salary, email = row

                cursor.execute(
                    "INSERT INTO users (name, surename, identity, phone, job, salary, email) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (name, surename, identity, phone, job, salary, email)
                )
        conn.commit()
        print("data successfully uploaded.")




def show_all(cursor,conn):
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("all users:")
    for user in users:
        print(f"id: {user[0]}, name: {user[1]}, surename: {user[2]}, identity: {user[3]}, phone: {user[4]}, job: {user[5]}, salary: {user[6]}, email: {user[7]}, date: {user[8]}   ")
    print("\t")
    conn.commit()
    
def show_fm(cursor,conn):
    print("choose identity (m or f):")
    identity = input()
    cursor.execute("SELECT * FROM users WHERE identity = %s ", (identity,))
    users = cursor.fetchall() 
    print(f"all {identity}ale users:")
    for user in users:
        print(f"id: {user[0]}, name: {user[1]}, surename: {user[2]}, identity: {user[3]}, phone: {user[4]}, job: {user[5]}, salary: {user[6]}, email: {user[7]}, date: {user[8]}   ")
    print("\t")
    conn.commit()

def show(cursor,conn):
    print("choose name:")
    name = input()
    cursor.execute("SELECT * FROM users WHERE name = %s ", (name,))
    users = cursor.fetchall()
    print("matched users:")
    for user in users:
        print(f"id: {user[0]}, name: {user[1]}, surename: {user[2]}, identity: {user[3]}, phone: {user[4]}, job: {user[5]}, salary: {user[6]}, email: {user[7]}, date: {user[8]}   ")
    print("\t")
    conn.commit() 
        
def update(cursor,conn):
    print("input name:")
    name = input()
    print("input surename:")
    surename = input()
    print("input updated phone number:")
    phone = input()
    pattern1 = r"^77\d{9}$"
    check1 = re.search(pattern1, phone)
    if len(phone)!=11:
        print("pls, there should be 11 digits")
    if not check1:
        while not check1:
            phone = input()
            check1 = re.search(pattern1, phone)
            print("pls, type a valid form 12 digits, starting from 77")
    phone = int(phone)
    cursor.execute("UPDATE users SET phone = %s WHERE name = %s AND surename = %s",
                   (phone, name, surename))
    print("phone number was updated successfully")
    print("\t")
    conn.commit()
    
def delete(cursor,conn):
    print("input name:")
    name = input()
    print("input surename:")
    surename = input()
    cursor.execute("DELETE FROM users WHERE name = %s AND surename = %s",
                   (name, surename))
    print("user was deleted successfully")
    print("\t")
    conn.commit()
    
def limit(cursor,conn):
    print("limit:")
    limit = int(input())
    print("offset (starting page)")
    offset = int(input())
    cursor.execute("SELECT * FROM users LIMIT %s OFFSET %s",
                   (limit, offset))
    users = cursor.fetchall()
    print("matched users:")
    for user in users:
        print(f"id: {user[0]}, name: {user[1]}, surename: {user[2]}, identity: {user[3]}, phone: {user[4]}, job: {user[5]}, salary: {user[6]}, email: {user[7]}, date: {user[8]}   ")
    print("\t")
  

def menu(cursor,conn):
    while True:
        print("menu:")
        print("Select operation, that u want to commit:")
        print("0 - exit")
        print("1 - add user")
        print("2 - upload users from csv file")
        print("3 - show all users")
        print("4 - show all male or female users")
        print("5 - show users by name")
        print("6 - update phone number")
        print("7 - delete user")
        print("8 - show limited users")
        print("9 - add multiple users")
        
        operation = int(input())   
        
        if operation == 1:
            add(cursor,conn)
        elif operation == 2:
            upload(cursor,conn)
        elif operation == 3:
            show_all(cursor,conn)
        elif operation == 4:
            show_fm(cursor,conn)
        elif operation == 5:
            show(cursor,conn)
        elif operation == 6:
            update(cursor,conn)
        elif operation == 7:
            delete(cursor,conn)
        elif operation == 8:
            limit(cursor,conn)
        elif operation == 9:
            add_m(cursor,conn)
        
        elif operation == 0:
            print("see u soon")
            break
        else:
            print("error")




# Точка входа
def main():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                create_tables(cursor)
                menu(cursor, conn)
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    main()
