import pygame
from math import sqrt

def main():
    pygame.init()  # Инициализация библиотеки pygame
    screen = pygame.display.set_mode((640, 480))  # Установка размера окна
    clock = pygame.time.Clock()  # Создание объекта для управления частотой обновлений экрана
    
    radius = 15  # Начальный радиус точек
    color = (0, 0, 255)  # Начальный цвет, по умолчанию синий
    mode = 'blue'
    points = []  # Список для хранения точек, через которые будет рисоваться линия
    
    while True:  # Главный игровой цикл
        pressed = pygame.key.get_pressed()  # Получение состояния всех клавиш

        alt_left_held = pressed[pygame.K_LALT]  # circle
        alt_right_held = pressed[pygame.K_RALT]  # rhombus
        ctrl_left_held = pressed[pygame.K_LCTRL]  # rect
        ctrl_right_held = pressed[pygame.K_RCTRL]  # square
        shift_left_held = pressed[pygame.K_LSHIFT]  # right triangle
        shift_right_held = pressed[pygame.K_RSHIFT]  # equilateral triangle
        
        for event in pygame.event.get():  # Обработка всех событий
            if event.type == pygame.QUIT:
                return  # Закрыть программу

            # Обработка нажатия клавиш
            if event.type == pygame.KEYDOWN:
                # Клавиши для рисования фигур
                if alt_left_held:
                    x1, y1 = pygame.mouse.get_pos()  # Начальные координаты
                    x2, y2 = x1 + 50, y1 + 50  # Примерные координаты второго угла
                    circle(screen, x1, y1, x2, y2, color)

                if alt_right_held:
                    x1, y1 = pygame.mouse.get_pos()  # Начальные координаты
                    x2, y2 = x1 + 50, y1 + 50  # Примерные координаты второго угла
                    rhombus(screen, x1, y1, x2, y2, color)

                if ctrl_left_held:
                    x1, y1 = pygame.mouse.get_pos()  # Начальные координаты
                    x2, y2 = x1 + 50, y1 + 50  # Примерные координаты второго угла
                    rect(screen, x1, y1, x2, y2, color)

                if ctrl_right_held:
                    x1, y1 = pygame.mouse.get_pos()  # Начальные координаты
                    x2, y2 = x1 + 50, y1 + 50  # Примерные координаты второго угла
                    square(screen, x1, y1, x2, y2, color)

                if shift_left_held:
                    x1, y1 = pygame.mouse.get_pos()  # Начальные координаты
                    x2, y2 = x1 + 50, y1 + 50  # Примерные координаты второго угла
                    right(screen, x1, y1, x2, y2, color)

                if shift_right_held:
                    x1, y1 = pygame.mouse.get_pos()  # Начальные координаты
                    x2, y2 = x1 + 50, y1 + 50  # Примерные координаты второго угла
                    equip(screen, x1, y1, x2, y2, color)

                # Изменение цвета
                if event.key == pygame.K_r:
                    color = (255, 0, 0)
                    mode = 'red'
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)
                    mode = 'green'
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)
                    mode = 'blue'
                if event.key == pygame.K_e:
                    color = (0, 0, 0)
                if event.key == pygame.K_c:
                    screen.fill((0, 0, 0))
            
            # Обработка нажатия кнопок мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левый клик мыши увеличивает радиус
                    radius = min(200, radius + 1)
                elif event.button == 3:  # Правый клик мыши уменьшает радиус
                    radius = max(1, radius - 1)

            # Обработка движения мыши
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append(position)
                points = points[-256:]  # Оставляем только последние 256 точек

        screen.fill((0, 0, 0))  # Заполнение экрана черным цветом перед отрисовкой

        # Рисуем все точки, соединенные линиями
        for i in range(len(points) - 1):
            drawLineBetween(screen, points[i], points[i + 1], radius, mode)  # Рисуем линию между точками
        
        pygame.display.flip()  # Обновляем экран
        
        clock.tick(60)  # Ограничение обновлений экрана до 60 кадров в секунду

def drawLineBetween(screen, start, end, width, color_mode):
    # Выбор цвета в зависимости от режима
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)
    
    # Рисуем линию
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))  # Количество шагов для рисования линии
    
    # Процесс рисования линии с помощью точек между начальной и конечной точкой
    for i in range(iterations):
        progress = 1.0 * i / iterations  # Прогресс рисования
        aprogress = 1 - progress  # Обратный прогресс
        x = int(aprogress * start[0] + progress * end[0])  # Вычисляем позицию X на линии
        y = int(aprogress * start[1] + progress * end[1])  # Вычисляем позицию Y на линии
        pygame.draw.circle(screen, color, (x, y), width)  # Рисуем маленький круг для отображения линии

#circle   
def circle(screen, x1, y1, x2, y2, color):
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = max(abs(x2 - x1), abs(y2 - y1)) // 2
    pygame.draw.circle(screen, color, (center_x, center_y), radius, 4)

#rhombus  
def rhombus(screen, x1, y1, x2, y2, color):
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
    pygame.draw.polygon(screen, color, points, 4)

#rect    
def rect(screen, x1, y1, x2, y2, color):
    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, color, rect, 4)
    
#square   
def square(screen, x1, y1, x2, y2, color):
    square = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(x2 - x1))
    pygame.draw.rect(screen, color, square, 4)
        
#right t  
def right(screen, x1, y1, x2, y2, color):
    side_length = abs(x2 - x1)  # Длина стороны треугольника
    height = (sqrt(3) / 2) * side_length 
    pygame.draw.polygon(screen, color, [[(x1+x2)//2, y1], [x1, y1 + height], [x2, y1 + height]], 4)

#equip t  
def equip(screen, x1, y1, x2, y2, color):
    pygame.draw.polygon(screen, color, [[x1, y2], [x2, y2], [(x1+x2)//2, y1]], 4)

main()  # Запуск программы
