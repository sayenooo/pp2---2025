import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

run = True
running = False
sprinting = False
while run:
    screen.fill((0,0,0))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                running = True
            if  event.key == pygame.K_a:
                sprinting = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                running = False
            if  event.key == pygame.K_a:
                sprinting = False
    if running:
        print("NEVER GIVE UP")
    if sprinting:
        print("u've got this girl")
   
        
            
    pygame.display.flip()
    clock.tick(60)
        
pygame.quit()