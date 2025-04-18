import sqlite3   # Импорт модуля для работы с базой данных SQLite
import csv       # Импорт модуля для чтения CSV-файлов
import re 

conn = sqlite3.connect("book.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name VARCHAR(20),
    surename VARCHAR(20),
    identity CHAR,
    phone INTEGER UNIQUE,
    job VARCHAR(100),
    salary INTEGER) 
"""
)
conn.commit()

def add():
    print("name:")
    name = input()
    print("surename")
    surename = input()
    print("identity:")
    identity = input()
    pattern = r"f*m*"
    check = re.search(pattern, identity)
    if identity!='f' or identity!='m':
        while not check:
           identity = input()
           check = re.search(pattern, identity)
           print("pls, type a valid form (f or m)")
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
            print("pls, type a valid form 12 digits, starting from 77")
            phone = int(phone)
    print("job:")
    job = input()
    print("salary:")
    salary = int(input())
    
    cursor.execute("INSERT INTO employees (name, surename, identity, phone, job, salary) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, surename, identity, phone, job, salary))
    print("\t")
    conn.commit()

def upload():
    path = input("enter the csv file path:")
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row)==6:
                name, surename, identity, phone, job, salary = row
                cursor.execute("INSERT INTO employees (name, surename, identity, phone, job, salary) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, surename, identity, phone, job, salary))
conn.commit()

def show_all():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    print("all employees:")
    for employee in employees:
        print(f"id: {employee[0]}, name: {employee[1]}, surename: {employee[2]}, identity: {employee[3]}, phone: {employee[4]}, job: {employee[5]}, salary: {employee[6]} ")
    print("\t")
    
def show_fm():
    print("choose identity (m or f):")
    identity = input()
    i = identity
    cursor.execute("SELECT * FROM employees WHERE identity = ? ", (identity,))
    employees = cursor.fetchall()
    if i == 'f':
        i = "female"
    elif i == 'm':
        i = "male"  
    print(f"all {i} employees:")
    for employee in employees:
        print(f"id: {employee[0]}, name: {employee[1]}, surename: {employee[2]}, identity: {employee[3]}, phone: {employee[4]}, job: {employee[5]}, salary: {employee[6]} ")
    print("\t")

def show():
    print("choose name:")
    name = input()
    cursor.execute("SELECT * FROM employees WHERE name = ? ", (name,))
    employees = cursor.fetchall()
    print("matched employees:")
    for employee in employees:
        print(f"id: {employee[0]}, name: {employee[1]}, surename: {employee[2]}, identity: {employee[3]}, phone: {employee[4]}, job: {employee[5]}, salary: {employee[6]} ")
    print("\t")    
        
def update():
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
    cursor.execute("UPDATE employees SET phone = ? WHERE name = ? AND surename = ?",
                   (phone, name, surename))
    print("phone number was updated successfully")
    print("\t")
    conn.commit()
    
def delete():
    print("input name:")
    name = input()
    print("input surename:")
    surename = input()
    cursor.execute("DELETE * employees WHERE name = ? AND surename = ?",
                   (name, surename))
    print("an employee was deleted successfully")
    print("\t")
    conn.commit()
    
def limit():
    print("limit:")
    limit = int(input())
    print("offset (starting page)")
    offset = int(input())
    cursor.execute("SELECT * FROM employees LIMIT ? OFFSET ?",
                   ((limit, offset)))
    employees = cursor.fetchall()
    print("matched employees:")
    for employee in employees:
        print(f"id: {employee[0]}, name: {employee[1]}, surename: {employee[2]}, identity: {employee[3]}, phone: {employee[4]}, job: {employee[5]}, salary: {employee[6]} ")
    print("\t")    
    conn.commit()
  

def menu():
    while True:
        print("menu:")
        print("Select operation, that u want to commit:")
        print("0 - exit")
        print("1 - add employee")
        print("2 - upload employees from csv file")
        print("3 - show all employees")
        print("4 - show all male or female employees")
        print("5 - show employees by name")
        print("6 - update phone number")
        print("7 - delete employee")
        print("8 - show limited employees")
        
        operation = int(input())   
        
        if operation == 1:
            add()
        elif operation == 2:
            upload()
        elif operation == 3:
            show_all()
        elif operation == 4:
            show_fm()
        elif operation == 5:
            show()
        elif operation == 6:
            update()
        elif operation == 7:
            delete()
        elif operation == 8:
            limit()
        elif operation == 0:
            print("see u soon")
            break
        else:
            print("error")
            
menu()
        
conn.close()    

