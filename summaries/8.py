"""
Лекция L8: Pygame

Темы:
  1. Fonts and Text: Рендеринг текста с использованием pygame.font
  2. More on Input: Расширенная обработка ввода (клавиатура, мышь)
  3. Centralized Scene Logic: Централизованная логика сцен для управления игровым процессом
  4. Game Creation: Создание базовой структуры игры с использованием сцен
"""

import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Лекция L8: Pygame - Fonts, Input, Scenes, Game Creation")

# -----------------------------
# Fonts and Text
# -----------------------------
# Инициализация шрифта
FONT_SIZE = 36
font = pygame.font.SysFont("Arial", FONT_SIZE)

def render_text(text, color=(255, 255, 255)):
    """Функция для рендеринга текста с заданным цветом."""
    return font.render(text, True, color)

# -----------------------------
# Centralized Scene Logic
# -----------------------------
class Scene:
    """Базовый класс для всех сцен игры."""
    def handle_events(self, events):
        """Обработка входных событий."""
        pass

    def update(self):
        """Обновление логики сцены."""
        pass

    def render(self, screen):
        """Отрисовка сцены."""
        pass

class MainMenu(Scene):
    """Сцена главного меню."""
    def __init__(self):
        self.title_text = render_text("Главное меню", (0, 255, 0))
        self.instruction_text = render_text("Нажмите Enter для старта", (255, 255, 255))
    
    def handle_events(self, events):
        """Обработка ввода в главном меню."""
        for event in events:
            if event.type == pygame.KEYDOWN:
                # More on Input: Обработка клавиатуры
                if event.key == pygame.K_RETURN:
                    return "start_game"  # Переход к игровой сцене
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        return None

    def update(self):
        """Обновление логики главного меню (при необходимости)."""
        pass

    def render(self, screen):
        """Отрисовка главного меню."""
        screen.fill((0, 0, 0))
        title_rect = self.title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        instruction_rect = self.instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
        screen.blit(self.title_text, title_rect)
        screen.blit(self.instruction_text, instruction_rect)

class GameScene(Scene):
    """Сцена самой игры."""
    def __init__(self):
        self.info_text = render_text("Игра запущена! Нажмите ESC для выхода", (255, 255, 0))
    
    def handle_events(self, events):
        """Обработка ввода во время игры."""
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "exit_to_menu"
        return None

    def update(self):
        """Обновление игровой логики (например, перемещение объектов)."""
        pass

    def render(self, screen):
        """Отрисовка игровой сцены."""
        screen.fill((50, 50, 100))
        info_rect = self.info_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(self.info_text, info_rect)

class SceneManager:
    """Класс для централизованного управления сценами."""
    def __init__(self):
        self.scenes = {
            "menu": MainMenu(),
            "game": GameScene()
        }
        self.current_scene = "menu"
    
    def handle_events(self, events):
        action = self.scenes[self.current_scene].handle_events(events)
        if action == "start_game":
            self.current_scene = "game"
        elif action == "exit_to_menu":
            self.current_scene = "menu"
    
    def update(self):
        self.scenes[self.current_scene].update()
    
    def render(self, screen):
        self.scenes[self.current_scene].render(screen)

# -----------------------------
# Game Creation: Основной цикл игры
# -----------------------------
def main():
    clock = pygame.time.Clock()
    scene_manager = SceneManager()
    
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        scene_manager.handle_events(events)
        scene_manager.update()
        scene_manager.render(screen)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
