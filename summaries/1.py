"""
Лекция L1: Python Fundamentals

Темы:
  - Python Intro
  - Python User Input
  - Python Get Started
  - Python Syntax
  - Python Comments
  - Python Variables
  - Python Data Types
  - Python Numbers
  - Python Casting
  - Python Strings
  - Python String Formatting
  - Python Booleans
  - Python Operators
  - Python If...Else
  - Git (основы работы с Git)
"""

# -------------------------------
# Python Intro и Get Started
# -------------------------------

def intro_demo():
    """
    Демонстрация базового вывода в Python.
    Обычно первая программа: "Hello, World!"
    """
    print("Hello, World! Добро пожаловать в Python!")


def get_started_demo():
    """
    Демонстрация базового старта: вывод простого сообщения.
    """
    print("Запуск программы: Python Get Started")


# -------------------------------
# Python User Input
# -------------------------------

def user_input_demo():
    """
    Демонстрация получения ввода от пользователя.
    Обратите внимание: эта функция требует ввода с клавиатуры.
    """
    name = input("Введите ваше имя: ")
    print(f"Привет, {name}!")


# -------------------------------
# Python Syntax и Comments
# -------------------------------

def syntax_and_comments_demo():
    """
    Демонстрация синтаксиса Python и комментариев.
    
    Примеры:
      - Отступы обязательны.
      - Комментарии начинаются с символа #.
      - Многострочные комментарии (докстринги) используются для документации.
    """
    # Это однострочный комментарий
    """
    Это многострочный комментарий,
    который также может служить документацией
    для функции или модуля.
    """
    print("Синтаксис Python: отступы, двоеточия и комментарии.")


# -------------------------------
# Python Variables и Data Types
# -------------------------------

def variables_and_data_types_demo():
    """
    Демонстрация переменных и основных типов данных в Python.
    """
    # Переменные
    number = 42              # целое число (int)
    pi = 3.14159             # число с плавающей точкой (float)
    message = "Python"       # строка (str)
    is_active = True         # булево значение (bool)
    
    # Списки, кортежи, словари и множества
    fruits = ["яблоко", "банан", "вишня"]  # список (list)
    dimensions = (1920, 1080)               # кортеж (tuple)
    person = {"имя": "Алиса", "возраст": 28} # словарь (dict)
    unique_numbers = {1, 2, 3, 3, 2, 1}      # множество (set)
    
    print("Переменные и типы данных:")
    print("number =", number, "тип:", type(number))
    print("pi =", pi, "тип:", type(pi))
    print("message =", message, "тип:", type(message))
    print("is_active =", is_active, "тип:", type(is_active))
    print("fruits =", fruits, "тип:", type(fruits))
    print("dimensions =", dimensions, "тип:", type(dimensions))
    print("person =", person, "тип:", type(person))
    print("unique_numbers =", unique_numbers, "тип:", type(unique_numbers))


# -------------------------------
# Python Numbers и Casting
# -------------------------------

def numbers_and_casting_demo():
    """
    Демонстрация арифметических операций и преобразования типов.
    """
    a = 7
    b = 3
    print("Арифметические операции:")
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)
    print("a // b =", a // b)  # целочисленное деление
    print("a ** b =", a ** b)  # возведение в степень
    print("a % b =", a % b)    # остаток от деления

    # Преобразование типов (casting)
    num_str = "123"
    num_int = int(num_str)
    num_float = float(num_str)
    print("\nПреобразование типов:")
    print("Строка:", num_str, "-> целое число:", num_int, "-> число с плавающей точкой:", num_float)
    
    # Преобразование числа в строку
    num = 456
    num_str2 = str(num)
    print("Число:", num, "-> строка:", num_str2)


# -------------------------------
# Python Strings и String Formatting
# -------------------------------

def strings_and_formatting_demo():
    """
    Демонстрация работы со строками и их форматирования.
    """
    # Объявление строк
    single_quote = 'Строка в одинарных кавычках'
    double_quote = "Строка в двойных кавычках"
    multi_line = """Это
многострочная
строка"""
    
    print("Работа со строками:")
    print(single_quote)
    print(double_quote)
    print(multi_line)
    
    # Форматирование строк
    name = "Алиса"
    age = 30
    # Использование f-строк (f-strings)
    formatted1 = f"Привет, меня зовут {name}, и мне {age} лет."
    # Использование метода format()
    formatted2 = "Привет, меня зовут {}, и мне {} лет.".format(name, age)
    # Использование оператора %
    formatted3 = "Привет, меня зовут %s, и мне %d лет." % (name, age)
    
    print("\nФорматирование строк:")
    print(formatted1)
    print(formatted2)
    print(formatted3)


# -------------------------------
# Python Booleans и Operators
# -------------------------------

def booleans_and_operators_demo():
    """
    Демонстрация булевых значений и операторов.
    """
    # Булевы значения
    flag = True
    not_flag = False
    print("Булевы значения:")
    print("flag =", flag, ", not flag =", not flag)
    
    # Операторы сравнения
    x = 10
    y = 20
    print("\nОператоры сравнения:")
    print("x == y:", x == y)
    print("x != y:", x != y)
    print("x < y:", x < y)
    print("x > y:", x > y)
    
    # Логические операторы
    print("\nЛогические операторы:")
    print("True and False =", True and False)
    print("True or False =", True or False)
    print("not True =", not True)
    
    # Арифметические операторы уже продемонстрированы в функции numbers_and_casting_demo()


# -------------------------------
# Python If...Else
# -------------------------------

def if_else_demo():
    """
    Демонстрация условных операторов if, elif и else.
    """
    number = 15
    print("\nУсловные операторы:")
    if number > 10:
        print("Число больше 10")
    elif number == 10:
        print("Число равно 10")
    else:
        print("Число меньше 10")


# -------------------------------
# Git (основы работы с Git)
# -------------------------------

def git_demo():
    """
    Основные команды Git (описаны в комментариях, не выполняются как Python код):
    
    1. git init          - инициализация нового репозитория
    2. git add .         - добавление изменений в индекс
    3. git commit -m "сообщение" - создание коммита с сообщением
    4. git status        - проверка состояния репозитория
    5. git log           - просмотр истории коммитов
    6. git push          - отправка изменений в удаленный репозиторий
    7. git pull          - получение изменений из удаленного репозитория
    """
    print("\nGit demo: Основные команды Git описаны в комментариях.")


# -------------------------------
# Основной блок выполнения
# -------------------------------

if __name__ == "__main__":
    print("Лекция L1: Python Fundamentals\n")
    
    # Python Intro и Get Started
    intro_demo()
    get_started_demo()
    
    # Python Syntax и Comments
    syntax_and_comments_demo()
    
    # Python Variables и Data Types
    variables_and_data_types_demo()
    
    # Python Numbers и Casting
    numbers_and_casting_demo()
    
    # Python Strings и String Formatting
    strings_and_formatting_demo()
    
    # Python Booleans и Operators
    booleans_and_operators_demo()
    
    # Python If...Else
    if_else_demo()
    
    # Python User Input (раскомментируйте, чтобы протестировать)
    # user_input_demo()
    
    # Git (основы)
    git_demo()
