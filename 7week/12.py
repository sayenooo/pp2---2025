import pygame
import datetime

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Favourite Songs")

mine = ["music.mp3", "music1.mp3", "music2.mp3"]
x = 0

# Загружаем изображения
cassette = pygame.image.load("1.jpeg").convert_alpha()  # Кассета
disk = pygame.image.load("2.jpeg").convert_alpha()  # Диски

# Координаты центров дисков
disk1_center = (150, 180)
disk2_center = (250, 180)

def rotate(image, angle, center):
    """Поворачивает изображение вокруг заданного центра"""
    rotated_image = pygame.transform.rotate(image, -angle)  
    new_rect = rotated_image.get_rect(center=center)  
    return rotated_image, new_rect.topleft

def play(x):
    pygame.mixer.music.load(mine[x])
    pygame.mixer.music.play(-1)

def stop():
    pygame.mixer.music.stop()

def previous():
    global x
    x = (x - 1) % len(mine)
    play(x)

run = True
while run:
    screen.fill((255, 255, 255))

    # Отображаем кассету
    screen.blit(cassette, (80, 80))

    # Определяем угол вращения по текущему времени
    now = datetime.datetime.now()
    angle = now.second * 6  # Каждую секунду диск поворачивается на 6 градусов

    # Вращаем и отображаем диски
    rotated_disk1, pos1 = rotate(disk, angle, disk1_center)
    rotated_disk2, pos2 = rotate(disk, angle, disk2_center)

    screen.blit(rotated_disk1, pos1)
    screen.blit(rotated_disk2, pos2)

    # Управление музыкой
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        play(x)
    if key[pygame.K_d]:
        stop()
    if key[pygame.K_w]:
        previous()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
