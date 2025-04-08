# Импортируем необходимые модули
import pygame         # для графики и отображения
import datetime       # для получения текущего времени

# Инициализируем pygame
pygame.init()

# Создаём окно размером 920 на 700 пикселей
screen = pygame.display.set_mode((920, 700))

# Создаём объект clock для управления FPS
clock = pygame.time.Clock()

# Загружаем картинку с Микки Маусом (фоновые часы)
image = pygame.image.load('mickey.png')

# Масштабируем её до размера 600x600 пикселей
image = pygame.transform.scale(image, (600, 600))

# Загружаем картинку стрелки (одну и ту же для минут и секунд)
minute_img = pygame.image.load('hand.png')
minute_img = pygame.transform.scale(minute_img, (600, 400))  # минутная стрелка

second_img = pygame.image.load('hand.png')
second_img = pygame.transform.scale(second_img, (600, 400))  # секундная стрелка

# Флаг завершения главного цикла
done = False

# Главный цикл программы
while not done:
    # Обработка событий (например, выход из игры)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  

    # Получаем текущее время
    current_time = datetime.datetime.now()

    # Извлекаем часы, минуты и секунды как целые числа
    hour = int(current_time.strftime("%I"))     # 12-часовой формат
    minute = int(current_time.strftime("%M"))
    second = int(current_time.strftime("%S"))

    # -------------------- Расчёт углов --------------------
    # Каждый час — 30 градусов (360 / 12), + учёт минут
    # Знак минус — для вращения по часовой стрелке
    hour_angle = (hour % 12 + minute / 60) * 30 * -1

    # Минутная стрелка: 360 градусов / 60 минут = 6 градусов за минуту
    # Минус 30 — поправка на смещение стрелки (визуальная настройка)
    minute_angle = minute * 6 * -1 - 30

    # Секундная стрелка: 6 градусов за секунду
    # Минус 50 — ещё одна визуальная настройка (центрирование стрелки)
    second_angle = second * 6 * -1 - 50

    # -------------------- Вращение стрелок --------------------

    # Поворачиваем изображения стрелок на рассчитанные углы
    rotated_minute = pygame.transform.rotate(minute_img, minute_angle)
    rotated_second = pygame.transform.rotate(second_img, second_angle)

    # -------------------- Отрисовка --------------------

    # Закрашиваем экран белым цветом
    screen.fill((255, 255, 255))

    # Рисуем циферблат (Микки) в центре экрана (примерно)
    screen.blit(image, (100, 100))  # позиция подбиралась вручную

    # Рисуем секундную стрелку, центрируя её относительно 400x400
    screen.blit(rotated_second, (
        400 - int(rotated_second.get_width() / 2),
        400 - int(rotated_second.get_height() / 2)
    ))

    # Рисуем минутную стрелку аналогично
    screen.blit(rotated_minute, (
        400 - int(rotated_minute.get_width() / 2),
        400 - int(rotated_minute.get_height() / 2)
    ))

    # Обновляем экран (всё, что отрисовали, становится видимым)
    pygame.display.flip()

    # Устанавливаем частоту обновления — 60 кадров в секунду
    clock.tick(60)

# Когда цикл завершён (выход из программы) — корректно закрываем pygame
pygame.quit()
