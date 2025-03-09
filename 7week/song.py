import pygame
pygame.init()

#1part

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Working with rectangles")

pygame.mixer.Sound.load('sound.wav')
pygame.mixer.Sound.play(-1)

pygame.mixer.Sound.load('sound1.wav')


#2PART

run = True
while run:
    #3part
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
            

pygame.quit()