"""
Лекция L4: Конспект в виде Python кода
Темы:
  1. Итераторы и Генераторы
  2. Область видимости (Scope)
  3. Модули
  4. Работа с датами
  5. Модуль math
  6. Работа с JSON
"""

# ===============================
# 1. Итераторы и Генераторы
# ===============================

def iterators_demo():
    """
    Демонстрация работы итератора.
    Итератор – объект, который имеет методы __iter__() и __next__().
    """
    my_list = [1, 2, 3, 4, 5]
    it = iter(my_list)  # Получаем итератор из списка
    print("Итератор (последовательный вывод элементов списка):")
    while True:
        try:
            item = next(it)
            print(item, end=" ")
        except StopIteration:
            break
    print("\n")  # Переход на новую строку после завершения итерации

def generators_demo():
    """
    Демонстрация работы генератора.
    Генератор – это функция, использующая ключевое слово yield для возврата элементов по одному.
    """
    print("Генератор (Countdown от 5 до 1):")
    def countdown(n):
        while n > 0:
            yield n  # Возвращаем значение и приостанавливаем выполнение функции
            n -= 1
    for num in countdown(5):
        print(num, end=" ")
    print("\n")


# ===============================
# 2. Область видимости (Scope)
# ===============================

def scope_demo():
    """
    Демонстрация областей видимости переменных:
      - Локальные переменные
      - Nonlocal (переменные во внешней функции)
      - Глобальные переменные
    """
    global_var = "Глобальная переменная"

    def outer():
        outer_var = "Внешняя переменная"

        def inner():
            nonlocal outer_var  # Позволяет изменить переменную, объявленную в outer()
            inner_var = "Локальная переменная"
            outer_var = "Изменённая внешняя переменная"
            print("Внутри inner():")
            print("  inner_var =", inner_var)
            print("  outer_var =", outer_var)
            print("  global_var =", global_var)
        inner()
        print("После inner(), outer_var =", outer_var)
    
    print("Область видимости переменных:")
    outer()
    print()


# ===============================
# 3. Модули
# ===============================

def modules_demo():
    """
    Демонстрация импорта и использования стандартного модуля.
    Пример: использование модуля math для вычисления квадратного корня.
    """
    import math
    print("Модули:")
    print("  sqrt(16) =", math.sqrt(16))
    print()


# ===============================
# 4. Работа с датами
# ===============================

def dates_demo():
    """
    Работа с датами с использованием модуля datetime.
    Получение текущей даты и времени, а также вычисление даты завтрашнего дня.
    """
    from datetime import datetime, timedelta
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    print("Работа с датами:")
    print("  Текущая дата и время:", now)
    print("  Завтрашняя дата:", tomorrow)
    print()


# ===============================
# 5. Модуль math
# ===============================

def math_demo():
    """
    Демонстрация модуля math.
    Вычисление значения числа pi и синуса угла.
    """
    import math
    print("Модуль math:")
    print("  pi =", math.pi)
    print("  sin(pi/2) =", math.sin(math.pi/2))
    print()


# ===============================
# 6. Работа с JSON
# ===============================

def json_demo():
    """
    Работа с JSON:
      - Сериализация Python-объекта в JSON-строку
      - Десериализация JSON-строки обратно в Python-объект
    """
    import json
    data = {
        "name": "Алиса",
        "age": 28,
        "city": "Москва"
    }
    # Преобразование Python-объекта в форматированный JSON-строку
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    print("Работа с JSON:")
    print("  Сериализованный JSON:")
    print(json_str)
    # Обратное преобразование JSON-строки в Python-объект
    parsed_data = json.loads(json_str)
    print("  Десериализованные данные:")
    print(parsed_data)
    print()

"""
json.dumps(obj)	Преобразует Python-объект в JSON-строку
json.dump(obj, file)	Записывает JSON в файл
json.loads(json_str)	Преобразует JSON-строку в Python-объект
json.load(file)	Читает JSON из файла
uppercase reverse slash
"""



# ===============================
# Основной блок выполнения
# ===============================

if __name__ == "__main__":
    print("Лекция L4: Iterators, Generators, Scope, Modules, Dates, Math, JSON\n")
    
    iterators_demo()    # Демонстрация итераторов
    generators_demo()     # Демонстрация генераторов
    scope_demo()          # Демонстрация областей видимости
    modules_demo()        # Демонстрация работы с модулями
    dates_demo()          # Работа с датами
    math_demo()           # Работа с модулем math
    json_demo()           # Работа с JSON
