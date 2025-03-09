import pygame
import datetime

pygame.init()

# Экран
SCREEN_WIDTH = 836
SCREEN_HEIGHT = 836
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mickey's Clock")

# Загрузка изображений
background = pygame.image.load("7week/mickey.jpeg").convert_alpha()
minute_hand = pygame.image.load("7week/m.jpeg").convert_alpha()
second_hand = pygame.image.load("7week/s.jpeg").convert_alpha()

clock = pygame.time.Clock()
center1 = (SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2)
center2 = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
# Центр экрана (основа стрелок)

def rotate_hand(image, angle, pivot):
    """ Поворачивает стрелку вокруг заданного pivot (основания) """
    rotated_image = pygame.transform.rotate(image, -angle)  # Pygame поворачивает против часовой стрелки, поэтому берём '-angle'
    new_rect = rotated_image.get_rect(center=pivot)  # Новый прямоугольник после поворота
    return rotated_image, new_rect.topleft  # Возвращаем изображение и новую позицию

# Основной цикл
run = True
while run:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # Получаем текущее время
    now = datetime.datetime.now()
    minute_angle = now.minute * 6  # 360° / 60 мин = 6° за 1 мин
    second_angle = now.second * 6  # 360° / 60 сек = 6° за 1 сек

    # Вращаем стрелки
    rotated_minute, min_pos = rotate_hand(minute_hand, minute_angle, center1)
    rotated_second, sec_pos = rotate_hand(second_hand, second_angle, center2)

    # Отображаем стрелки
    screen.blit(rotated_minute, min_pos)
    screen.blit(rotated_second, sec_pos)

    # Проверяем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
