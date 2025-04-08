import pygame
import random
from pygame.math import Vector2
from math import *
import time

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600  # Размеры окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание экрана с заданными размерами
pygame.display.set_caption("Рисовалка")  # Заголовок окна

# Основные параметры
clock = pygame.time.Clock()  # Часы для управления частотой кадров
FPS = 60  # Частота кадров в секунду
running = True  # Флаг работы главного цикла

# Состояния клавиш и мыши
LMBpressed = False  # Переменная, указывающая на то, что левая кнопка мыши нажата
lshift_pressed = rshift_pressed = False  # Состояния клавиш Shift (левая и правая)
lctrl_pressed = rctrl_pressed = False  # Состояния клавиш Ctrl (левая и правая)
lalt_pressed = ralt_pressed = False  # Состояния клавиш Alt (левая и правая)
eraser_mode = False  # Флаг, показывающий, активирован ли режим стирания

# Толщина линий и стирания
THICKNESS = 5  # Толщина линий по умолчанию
ERASER_THICKNESS = 15  # Толщина стирания

# Цвет по умолчанию
color = "red"  # Начальный цвет для рисования (красный)

# Предыдущая позиция мыши и начальная точка фигуры
prevX = prevY = None  # Для рисования линии по предыдущей точке
start_pos = end_pos = None  # Начальная и конечная точка для рисования фигур

# Список всех нарисованных объектов, чтобы их можно было отрисовать после очистки экрана
drawn_shapes = []

# ----------- Функции рисования фигур -----------
def rect(x1, y1, x2, y2, color, thickness):
    """Рисует прямоугольник"""
    pygame.draw.rect(screen, color, pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), thickness)

def circle(x1, y1, x2, y2, color, thickness):
    """Рисует круг"""
    cx = (x1 + x2) // 2  # Центр по оси X
    cy = (y1 + y2) // 2  # Центр по оси Y
    radius = max(abs(x2 - x1), abs(y2 - y1)) // 2  # Радиус круга
    pygame.draw.circle(screen, color, (cx, cy), radius, thickness)

def square(x1, y1, x2, y2, color, thickness):
    """Рисует квадрат (по сути, прямоугольник с одинаковыми сторонами)"""
    side = abs(x2 - x1)  # Сторона квадрата
    pygame.draw.rect(screen, color, pygame.Rect(min(x1, x2), min(y1, y2), side, side), thickness)

