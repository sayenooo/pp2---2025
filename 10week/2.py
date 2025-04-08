import pygame
import time
import random
import sqlite3

# Инициализация Pygame
pygame.init()

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
wall_color = (213, 0, 255)
dgreen = (137, 255, 252)

# Окно
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)

# Подключение к БД
conn = sqlite3.connect("scorebook.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    score INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    score INTEGER,
    level INTEGER,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")
conn.commit()

def generate_walls(level):
    walls = []
    for _ in range(level * 5):
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

def add_user(name):
    cursor.execute("INSERT INTO users (name, score, level) VALUES (?, ?, ?)", (name, 0, 1))
    conn.commit()

def save_game_state(user_id, score, level):
    cursor.execute("INSERT INTO user_score (user_id, score, level) VALUES (?, ?, ?)", (user_id, score, level))
    conn.commit()

def pause_game(user_id, score, level):
    print("⏸ Game paused. Press P again to resume.")
    save_game_state(user_id, score, level)
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = False

def gameLoop():
    name = input("Enter your username: ").strip()
    if not name:
        print("❌ Username cannot be empty.")
        return

    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    user = cursor.fetchone()

    if user:
        print(f"👋 Welcome back, {name}! Level: {user[3]}")
        user_id = user[0]
        level = user[3]
    else:
        print(f"👤 New user created: {name}")
        add_user(name)
        cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
        user = cursor.fetchone()
        user_id = user[0]
        level = 1

    game_over = False
    game_close = False

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

    walls = generate_walls(level)

    while not game_over:
        while game_close:
            dis.fill(black)
            msg = font_style.render("Game Over! Q-Quit | C-Play Again", True, red)
            dis.blit(msg, [dis_width / 6, dis_height / 3])
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
                elif event.key == pygame.K_p:
                    pause_game(user_id, Length_of_snake - 1, level)
                elif event.key == pygame.K_s:
                    save_game_state(user_id, Length_of_snake - 1, level)
                    print("✅ Progress saved.")

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
            pygame.draw.rect(dis, wall_color, [wall[0], wall[1], snake_block, snake_block])

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

    print(f"\n🎉 Game over for {name}!")
    print(f"👉 Final score: {Length_of_snake - 1}")
    print(f"👉 Your Level: {level}")

    save_game_state(user_id, Length_of_snake - 1, level)

    print("\n📊 Last 5 games:")
    cursor.execute("""
    SELECT score, level FROM user_score
    WHERE user_id = ?
    ORDER BY ROWID DESC
    LIMIT 5
    """, (user_id,))
    for row in cursor.fetchall():
        print(f"  🐍 Score: {row[0]}, Level: {row[1]}")



    quit()

# Запуск
gameLoop()
