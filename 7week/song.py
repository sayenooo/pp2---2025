import pygame
pygame.init()

# ===== 1 ЧАСТЬ: НАСТРОЙКА ОКНА =====

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800  # Исправлена опечатка

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working with rectangles")

# ===== ЗАГРУЗКА И ВОСПРОИЗВЕДЕНИЕ ЗВУКА =====

# Загружаем звук
sound = pygame.mixer.Sound('sound.wav')  # создаем объект звука
sound.play(-1)  # -1 означает бесконечное повторение

# Загружаем второй звук (но не проигрываем пока)
sound1 = pygame.mixer.Sound('sound1.wav')

# ===== 2 ЧАСТЬ: ОСНОВНОЙ ЦИКЛ =====

run = True
while run:
    # ===== 3 ЧАСТЬ: ОТРИСОВКА И СОБЫТИЯ =====
    screen.fill((0, 0, 0))  # Заливаем экран черным

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()  # Обновляем экран

pygame.quit()
