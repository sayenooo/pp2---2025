"""
Лекция L9: Pygame – Snake и Paint

Этот конспект в виде Python кода демонстрирует два простых приложения на Pygame:
  1. Snake – классическая змейка с управлением стрелками.
  2. Paint – простое приложение для рисования мышью.

Нажмите:
  - "1" для запуска игры Snake.
  - "2" для запуска приложения Paint.
  - "ESC" для выхода в меню или завершения программы.
"""

import pygame
import sys
import random

# Инициализация Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Лекция L9: Pygame – Snake & Paint")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

# ===============================
# Snake Game
# ===============================
def snake_game():
    """Простая реализация игры "Snake"."""
    # Размеры клетки и начальные настройки
    cell_size = 20
    snake_pos = [(100, 100), (80, 100), (60, 100)]
    direction = "RIGHT"
    change_to = direction

    # Функция генерации еды в случайной позиции
    def get_food_pos():
        x = random.randrange(0, SCREEN_WIDTH, cell_size)
        y = random.randrange(0, SCREEN_HEIGHT, cell_size)
        return (x, y)
    
    food_pos = get_food_pos()
    score = 0

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Обработка нажатия клавиш для изменения направления
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"
                elif event.key == pygame.K_ESCAPE:
                    game_over = True  # Выход в меню
        
        direction = change_to
        head_x, head_y = snake_pos[0]
        # Обновление позиции головы змейки в зависимости от направления
        if direction == "UP":
            head_y -= cell_size
        elif direction == "DOWN":
            head_y += cell_size
        elif direction == "LEFT":
            head_x -= cell_size
        elif direction == "RIGHT":
            head_x += cell_size
        new_head = (head_x, head_y)

        # Проверка столкновения со стеной или самим собой
        if (head_x < 0 or head_x >= SCREEN_WIDTH or
            head_y < 0 or head_y >= SCREEN_HEIGHT or
            new_head in snake_pos):
            game_over = True
            continue

        # Добавление новой головы
        snake_pos.insert(0, new_head)
        # Если змейка съела еду, увеличиваем счет и генерируем новую еду
        if new_head == food_pos:
            score += 1
            food_pos = get_food_pos()
        else:
            snake_pos.pop()  # Удаление хвоста, если еда не съедена

        # Рисование игрового поля
        screen.fill((0, 0, 0))
        # Рисуем еду
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))
        # Рисуем змейку
        for pos in snake_pos:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], cell_size, cell_size))
        # Рисуем счет
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(10)  # Управление скоростью змейки

    # Вывод сообщения "Game Over" и ожидание нажатия клавиши
    game_over_text = font.render("Game Over! Нажмите ESC для меню", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
                                 SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False

# ===============================
# Paint App
# ===============================
def paint_app():
    """Простое приложение для рисования (Paint)."""
    drawing = False
    last_pos = None
    color = (0, 0, 0)  # черный цвет для рисования
    screen.fill((255, 255, 255))  # белый фон

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Выход в меню
                # Можно добавить смену цвета по клавишам, если нужно
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                last_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif event.type == pygame.MOUSEMOTION:
                if drawing and last_pos is not None:
                    current_pos = event.pos
                    # Рисуем линию между последней и текущей позицией
                    pygame.draw.line(screen, color, last_pos, current_pos, 5)
                    last_pos = current_pos
        
        pygame.display.flip()
        clock.tick(120)

# ===============================
# Main Menu
# ===============================
def main_menu():
    """Главное меню для выбора между Snake и Paint."""
    while True:
        screen.fill((50, 50, 50))
        title_text = font.render("Лекция L9: Pygame – Snake & Paint", True, (255, 255, 0))
        option1_text = font.render("Нажмите 1 для Snake", True, (255, 255, 255))
        option2_text = font.render("Нажмите 2 для Paint", True, (255, 255, 255))
        exit_text = font.render("Нажмите ESC для выхода", True, (255, 255, 255))
        
        # Отображаем текст меню
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
        screen.blit(option1_text, (SCREEN_WIDTH // 2 - option1_text.get_width() // 2, 180))
        screen.blit(option2_text, (SCREEN_WIDTH // 2 - option2_text.get_width() // 2, 230))
        screen.blit(exit_text, (SCREEN_WIDTH // 2 - exit_text.get_width() // 2, 280))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    snake_game()
                elif event.key == pygame.K_2:
                    paint_app()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        clock.tick(60)

# ===============================
# Основной блок выполнения
# ===============================
if __name__ == "__main__":
    main_menu()
