import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Working with shapes")
clock = pygame.time.Clock()
run = True
x = 0
while run:
    screen.fill((255,255,255))
    
    if pygame.mouse.get_pressed()[0]:
        x+=0.001
    else:
        x-=0.001
    
    pygame.draw.rect(screen, (43,64,123), (200,180, 100, 100), width = 5, border_bottom_right_radius = 50)
    pygame.draw.circle(screen, (0,43,234), (100,100), 25, 3)
    pygame.draw.circle(screen, (43,54,34), (300,300), 50, draw_top_right = True, draw_bottom_left = True)
    pygame.draw.ellipse(screen, (43,243,234), (120,120, 23, 56))
    pygame.draw.arc(screen, (245,200,0), (350,350, 100, 100), 0, x, width = 5)
    pygame.draw.line(screen, (43, 54, 78), (300, 300), (x,46) )
    pygame.draw.polygon(screen, (243, 228, 210),( (213,654), (95, 52), (324,21), (423,65)))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    clock.tick(9000000000000000000000000000000000000000000000000000000000000)
    pygame.display.flip()


pygame.quit()