"""
Лекция L7: Pygame

Темы:
  1. Getting Started: Инициализация и создание окна
  2. Working with Images: Загрузка и отображение изображений
  3. Music and Sound Effects: Воспроизведение фоновой музыки и звуковых эффектов
  4. Geometric Drawing: Рисование геометрических фигур
  5. Timer: Использование таймера для периодических событий

Примечание: Для полного функционирования замените пути к файлам изображений и звуков на существующие файлы.
"""

import pygame
import sys

def main():
    # 1. Getting Started: Инициализация Pygame и создание окна
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Лекция L7: Pygame")

    # 2. Working with Images: Загрузка изображения
    # Замените "example_image.png" на путь к вашему изображению.
    try:
        image = pygame.image.load("example_image.png").convert_alpha()
    except Exception as e:
        print("Изображение не найдено. Будет использована заглушка. Ошибка:", e)
        image = None

    # 3. Music and Sound Effects
    # Попытка загрузить фоновую музыку
    try:
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.play(-1)  # -1 для бесконечного повторения
    except Exception as e:
        print("Фоновая музыка не найдена. Ошибка:", e)
    
    # Попытка загрузить звуковой эффект
    try:
        sound_effect = pygame.mixer.Sound("effect.wav")
    except Exception as e:
        print("Звуковой эффект не найден. Ошибка:", e)
        sound_effect = None

    # 5. Timer: Настройка таймера, который будет генерировать событие каждые 2000 мс (2 секунды)
    TIMER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER_EVENT, 2000)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Таймер генерирует событие, при получении которого можно выполнить действие
            elif event.type == TIMER_EVENT:
                print("Таймер сработал!")
                # Воспроизведение звукового эффекта при срабатывании таймера
                if sound_effect:
                    sound_effect.play()

        # 4. Geometric Drawing: Рисование фигур
        # Заливка фона темно-серым цветом
        screen.fill((30, 30, 30))
        
        # Отображение изображения (если загружено) или заглушки в виде красного прямоугольника
        if image:
            screen.blit(image, (50, 50))
        else:
            pygame.draw.rect(screen, (255, 0, 0), (50, 50, 200, 150))
        
        # Рисование круга (зеленый)
        pygame.draw.circle(screen, (0, 255, 0), (400, 300), 50)
        
        # Рисование линии (синяя диагональная линия)
        pygame.draw.line(screen, (0, 0, 255), (0, 0), (screen_width, screen_height), 5)
        
        # Рисование эллипса (желтый)
        pygame.draw.ellipse(screen, (255, 255, 0), (300, 400, 200, 100))
        
        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)  # Ограничение до 60 кадров в секунду

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
