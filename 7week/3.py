# Импортируем библиотеку pygame и инициализируем её
import pygame
pygame.init()

# ---------------- ЧАСТЬ 1: НАСТРОЙКА ----------------

# Размеры окна
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 800

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

# Название окна
pygame.display.set_caption("red ball")

# Настройка таймера (для контроля FPS)
clock = pygame.time.Clock()

# Начальные координаты шара
x = 5
y = 5

# ---------------- ЧАСТЬ 2: ГЛАВНЫЙ ЦИКЛ ----------------

run = True
while run:
    # ---------------- ЧАСТЬ 3: ОТРИСОВКА ----------------

    # Заливаем фон белым цветом
    screen.fill((255, 255, 255))

    # Рисуем красный круг (шар) в текущих координатах (x, y), радиус 25
    circle = pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    # Обработка нажатий клавиш
    key = pygame.key.get_pressed()

    # Если нажата стрелка вверх и круг не выходит за верхнюю границу
    if key[pygame.K_UP] and y - 50 >= 0:
        y -= 20  # двигаем вверх

    # Если нажата стрелка вниз и круг не выходит за нижнюю границу
    if key[pygame.K_DOWN] and y + 50 <= SCREEN_HEIGTH:
        y += 20  # двигаем вниз

    # Если нажата стрелка влево и круг не выходит за левую границу
    if key[pygame.K_LEFT] and x - 50 >= 0:
        x -= 20  # двигаем влево

    # Если нажата стрелка вправо и круг не выходит за правую границу
    if key[pygame.K_RIGHT] and x + 50 <= SCREEN_WIDTH:
        x += 20  # двигаем вправо

    # Проверка на выход из игры (нажатие на крестик)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # завершить цикл

    # Устанавливаем частоту обновления экрана (60 кадров в секунду)
    clock.tick(60)

    # Обновляем экран
    pygame.display.flip()

# После выхода из цикла закрываем pygame
pygame.quit()
