import pygame
pygame.init()

# 1part
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working with rectangles")

rec1 = pygame.Rect(200, 100, 150, 100)

# Загрузка изображения
soldier = pygame.image.load("soldier.png").convert_alpha()
rec2 = soldier.get_rect(topleft=(300, 300))  # Устанавливаем начальные координаты

clock = pygame.time.Clock()
color = (231,43,64)

# 2PART
run = True
is_blue = True
while run:
    # 3part
    screen.fill((0,0,0))    
    # Отрисовка объектов
    pygame.draw.rect(screen, color, rec1)
    pygame.draw.rect(screen, (231, 4, 45), rec2)
    screen.blit(soldier, rec2)
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    # Обработка клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        rec2.x -= 5
    if keys[pygame.K_d]:
        rec2.x += 5
    if keys[pygame.K_w]:
        rec2.y -= 5
    if keys[pygame.K_s]:
        rec2.y += 5
        is_blue = not is_blue
        
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    pygame.draw.rect(screen, color, rec1)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
