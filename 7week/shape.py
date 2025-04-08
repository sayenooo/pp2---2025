# Импортируем модуль pygame
import pygame

# Инициализируем все модули pygame
pygame.init()

# Задаем размеры окна
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 800  # <-- Тут опечатка: должно быть HEIGHT, но пока оставим как есть

# Создаем окно и задаем его размеры
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Working with shapes")  # Название окна

# Создаем объект часов для управления FPS
clock = pygame.time.Clock()

# Переменная для главного цикла
run = True

# Переменная, которая будет изменяться при зажатой мыши
x = 0

# Главный цикл игры
while run:
    # Заливаем фон белым цветом
    screen.fill((255, 255, 255))
    
    # Если левая кнопка мыши нажата, увеличиваем x
    if pygame.mouse.get_pressed()[0]:
        x += 0.001
    else:
        x -= 0.001

    # Прямоугольник с цветом, толщиной и закруглением правого нижнего угла
    pygame.draw.rect(screen, (43, 64, 123), (200, 180, 100, 100), width=5, border_bottom_right_radius=50)

    # Круг с обводкой
    pygame.draw.circle(screen, (0, 43, 234), (100, 100), 25, 3)

    # Полукруг — для него используются флаги (не во всех версиях Pygame работает)
    # draw_top_right и draw_bottom_left поддерживаются только в новых версиях pygame
    pygame.draw.circle(screen, (43, 54, 34), (300, 300), 50, draw_top_right=True, draw_bottom_left=True)

    # Эллипс
    pygame.draw.ellipse(screen, (43, 243, 234), (120, 120, 23, 56))

    # Дуга: от 0 до x радиан
    pygame.draw.arc(screen, (245, 200, 0), (350, 350, 100, 100), 0, x, width=5)

    # Линия от точки (300, 300) до (x, 46)
    pygame.draw.line(screen, (43, 54, 78), (300, 300), (x, 46))

    # Многоугольник с заданными вершинами
    pygame.draw.polygon(screen, (243, 228, 210), ((213, 654), (95, 52), (324, 21), (423, 65)))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Завершаем цикл, если нажата кнопка "Закрыть"

    # Устанавливаем FPS — ОЧЕНЬ большое значение, лучше заменить на разумное, например, 60
    clock.tick(60)

    # Обновляем экран
    pygame.display.flip()

# Завершаем работу pygame
pygame.quit()
