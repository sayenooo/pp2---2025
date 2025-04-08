# Импортируем библиотеку pygame
import pygame

# Инициализируем pygame (обязательный шаг перед использованием)
pygame.init()

# ---------------- НАСТРОЙКИ ОКНА ----------------

# Устанавливаем размеры окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Создаём само окно с заданными размерами
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ---------------- НАСТРОЙКИ ШРИФТА ----------------

# Загружаем системный шрифт Arial, размер 30
# bold = True → жирный шрифт
# italic = True → курсив
font = pygame.font.SysFont("Arial", 30, bold=True, italic=True)

# ---------------- ФУНКЦИЯ ОТРИСОВКИ ТЕКСТА ----------------

# Функция, которая принимает текст, шрифт, цвет и координаты
def draw_text(text, font, color, x, y):
    # Рендерим текст — создаём изображение с заданным текстом
    img = font.render(text, True, color)
    # Отображаем его на экране в точке (x, y)
    screen.blit(img, (x, y))

# ---------------- ОСНОВНОЙ ЦИКЛ ----------------

run = True  # флаг, чтобы игра не закрывалась сразу

while run:
    # Заливаем экран белым цветом каждый кадр
    screen.fill((255, 255, 255))
    
    # Рисуем текст на экране: "HELLO EVERYBODY"
    # Цвет текста: тёмно-зелёный (0, 31, 23)
    draw_text("HELLO EVERYBODY", font, (0, 31, 23), 200, 200)
    
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Если нажали на крестик — выходим из цикла

    # Обновляем экран
    pygame.display.flip()

# После выхода из цикла — закрываем окно и завершаем pygame
pygame.quit()
