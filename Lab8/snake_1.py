import pygame
import sys
import random
pygame.init()

width, height = 600, 600
cell_size = 30

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Snake Game')

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Значения змейки
snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = "RIGHT"
change_to = direction

#Позиция и значение еды
food_pos = [random.randrange(1, width//cell_size) * cell_size, random.randrange(1, height//cell_size) * cell_size]
food_spawn = True
speed = 2

# Значения для добавлении очков и уровней
score_food = 0
level_snake = 1
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != 'DOWN':    
                change_to = 'UP'
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != 'UP':    
                change_to = 'DOWN'
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d)and direction != 'LEFT':    
                change_to = 'RIGHT'
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a)and direction != 'RIGHT':    
                change_to = 'LEFT'
    direction = change_to

    # Движение змейки
    if direction == 'UP':
        snake_pos[1] -= cell_size 
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size

    # Игра завершится если змея столкнется с границей
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False

    # Добавление новой головы в тело змеи
    snake_body.insert(0, list(snake_pos))

    # Игра завершится если змея столкнется со своим телом
    if snake_pos in snake_body[1:]:
        running = False 

    # Проверка еды и увеличиваем очко змейки, когда сьедает еду
    if abs(snake_pos[0] - food_pos[0]) < cell_size and abs(snake_pos[1] - food_pos[1]) < cell_size:
        food_spawn = False
        score_food += 1

        # Повышаем уровень и скорость змейки, когда змейка сьедает 3 еды
        if score_food % 3 == 0:  
            level_snake += 1
            speed += 1
    else:
        snake_body.pop()

    # Генерация еды
    if not food_spawn:
        food_pos = [random.randrange(0, width, cell_size), random.randrange(0, height, cell_size)]
        
        # Проверить не занята ли эта позиция телом змейки
        while food_pos in snake_body:
            food_pos = [random.randrange(0, width, cell_size), random.randrange(0, height, cell_size)]


        food_spawn = True

    # Отображение экрана
    screen.fill(black)
    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

    # Отображение счёта и уровня
    show_level = font.render(f"Level: {level_snake} ", True, white)
    show_score = font.render(f"Score: {score_food} ", True, white)
    screen.blit(show_level, (10, 10))
    screen.blit(show_score, (10, 40))
    

    pygame.display.flip()  
    clock.tick(speed)

pygame.quit()
sys.exit()
