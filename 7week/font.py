import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("Arial", 30, bold = True, italic = True)

def draw_text(text,font,color,x,y):
    img = font.render(text,True,color)
    screen.blit(img,(x,y))
    
    

run = True

while run:
    screen.fill((255, 255, 255))
    
    draw_text("HELLO EVERYBODY", font, (0,31,23), 200, 200)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
         
    pygame.display.flip()

pygame.quit()
