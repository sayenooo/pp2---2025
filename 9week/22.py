import pygame  # Импорт библиотеки pygame
import random  # Импорт библиотеки random

# Инициализация pygame
pygame.init()

# Определение цветов
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
gray = (50, 50, 50)

# Размеры окна
dis_width = 800  # Ширина
dis_height = 600  # Высота

# Создание окна игры
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

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

def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

def Your_level(level):
    value = font_style.render("Your Level: " + str(level), True, white)
    dis.blit(value, [600, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    game_over = False
    game_close = False
    x1, y1 = dis_width / 2, dis_height / 2
    x1_change, y1_change = 0, 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    level = 0
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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        for wall in walls:
            if (x1, y1) == wall:
                game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        
        for wall in walls:
            pygame.draw.rect(dis, gray, [wall[0], wall[1], snake_block, snake_block])
        
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
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        new_level = (Length_of_snake - 1) // 2
        if new_level > level:
            level = new_level
            walls = generate_walls(level)
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

gameLoop()