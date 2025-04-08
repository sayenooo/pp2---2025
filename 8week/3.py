# Импорт необходимых библиотек
import pygame
import random
from pygame.math import Vector2
import time

# Инициализация pygame
pygame.init()

# Размеры экрана
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Настройка FPS и таймера
clock = pygame.time.Clock()
FPS = 60
running = True

# Флаги для состояния ввода
LMBpressed = False         # Левая кнопка мыши нажата
shift_pressed = False      # Нажата клавиша Shift (для рисования прямоугольника)
ctrl_pressed = False       # Нажата клавиша Ctrl (для рисования круга)
eraser_mode = False        # Активирован режим ластика

# Толщина кисти и ластика
THICKNESS = 5
ERASER_THICKNESS = 15

# Предыдущие координаты мыши
prevX = None
prevY = None

# Начальные и конечные координаты фигуры (для прямоугольников и кругов)
start_pos = None
end_pos = None

# Цвет по умолчанию
color = "red"

# Список нарисованных фигур
drawn_shapes = []

# Функция для рисования прямоугольника
def draw_rect(x1, y1, x2, y2, color, thickness):
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, color, rect, thickness) 

# Функция для рисования круга
def draw_circle(x1, y1, x2, y2, color, thickness):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = max(abs(x2 - x1), abs(y2 - y1)) // 2
    pygame.draw.circle(screen, color, (center_x, center_y), radius, thickness)


# Основной цикл приложения
while running:
    # Очистка экрана
    screen.fill("black")

    # Отрисовка всех сохранённых фигур
    for shape in drawn_shapes:
        shape_type, *params = shape

        if shape_type == "line":
            pygame.draw.line(screen, *params)
        elif shape_type == "rect":
            draw_rect(*params)
        elif shape_type == "circle":
            draw_circle(*params)
        elif shape_type == "eraser":
            pygame.draw.line(screen, *params)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Нажата ЛКМ
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos
            start_pos = event.pos
            
        # Движение мыши
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                end_pos = event.pos

                # Свободное рисование линий
                if not shift_pressed and not ctrl_pressed and prevX is not None and not eraser_mode:
                    drawn_shapes.append(("line", color, (prevX, prevY), event.pos, THICKNESS))
                    prevX, prevY = event.pos
                # Режим ластика
                if eraser_mode and prevX is not None:
                    drawn_shapes.append(("eraser", "black", (prevX, prevY), event.pos, ERASER_THICKNESS))
                    prevX, prevY = event.pos

        # Отпускание ЛКМ — завершение рисования фигуры
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False

            # Сохранение прямоугольника
            if shift_pressed and start_pos and end_pos:
                drawn_shapes.append(("rect", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))
            # Сохранение круга
            if ctrl_pressed and start_pos and end_pos:
                drawn_shapes.append(("circle", start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS))

            start_pos = None
            end_pos = None

        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_EQUALS:         # Увеличить толщину кисти
                THICKNESS += 1
            if event.key == pygame.K_MINUS:          # Уменьшить толщину кисти
                THICKNESS = max(1, THICKNESS - 1)

            # Смена цвета
            if event.key == pygame.K_r:
                color = "red"
            if event.key == pygame.K_g:
                color = "green"
            if event.key == pygame.K_b:
                color = "blue"

            # Включение режимов
            if event.key == pygame.K_LSHIFT:
                shift_pressed = True
            if event.key == pygame.K_LCTRL:
                ctrl_pressed = True
            if event.key == pygame.K_e:
                eraser_mode = True
            if event.key == pygame.K_q:
                eraser_mode = False
            if event.key == pygame.K_c:  # Очистить экран
                drawn_shapes.clear()
        
        # Отпускание клавиш
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                shift_pressed = False
            if event.key == pygame.K_LCTRL:
                ctrl_pressed = False
            
    # Предпросмотр фигуры при рисовании (не сохраняется до отпускания мыши)
    if shift_pressed and LMBpressed and start_pos and end_pos:
        draw_rect(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)
    if ctrl_pressed and LMBpressed and start_pos and end_pos:
        draw_circle(start_pos[0], start_pos[1], end_pos[0], end_pos[1], color, THICKNESS)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)


''''
Клавиша	Действие
R / G / B	Цвет: красный / зелёный / синий
Shift	Режим прямоугольников
Ctrl	Режим кругов
E	Ластик
Q	Выключить ластик
C	Очистить экран
= / -	Изменение толщины линии
'''