import pygame  # Библиотека для создания игр
import time    # Для работы со временем
import random  # Для генерации случайных чисел

# Инициализация всех модулей pygame
pygame.init()

# Определение цветов в формате RGB
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
color = (213, 0, 255)     # Цвет стен
dgreen = (137, 255, 252)  # Цвет дополнительной еды

# Размеры игрового окна
dis_width = 800
dis_height = 600

# Создание окна с заданными размерами
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')  # Название окна

# Установка частоты обновления экрана
clock = pygame.time.Clock()

# Настройки змейки
snake_block = 10      # Размер одного блока змейки
snake_speed = 15      # Скорость змейки (больше = быстрее)

# Настройка шрифта для текста на экране
font_style = pygame.font.SysFont("bahnschrift", 25)

# Функция для генерации стен в зависимости от уровня
def generate_walls(level):
    walls = []
    for _ in range(level * 5):  # Чем выше уровень — тем больше стен
        wall_x = round(random.randrange(snake_block, dis_width - snake_block) / 10.0) * 10.0
        wall_y = round(random.randrange(snake_block, dis_height - snake_block) / 10.0) * 10.0
        walls.append((wall_x, wall_y))
    return walls

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

# Главная игровая функция
def gameLoop():
    game_over = False
    game_close = False

    # Начальная позиция змейки (центр экрана)
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Смещение по координатам (движение)
    x1_change = 0
    y1_change = 0

    # Список, содержащий координаты тела змейки
    snake_List = []
    Length_of_snake = 1

    # Генерация координат еды
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Дополнительная еда, которая появляется через время
    foodxx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foodyy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    food_time = pygame.time.get_ticks()  # Засекаем время появления

    # Уровень игры
    level = 1
    walls = generate_walls(level)  # Генерация стен

    while not game_over:

        while game_close:
            # Экран "Game Over"
            dis.fill(black)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            dis.blit(message, [dis_width / 6, dis_height / 3])
            Your_score(Length_of_snake - 1)
            Your_level(level)
            pygame.display.update()

            # Обработка ввода после проигрыша
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Выйти
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Играть снова
                        gameLoop()

        # Обработка событий (движение и выход)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
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

        # Проверка на выход за границы или столкновение со стеной
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0 or (x1, y1) in walls:
            game_close = True

        # Обновление позиции змейки
        x1 += x1_change
        y1 += y1_change

        # Очистка экрана
        dis.fill(black)

        # Основная еда
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Если прошло 5 секунд — появится дополнительная еда
        if pygame.time.get_ticks() - food_time > 5000:
            food_time = pygame.time.get_ticks()
            foodxx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foodyy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        pygame.draw.rect(dis, dgreen, [foodxx, foodyy, snake_block, snake_block])

        # Обновление позиции головы змейки
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        # Удаление хвоста, если змейка не растет
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение с собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Отрисовка змейки, счета, уровня, стен
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        Your_level(level)

        # Рисуем стены
        for wall in walls:
            pygame.draw.rect(dis, color, [wall[0], wall[1], snake_block, snake_block])

        pygame.display.update()  # Обновление экрана

        # Если съел обычную еду
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Если съел дополнительную еду
        if x1 == foodxx and y1 == foodyy:
            foodxx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foodyy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 3

        # Повышение уровня за каждые 5 очков
        if Length_of_snake // 5 > level:
            level += 1
            walls = generate_walls(level)

        clock.tick(snake_speed)  # Ограничение FPS

    # Завершение игры
    pygame.quit()
    quit()

# Запуск игры
gameLoop()
