import os
path = input()

if not os.path.exists(path):
    print("Ошибка: указанный путь не существует.")
elif not os.path.isfile(path):
    print("Ошибка: это не файл, а директория.")
elif not os.access(path, os.W_OK):
    print("Ошибка: нет прав на удаление файла.")
else:
    os.remove(path)
    print(f"Файл '{path}' успешно удален.")