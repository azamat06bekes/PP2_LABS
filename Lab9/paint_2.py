import pygame
import sys

pygame.init()
width, height = 1200, 620
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Paint')

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

drawing = False
brush_color = black
mode = 'brush'  # Возможные режимы: 'brush', 'rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus', 'eraser'
start_pos = None

temp_surface = screen.copy()

class Button:
    """Класс кнопки для управления инструментами"""
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text_surface = font.render(self.text, True, white if self.color != white else black)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 8))
    
    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.action()

# Функции смены режимов и цветов
def set_mode(new_mode):
    global mode
    mode = new_mode

def set_color(new_color):
    global brush_color
    brush_color = new_color

def clear_screen():
    """Очищает экран"""
    global temp_surface
    screen.fill(white)
    temp_surface = screen.copy()
    pygame.display.flip()

def exit_app():
    """Закрывает приложение"""
    pygame.quit()
    sys.exit()

# Создание кнопок
buttons = [
    Button(10, 10, 60, 30, 'Brush', gray, lambda: set_mode('brush')),
    Button(70, 10, 100, 30, 'Rectangle', gray, lambda: set_mode('rectangle')),
    Button(170, 10, 70, 30, 'Circle', gray, lambda: set_mode('circle')),
    Button(230, 10, 70, 30, 'Square', gray, lambda: set_mode('square')),
    Button(310, 10, 80, 30, 'Right Tri.', gray, lambda: set_mode('right_triangle')),
    Button(390, 10, 80, 30, 'Equi. Tri.', gray, lambda: set_mode('equilateral_triangle')),
    Button(470, 10, 80, 30, 'Rhombus', gray, lambda: set_mode('rhombus')),
    Button(560, 10, 80, 30, 'Eraser', gray, lambda: set_mode('eraser')),
    Button(650, 10, 60, 30, 'Black', black, lambda: set_color(black)),
    Button(720, 10, 60, 30, 'Red', red, lambda: set_color(red)),
    Button(790, 10, 60, 30, 'Green', green, lambda: set_color(green)),
    Button(860, 10, 60, 30, 'Blue', blue, lambda: set_color(blue)),
    Button(940, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(1000, 10, 60, 30, 'Exit', gray, exit_app),
]

clear_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
                drawing = True
                temp_surface = screen.copy()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        
        for button in buttons:
            button.check_action(event)
    
    if drawing and mode == 'brush':
        pygame.draw.circle(screen, brush_color, pygame.mouse.get_pos(), 5)
    elif drawing and mode == 'eraser':
        pygame.draw.circle(screen, white, pygame.mouse.get_pos(), 10)
    elif drawing and mode in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
        screen.blit(temp_surface, (0, 0))
        end_pos = pygame.mouse.get_pos()
        
        if mode == 'rectangle':
            pygame.draw.rect(screen, brush_color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 2)
        elif mode == 'square':
            side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
            pygame.draw.rect(screen, brush_color, pygame.Rect(start_pos, (side, side)), 2)
        elif mode == 'circle':
            radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
            pygame.draw.circle(screen, brush_color, start_pos, radius, 2)
        elif mode == 'right_triangle':
            pygame.draw.polygon(screen, brush_color, [start_pos, (start_pos[0], end_pos[1]), end_pos], 2)
        elif mode == 'equilateral_triangle':
            height = abs(end_pos[1] - start_pos[1])
            base = height * (3 ** 0.5)
            pygame.draw.polygon(screen, brush_color, [start_pos, (start_pos[0] + base / 2, end_pos[1]), (start_pos[0] - base / 2, end_pos[1])], 2)
        elif mode == 'rhombus':
            center_x, center_y = start_pos
            dx = abs(end_pos[0] - start_pos[0])
            dy = abs(end_pos[1] - start_pos[1])
            pygame.draw.polygon(screen, brush_color, [(center_x, center_y - dy), (center_x + dx, center_y), (center_x, center_y + dy), (center_x - dx, center_y)], 2)
    
    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    for button in buttons:
        button.draw(screen)
    
    pygame.display.flip()