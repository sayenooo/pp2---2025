"""
Лекция L6: Работа с директориями и файлами, File Handling, 
Python Read/Write/Create/Delete Files, Working with Directories, 
и Python builtin functions

Темы:
  1. Python File Handling (Чтение, запись, создание, удаление файлов)
  2. Working with Directories (Работа с директориями)
  3. Python builtin functions (Встроенные функции Python)
"""

import os
import shutil

# ===============================
# 1. Python File Handling
# ===============================

def file_handling_demo():
    """
    Демонстрация основных операций с файлами:
      - Создание и запись в файл
      - Чтение файла
      - Удаление файла
    """
    filename = "example.txt"
    
    # --- Создание и запись в файл (Write/Create Files) ---
    content = "Это пример содержимого файла.\nСтрока 2.\nСтрока 3."
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Файл '{filename}' создан и записан.")
    
    # --- Чтение файла (Read Files) ---
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            read_content = f.read()
        print(f"\nСодержимое файла '{filename}':\n{read_content}")
    else:
        print(f"Файл '{filename}' не найден для чтения.")
    
    # --- Удаление файла (Delete Files) ---
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\nФайл '{filename}' удалён.")
    else:
        print(f"Файл '{filename}' не найден для удаления.")
    print()


# ===============================
# 2. Working with Directories
# ===============================

def directories_demo():
    """
    Демонстрация работы с директориями:
      - Создание директории
      - Переименование директории
      - Вывод содержимого текущей директории
      - Удаление директории
    """
    dir_name = "test_directory"
    
    # Создание директории, если она не существует
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"Директория '{dir_name}' создана.")
    else:
        print(f"Директория '{dir_name}' уже существует.")
    
    # Переименование директории
    new_dir_name = "renamed_directory"
    if os.path.exists(dir_name):
        os.rename(dir_name, new_dir_name)
        print(f"Директория переименована из '{dir_name}' в '{new_dir_name}'.")
    else:
        print(f"Директория '{dir_name}' не найдена для переименования.")
    
    # Вывод содержимого текущей директории
    current_dir = os.getcwd()
    print(f"\nСодержимое текущей директории ({current_dir}):")
    for item in os.listdir(current_dir):
        print("  -", item)
    
    # Удаление созданной директории (содержимое удаляется, если оно есть)
    if os.path.exists(new_dir_name):
        shutil.rmtree(new_dir_name)
        print(f"\nДиректория '{new_dir_name}' и её содержимое удалены.")
    else:
        print(f"Директория '{new_dir_name}' не найдена для удаления.")
    print()


# ===============================
# 3. Python builtin functions Demo
# ===============================

def builtin_functions_demo():
    """
    Демонстрация использования некоторых встроенных функций Python:
      - len, sum, max, min, type, list, range и т.д.
    """
    numbers = [10, 20, 30, 40, 50]
    text = "Пример строки"
    
    print("Демонстрация встроенных функций Python:")
    print("Список чисел:", numbers)
    print("Длина списка (len):", len(numbers))
    print("Сумма элементов (sum):", sum(numbers))
    print("Максимум (max):", max(numbers))
    print("Минимум (min):", min(numbers))
    print("Тип переменной 'text' (type):", type(text))
    print("Преобразование строки в список символов (list):", list(text))
    print("Диапазон чисел (range):", list(range(5)))
    print()


# ===============================
# Основной блок выполнения
# ===============================

if __name__ == "__main__":
    print("Лекция L6: Directories and Files, Python File Handling, Working with Directories, Builtin Functions\n")
    
    file_handling_demo()    # Демонстрация работы с файлами
    directories_demo()      # Демонстрация работы с директориями
    builtin_functions_demo()  # Демонстрация встроенных функций Python
