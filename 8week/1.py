# Импорт необходимых библиотек
import pygame, sys
from pygame.locals import *
import random, time

# Инициализация всех модулей pygame
pygame.init()

# Настройка FPS (кадров в секунду)
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов в формате RGB
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Глобальные переменные
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5             # Начальная скорость врагов
SCORE1 = 0            # Счёт за избегание врагов
SCORE2 = 0            # Счёт за собранные монетки
COIN_SPEED = 3        # Скорость падения монет

# Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Загрузка фонового изображения
background = pygame.image.load("AnimatedStreet.png")

# Создание окна
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE1
        self.rect.move_ip(0, SPEED)  # Двигаем врага вниз
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE1 += 1  # Увеличиваем счёт, если враг проскочил игрока
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс монет
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global COIN_SPEED
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)  # Стартовая позиция игрока

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Создание экземпляров классов
P1 = Player()
E1 = Enemy()
C1 = Coins()

# Создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Создание пользовательского события для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  # Каждую секунду

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5      # Увеличиваем скорость врагов
            COIN_SPEED += 0.3 # И монет
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Отрисовка фона
    DISPLAYSURF.blit(background, (0, 0))

    # Отображение счёта
    scores1 = font_small.render(str(SCORE1), True, BLACK)
    scores2 = font_small.render(str(SCORE2), True, BLACK)
    DISPLAYSURF.blit(scores1, (10, 10))      # Счёт за врагов (слева)
    DISPLAYSURF.blit(scores2, (350, 10))     # Счёт за монеты (справа)

    # Движение и отрисовка всех спрайтов
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Обработка сбора монет
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        SCORE2 += 5  # +5 очков за монетку
        new_coin = Coins()  # Создаём новую монету
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Обработка столкновения с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()  # Проигрываем звук
        time.sleep(1)  # Ждём немного

        # Экран "Game Over"
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        # Удаление всех спрайтов и выход
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Обновление экрана и установка FPS
    pygame.display.update()
    FramePerSec.tick(FPS)
