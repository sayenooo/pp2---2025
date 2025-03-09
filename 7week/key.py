import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

x = 30
y = 30
player = pygame.Rect(x, y, 10, 10)

run = True
while run:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]: 
        y -= 5
    if key[pygame.K_DOWN]: 
        y += 5                          
    if key[pygame.K_LEFT]: 
        x -= 5  
    if key[pygame.K_RIGHT]: 
        x += 5  

    player.topleft = (x, y)
    clock.tick(60)

    pygame.draw.rect(screen, (32, 234, 45), player)
    pygame.display.update()

pygame.quit()
