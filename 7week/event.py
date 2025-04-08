# Импортируем библиотеку pygame
import pygame

# Инициализируем pygame
pygame.init()

# ---------------- НАСТРОЙКИ ОКНА ----------------

# Размер окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Создание окна с заданной шириной и высотой
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Создание объекта таймера для управления FPS
clock = pygame.time.Clock()

# ---------------- ПЕРЕМЕННЫЕ СОСТОЯНИЯ ----------------

run = True          # Основной флаг, чтобы не выходить из игры
running = False     # Флаг "бега" (если нажата клавиша вниз)
sprinting = False   # Флаг "спринта" (если нажата клавиша A)

# ---------------- ГЛАВНЫЙ ЦИКЛ ----------------

while run:
    # Заливаем экран чёрным цветом каждый кадр
    screen.fill((0, 0, 0))
    
    # Обрабатываем события (клавиши, выход и т.п.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Закрытие окна — выходим из цикла

        # Если нажата клавиша
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                running = True  # Включаем флаг "бега"
            if event.key == pygame.K_a:
                sprinting = True  # Включаем флаг "спринта"

        # Если клавиша отпущена
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                running = False  # Выключаем флаг "бега"
            if event.key == pygame.K_a:
                sprinting = False  # Выключаем флаг "спринта"

    # Если в данный момент зажата клавиша вниз
    if running:
        print("NEVER GIVE UP")  # Показываем мотивацию

    # Если в данный момент зажата клавиша A
    if sprinting:
        print("u've got this girl")  # Ещё одна мотивашка!

    # Обновляем экран
    pygame.display.flip()

    # Задержка, чтобы было 60 кадров в секунду
    clock.tick(60)

# Когда вышли из цикла, закрываем pygame
pygame.quit()
