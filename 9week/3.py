import pygame
import random
from pygame.math import Vector2
from math import*
import time

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60
running = True

LMBpressed = False  # Left mouse button pressed
lshift_pressed = False  # left Shift key pressed
rshift_pressed = False  # right Shift key pressed
lctrl_pressed = False  # left Control key pressed
rctrl_pressed = False
lalt_pressed = False  # left Alt key pressed
ralt_pressed = False# right Alt key pressed
eraser_mode = False  # Eraser mode active

# Drawing settings
THICKNESS = 5
ERASER_THICKNESS = 15

# Previous mouse position for drawing lines
prevX = None
prevY = None

# Start and end positions for drawing shapes
start_pos = None
end_pos = None


color = "red" #default drawing color

# List to store drawn shapes
drawn_shapes = []

#rectangle lshift
def rect(x1, y1, x2, y2, color, thickness):
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, color, rect, thickness) 

#circle lctrl
def circle(x1, y1, x2, y2, color, thickness):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = max(abs(x2 - x1), abs(y2 - y1)) // 2
    pygame.draw.circle(screen, color, (center_x, center_y), radius, thickness)
    
#square   lalt
def square(x1, y1, x2, y2, color, thickness):
    square = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(x2 - x1))
    pygame.draw.rect(screen, color, square, thickness) 
    
#right t ralt 
def right(x1, y1, x2, y2, color, thickness):
    side_length = abs(x2 - x1)  # Длина стороны треугольника
    height = (sqrt(3) / 2) * side_length 
    pygame.draw.polygon(screen, color, [[(x1+x2)//2, y1], [x1, y1 + height], [x2, y2 + height]], thickness)

#equip t  rshift
def equip(x1, y1, x2, y2, color, thickness):
    pygame.draw.polygon(screen, color, [[x1, y2], [x2, y2], [(x1+x2)//2, y1]], thickness)

#rhombus rshift    
def rhombus(x1, y1, x2, y2, color, thickness):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    width = abs(x2 - x1) // 2
    height = abs(y2 - y1) // 2
    points = [
        (center_x, y1),  # Верхняя точка
        (x2, center_y),  # Правая точка
        (center_x, y2),  # Нижняя точка
        (x1, center_y)   # Левая точка
    ]
    pygame.draw.polygon(screen, color, points, thickness)


while running:
    # Fill the screen with black to refresh the drawing
    screen.fill("black")

    # Redraw all saved shapes
    for shape in drawn_shapes:
        shape_type, *params = shape

        if shape_type == "line":
            pygame.draw.line(screen, *params)
        elif shape_type == "rect":
            rect(*params)
        elif shape_type == "circle":
            circle(*params)
        elif shape_type == "square":
            square(*params)
        elif shape_type == "rhombus":
            square(*params)
        elif shape_type == "right":
            right(*params)
        elif shape_type == "equip":
            right(*params)
        elif shape_type == "eraser":
            pygame.draw.line(screen, *params)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse button press event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            # Store start position for shapes
            prevX = event.pos[0]
            prevY = event.pos[1]
            start_pos = event.pos
            
        # Mouse movement event
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                end_pos = event.pos

                # Drawing freehand lines
                if not lshift_pressed and not lctrl_pressed and not rshift_pressed and not rctrl_pressed and prevX is not None and not eraser_mode:
                    drawn_shapes.append(("line", color, (prevX, prevY), event.pos, THICKNESS))
                    prevX = event.pos[0]
                    prevY = event.pos[1]
               # Eraser mode 
                if eraser_mode and prevX is not None:
                    drawn_shapes.append(("eraser", "black", (prevX, prevY), event.pos, ERASER_THICKNESS))
                    prevX = event.pos[0]
                    prevY = event.pos[1]

        # Mouse button release event
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False

            #Save and drawing rectangles when Shift is pressed
            if lshift_pressed and start_pos and end_pos:
                drawn_shapes.append(("rect", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))
            #Save and drawing circles when Ctrl is pressed
            if lctrl_pressed and start_pos and end_pos:
                drawn_shapes.append(("circle", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))   
            #Save and drawing rectangles when Shift is pressed
            if lalt_pressed and start_pos and end_pos:
                drawn_shapes.append(("square", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))
                
            #Save and drawing rectangles when Shift is pressed
            if rshift_pressed and start_pos and end_pos:
                drawn_shapes.append(("right", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))
            #Save and drawing circles when Ctrl is pressed
            if rctrl_pressed and start_pos and end_pos:
                drawn_shapes.append(("rhombus", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))
            #Save and drawing circles when Ctrl is pressed
            if ralt_pressed and start_pos and end_pos:
                drawn_shapes.append(("equip", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))    
                
            start_pos = None
            end_pos = None


        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1  # Increase thickness
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)  # Deccrease thickness, can't be less than 1
            #changing the color
            if event.key == pygame.K_r:
                color = "red"
            if event.key == pygame.K_g:
                color = "green"
            if event.key == pygame.K_b:
                color = "blue"
            if event.key == pygame.K_LSHIFT: # rectangle drawing mode
                lshift_pressed = True
            if event.key == pygame.K_LCTRL: # circle drawing mode
                lctrl_pressed = True
            if event.key == pygame.K_LALT: # square drawing mode
                lalt_pressed = True
            if event.key == pygame.K_RSHIFT: # equip drawing mode
                rshift_pressed = True
            if event.key == pygame.K_RCTRL: # rhombus drawing mode
                rctrl_pressed = True
            if event.key == pygame.K_RALT: # right drawing mode
                ralt_pressed = True
            if event.key == pygame.K_e: # eraser mode
                eraser_mode = True
            if event.key == pygame.K_q: # disable eraser mode
                eraser_mode = False
            if event.key == pygame.K_c: # clear the screen
                drawn_shapes.clear()
        
        # Key release events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                lshift_pressed = False
            if event.key == pygame.K_LCTRL:
                lctrl_pressed = False
            if event.key == pygame.K_RSHIFT:
                rshift_pressed = False
            if event.key == pygame.K_RCTRL:
                rctrl_pressed = False
            if event.key == pygame.K_LALT:
                lalt_pressed = False
            if event.key == pygame.K_RALT:
                ralt_pressed = False
            
    # Preview shapes while drawing
    # Not saving them
    if lshift_pressed and LMBpressed and start_pos and end_pos:
        rect(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)
    if lctrl_pressed and LMBpressed and start_pos and end_pos:
        circle(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)
    if rshift_pressed and LMBpressed and start_pos and end_pos:
        right(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)
    if rctrl_pressed and LMBpressed and start_pos and end_pos:
        rhombus(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)
    if lalt_pressed and LMBpressed and start_pos and end_pos:
        square(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)
    if ralt_pressed and LMBpressed and start_pos and end_pos:
        equip(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)

    pygame.display.flip()
    clock.tick(FPS)
