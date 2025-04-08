# Импортируем библиотеки: pygame для графики и звука, datetime для времени
import pygame
import datetime

# Инициализация всех необходимых модулей
pygame.init()
pygame.mixer.init()  # для воспроизведения музыки

# ---------------- НАСТРОЙКА ОКНА ----------------
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # создаём окно
pygame.display.set_caption("My favourite songs")  # заголовок окна

# ---------------- ЗАГРУЗКА ДАННЫХ ----------------

# Список любимых песен (названия файлов mp3)
mine = ["music.mp3", "music1.mp3", "music2.mp3"]
x = 0  # индекс текущей песни

# Загружаем изображения
image = pygame.image.load("1.jpeg").convert_alpha()     # фоновое изображение
image1 = pygame.image.load("disk.png").convert_alpha()  # изображение диска

# Центры вращения двух дисков
center1 = (125 // 2, 120 // 2)
center2 = (220 // 2, 120 // 2)

# ---------------- ФУНКЦИИ ----------------

# Функция для воспроизведения песни с индексом x
def play(x):
    pygame.mixer.music.load(mine[x])     # загружаем песню
    pygame.mixer.music.play(-1)          # бесконечно проигрываем

# Остановить музыку
def stop():
    pygame.mixer.music.stop()

# Предыдущая песня
def previous():
    global x
    if x > 0:
        x -= 1
    else:
        x = len(mine) - 1  # если в начале списка — переходим к последней
    pygame.mixer.music.load(mine[x])
    play(x)

# ---------------- ГЛАВНЫЙ ЦИКЛ ----------------
run = True
while run:
    # Заливаем экран белым цветом
    screen.fill((255, 255, 255))

    # Рисуем фон (например, картинку человека, слушающего музыку)
    screen.blit(image, (80, 100))

    # Получаем текущее время (для вращения дисков по секундам)
    time = datetime.datetime.now()
    angle = time.second * 6  # каждая секунда — 6 градусов

    # Поворачиваем изображение диска
    img = pygame.transform.rotate(image1, angle)

    # Вычисляем положение повернутого изображения (чтобы оставалось по центру)
    img1 = img.get_rect(center=center1)
    img2 = img.get_rect(center=center2)

    # Отображаем два крутящихся диска
    screen.blit(img, (125, 140))  # левый диск
    screen.blit(img, (220, 140))  # правый диск

    # Проверка, нажаты ли клавиши
    key = pygame.key.get_pressed()

    if key[pygame.K_a]:
        play(x)          # A — воспроизвести музыку
    if key[pygame.K_d]:
        stop()           # D — остановить музыку
    if key[pygame.K_w]:
        previous()       # W — предыдущая песня

    # Обработка событий (например, закрытие окна)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Обновляем экран
    pygame.display.flip()

# Выход из pygame
pygame.quit()
