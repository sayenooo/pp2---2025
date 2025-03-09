import pygame
pygame.init()

#1part

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("red ball")
clock = pygame.time.Clock()
x = 5
y = 5
#2PART

run = True
while run:
    #3part
    screen.fill((255,255,255))
    circle = pygame.draw.circle(screen,(255,0,0),(x,y),25)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and y-50>=0:
        y -= 20
    if key[pygame.K_DOWN] and y+50<=SCREEN_HEIGTH:
        y += 20
    if key[pygame.K_LEFT] and x-50>=0:
        x -= 20
    if key[pygame.K_RIGHT] and x+50<=SCREEN_WIDTH:
        x += 20
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    clock.tick(60)       
    pygame.display.flip()
            

pygame.quit()