# Импортируем необходимые библиотеки
import pygame
import time
import random

# Инициализируем pygame
pygame.init()

# Цвета (RGB)
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размеры экрана
dis_width = 800
dis_height = 600

# Создание окна
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')  # Заголовок окна

# Таймер для управления скоростью
clock = pygame.time.Clock()

# Настройки змейки
snake_block = 10           # Размер одного блока змейки
snake_speed = 15           # Начальная скорость

# Шрифт для текста
font_style = pygame.font.SysFont("bahnschrift", 25)

# Функция отображения счета
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Функция отображения уровня
def Your_level(level):
    value = font_style.render("Your Level: " + str(level), True, white)
    dis.blit(value, [600, 0])

# Функция отрисовки змейки
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

# Основной игровой цикл
def gameLoop():
    game_over = False   # Конец игры
    game_close = False  # Пауза (когда проиграл)

    # Начальные координаты змейки
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Смещения
    x1_change = 0
    y1_change = 0

    snake_List = []          # Список сегментов змейки
    Length_of_snake = 1      # Начальная длина

    # Генерация первого "яблока" (еды)
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        # Если игрок проиграл
        while game_close:
            dis.fill(black)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            dis.blit(message, [dis_width / 6, dis_height / 3])
            Your_score(Length_of_snake - 1)
            Your_level(Length_of_snake // 2)
            pygame.display.update()

            # Обработка клавиш на экране "Game Over"
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()  # Перезапуск игры

        # Обработка событий клавиатуры и выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # Управление движением змейки
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Проверка на выход за границы
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Обновление координат головы
        x1 += x1_change
        y1 += y1_change

        # Очистка экрана
        dis.fill(black)

        # Отрисовка еды
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])

        # Обновление позиции змейки
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        # Удаление последнего элемента, если длина превышена
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на самоуничтожение (столкновение с телом)
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Отрисовка змейки, счёта и уровня
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        Your_level((Length_of_snake - 1) // 2)

        # Обновление экрана
        pygame.display.update()

        # Если змейка съела еду
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Увеличиваем скорость с ростом уровня
        if (Length_of_snake - 1) // 2:
            global snake_speed
            snake_speed += 0.01

        # Задержка по FPS
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Запуск игры
gameLoop()