def right(x1, y1, x2, y2, color, thickness):
    """Рисует равносторонний треугольник"""
    side = abs(x2 - x1)  # Длина стороны треугольника
    height = int((sqrt(3) / 2) * side)  # Высота треугольника (по формуле для равностороннего)
    pygame.draw.polygon(screen, color, [[(x1 + x2) // 2, y1], [x1, y1 + height], [x2, y1 + height]], thickness)

def equip(x1, y1, x2, y2, color, thickness):
    """Рисует треугольник (по форме похож на "щит")"""
    pygame.draw.polygon(screen, color, [[x1, y2], [x2, y2], [(x1 + x2) // 2, y1]], thickness)

def rhombus(x1, y1, x2, y2, color, thickness):
    """Рисует ромб"""
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # Центр ромба
    half_w, half_h = abs(x2 - x1) // 2, abs(y2 - y1) // 2  # Половина ширины и высоты ромба
    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]  # Точки ромба
    pygame.draw.polygon(screen, color, points, thickness)

# --------------- Главный цикл ---------------
while running:
    screen.fill("black")  # Очистка экрана (черный фон)

    # Перерисовываем все сохранённые фигуры
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
            rhombus(*params)
        elif shape_type == "right":
            right(*params)
        elif shape_type == "equip":
            equip(*params)
        elif shape_type == "eraser":
            pygame.draw.line(screen, *params)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Выход из цикла при закрытии окна

        # Нажатие мыши (левой кнопкой)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos  # Сохраняем начальную точку для рисования
            start_pos = event.pos  # Начальная точка для фигур

        # Движение мыши
        if event.type == pygame.MOUSEMOTION and LMBpressed:
            end_pos = event.pos  # Конечная точка движения мыши

            # Если не активированы клавиши модификаторы для рисования фигур
            if not any([lshift_pressed, lctrl_pressed, rshift_pressed, rctrl_pressed, lalt_pressed, ralt_pressed]):
                if not eraser_mode:  # Рисуем линию, если не в режиме стирания
                    drawn_shapes.append(("line", color, (prevX, prevY), event.pos, THICKNESS))
                else:  # В режиме стирания рисуем линию с цветом "черный"
                    drawn_shapes.append(("eraser", "black", (prevX, prevY), event.pos, ERASER_THICKNESS))
                prevX, prevY = event.pos  # Обновляем предыдущую позицию для рисования

        # Отпускание мыши
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            if start_pos and end_pos:
                x1, y1 = start_pos
                x2, y2 = end_pos

                # Сохраняем нарисованные фигуры
                if lshift_pressed:
                    drawn_shapes.append(("rect", x1, y1, x2, y2, color, THICKNESS))
                elif lctrl_pressed:
                    drawn_shapes.append(("circle", x1, y1, x2, y2, color, THICKNESS))
                elif lalt_pressed:
                    drawn_shapes.append(("square", x1, y1, x2, y2, color, THICKNESS))
                elif rshift_pressed:
                    drawn_shapes.append(("right", x1, y1, x2, y2, color, THICKNESS))
                elif rctrl_pressed:
                    drawn_shapes.append(("rhombus", x1, y1, x2, y2, color, THICKNESS))
                elif ralt_pressed:
                    drawn_shapes.append(("equip", x1, y1, x2, y2, color, THICKNESS))
            start_pos = end_pos = None  # Сброс начальной и конечной точки

        # Нажатие клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1  # Увеличиваем толщину линий
            elif event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)  # Уменьшаем толщину, не ниже 1
            elif event.key == pygame.K_r:
                color = "red"  # Выбираем красный цвет
            elif event.key == pygame.K_g:
                color = "green"  # Выбираем зеленый цвет
            elif event.key == pygame.K_b:
                color = "blue"  # Выбираем синий цвет
            elif event.key == pygame.K_e:
                eraser_mode = True  # Включаем режим стирания
            elif event.key == pygame.K_q:
                eraser_mode = False  # Выключаем режим стирания
            elif event.key == pygame.K_c:
                drawn_shapes.clear()  # Очищаем все нарисованные фигуры
            elif event.key == pygame.K_LSHIFT:
                lshift_pressed = True  # Включаем режим рисования прямоугольников
            elif event.key == pygame.K_LCTRL:
                lctrl_pressed = True  # Включаем режим рисования кругов
            elif event.key == pygame.K_LALT:
                lalt_pressed = True  # Включаем режим рисования квадратов
            elif event.key == pygame.K_RSHIFT:
                rshift_pressed = True  # Включаем режим рисования треугольников
            elif event.key == pygame.K_RCTRL:
                rctrl_pressed = True  # Включаем режим рисования ромбов
            elif event.key == pygame.K_RALT:
                ralt_pressed = True  # Включаем режим рисования "щита"

        # Отпускание клавиш
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                lshift_pressed = False
            elif event.key == pygame.K_LCTRL:
                lctrl_pressed = False
            elif event.key == pygame.K_LALT:
                lalt_pressed = False
            elif event.key == pygame.K_RSHIFT:
                rshift_pressed = False
            elif event.key == pygame.K_RCTRL:
                rctrl_pressed = False
            elif event.key == pygame.K_RALT:
                ralt_pressed = False

    # Предпросмотр фигуры (визуализация до отпускания мыши)
    if LMBpressed and start_pos and end_pos:
        x1, y1 = start_pos
        x2, y2 = end_pos
        # Рисуем предварительный вид фигуры в процессе её рисования
        if lshift_pressed:
            rect(x1, y1, x2, y2, color, THICKNESS)
        elif lctrl_pressed:
            circle(x1, y1, x2, y2, color, THICKNESS)
        elif lalt_pressed:
            square(x1, y1, x2, y2, color, THICKNESS)
        elif rshift_pressed:
            right(x1, y1, x2, y2, color, THICKNESS)
        elif rctrl_pressed:
            rhombus(x1, y1, x2, y2, color, THICKNESS)
        elif ralt_pressed:
            equip(x1, y1, x2, y2, color, THICKNESS)

    pygame.display.flip()  # Обновление экрана
    clock.tick(FPS)  # Поддержание частоты кадров

pygame.quit()  # Завершаем работу Pygame
