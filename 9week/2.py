import pygame  # Импорт библиотеки pygame
import time  # Импорт библиотеки time
import random  # Импорт библиотеки random

# Инициализация pygame
pygame.init()

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
color = (213, 0, 255)
dgreen = (137,255,252)

# Размеры окна
dis_width = 800  # Ширина
dis_height = 600  # Высота

# Создание окна игры
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')  # Заголовок окна

# Создание часов для управления скоростью змейки
clock = pygame.time.Clock()

# Настройки змейки
snake_block = 10  # Размер одного сегмента змейки
snake_speed = 15  # Начальная скорость змейки

# Шрифт для отображения текста
font_style = pygame.font.SysFont("bahnschrift", 25)

def generate_walls(level):
    walls = []
    for _ in range(level * 5):  # Количество стен зависит от уровня
        wall_x = round(random.randrange(snake_block, dis_width - snake_block) / 10.0) * 10.0
        wall_y = round(random.randrange(snake_block, dis_height - snake_block) / 10.0) * 10.0
        walls.append((wall_x, wall_y))
    return walls

# Функция для отображения счета игрока
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Функция для отображения уровня
def Your_level(level):
    value = font_style.render("Your Level: " + str(level), True, white)
    dis.blit(value, [600, 0])

# Функция для отрисовки змейки
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    game_over = False  # Переменная завершения игры
    game_close = False  # Переменная проигрыша

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    foodxx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foodyy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    food_time = pygame.time.get_ticks()
    
    level = 1
    walls = generate_walls(level)

    while not game_over:

        while game_close:
            dis.fill(black)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, red)
            dis.blit(message, [dis_width / 6, dis_height / 3])
            Your_score(Length_of_snake - 1)
            Your_level(level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0 or (x1, y1) in walls:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        if pygame.time.get_ticks() - food_time > 5000:
            food_time = pygame.time.get_ticks()
            foodxx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foodyy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        pygame.draw.rect(dis, dgreen, [foodxx, foodyy, snake_block, snake_block])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        Your_level(level)

        for wall in walls:
            pygame.draw.rect(dis, color, [wall[0], wall[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        if x1 == foodxx and y1 == foodyy:
            foodxx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foodyy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 3

        if Length_of_snake // 5 > level:
            level += 1
            walls = generate_walls(level)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
