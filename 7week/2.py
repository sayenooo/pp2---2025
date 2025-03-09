import pygame
import datetime

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My favourite songs")

mine = ["music.mp3", "music1.mp3", "music2.mp3"]
x = 0
image = pygame.image.load("1.jpeg").convert_alpha()
image1 = pygame.image.load("disk.png").convert_alpha()

center1 = (125//2, 120//2)
center2 = (220//2, 120//2)

def play(x):
   pygame.mixer.music.load(mine[x])
   pygame.mixer.music.play(-1)
def stop():
     pygame.mixer.music.stop()
def previous():
    global x
    if x>0:
        x-=1
    else:
        x = len(mine)-1
    pygame.mixer.music.load(mine[x])
    play(x)

   
run = True
while run:
    screen.fill((255, 255, 255))
    screen.blit(image,(80,100))
    time = datetime.datetime.now()
    angle = time.second * 6
    img = pygame.transform.rotate(image1, angle)
    img1 = img.get_rect(center=center1)
    img2 = img.get_rect(center=center2)
    
    screen.blit(img, (125,140))
    screen.blit(img, (220,140))
    
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