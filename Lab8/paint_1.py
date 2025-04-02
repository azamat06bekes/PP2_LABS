import pygame
import sys

pygame.init()
width, height = 1000, 600
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
mode = 'brush'  # Возможные режимы: 'brush', 'rectangle', 'circle', 'eraser'
start_pos = None

temp_surface = screen.copy()

class Button:
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
def set_brush():
    global mode
    mode = 'brush'

def set_rectangle():
    global mode
    mode = 'rectangle'

def set_circle():
    global mode
    mode = 'circle'

def set_eraser():
    global mode
    mode = 'eraser'

def set_black():
    global brush_color
    brush_color = black

def set_red():
    global brush_color
    brush_color = red

def set_green():
    global brush_color
    brush_color = green

def set_blue():
    global brush_color
    brush_color = blue

def clear_screen():
    global temp_surface
    screen.fill(white)
    temp_surface = screen.copy()
    pygame.display.flip()

def exit_app():
    pygame.quit()
    sys.exit()

# Создание кнопок
buttons = [
    Button(10, 10, 60, 30, 'Brush', gray, set_brush),
    Button(80, 10, 100, 30, 'Rectangle', gray, set_rectangle),
    Button(190, 10, 80, 30, 'Circle', gray, set_circle),
    Button(270, 10, 80, 30, 'Eraser', gray, set_eraser),
    Button(360, 10, 60, 30, 'Black', black, set_black),
    Button(430, 10, 60, 30, 'Red', red, set_red),
    Button(500, 10, 60, 30, 'Green', green, set_green),
    Button(570, 10, 60, 30, 'Blue', blue, set_blue),
    Button(650, 10, 80, 30, 'Clear', gray, clear_screen),
    Button(720, 10, 60, 30, 'Exit', gray, exit_app),
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
    elif drawing and mode in ['rectangle', 'circle']:
        screen.blit(temp_surface, (0, 0))
        end_pos = pygame.mouse.get_pos()
        if mode == 'rectangle':
            rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]), abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
            pygame.draw.rect(screen, brush_color, rect, 2)
        elif mode == 'circle':
            radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
            pygame.draw.circle(screen, brush_color, start_pos, radius, 2)
    
    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    for button in buttons:
        button.draw(screen)
    
    pygame.display.flip()
