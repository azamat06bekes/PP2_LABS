import pygame
import sys
import random
pygame.init()

width, height = 600, 600
cell_size = 30

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Snake Game')

# Цветa для фона и змейки 
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
grey = (192, 192, 192)

# Значения змейки
snake_pos = [100, 100]
snake_body = [[100, 100], [80, 100], [60, 100]]
direction = "RIGHT"
change_to = direction


# Изображения еды
apple_img = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\Lab9\apple.png").convert_alpha()
apple_img = pygame.transform.scale(apple_img, (cell_size + 20, cell_size + 20))

banana_img = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\Lab9\banana.png").convert_alpha()
banana_img = pygame.transform.scale(banana_img, (cell_size + 20, cell_size + 20))

burger_img = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\Lab9\burger.png").convert_alpha()
burger_img = pygame.transform.scale(burger_img, (cell_size + 20, cell_size + 20))

# Список еды
foods = [
    {"image": apple_img, "score": 1},
    {"image": banana_img, "score": 3},
    {"image": burger_img, "score": 7}
]

# Выбираем случайный фрукт
current_food = random.choice(foods)  

# Позиция еды и скорость змейки
food_pos = [random.randrange(1, width//cell_size) * cell_size, random.randrange(1, height//cell_size) * cell_size]
food_spawn = True
speed = 2
foods_eaten = 0  # Количество еды

# Значения для добавлении очков и уровней
score_food = 0
level_snake = 1
font = pygame.font.Font(None, 24)
clock = pygame.time.Clock()

# Время жизни еды (7-секунд) и запоминаем текущее время
food_lifetime = 7000  # это миллисекунд
food_timer = pygame.time.get_ticks()

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
        score_food += current_food["score"]
        foods_eaten += 1
        food_spawn = False

        # Повышаем уровень и скорость змейки, когда змейка сьедает 3 еды
        if foods_eaten == 3:  
            level_snake += 1
            speed += 1
            foods_eaten = 0
    else:
        snake_body.pop()

    # Генерация еды и проверяем, прошло ли 7 секунд с момента появления еды. А потом обновляем время
    if not food_spawn or pygame.time.get_ticks() - food_timer > food_lifetime:
        food_pos = [random.randrange(0, width, cell_size), random.randrange(0, height, cell_size)]
        
        # Проверить не занята ли эта позиция телом змейки
        while food_pos in snake_body:
            food_pos = [random.randrange(0, width, cell_size), random.randrange(0, height, cell_size)]

        food_timer = pygame.time.get_ticks()
        current_food = random.choice(foods)
        food_spawn = True

    # Отображение экрана
    bg_snake = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\Lab9\snake_bg.jpg")
    bg_snake = pygame.transform.scale(bg_snake, (width, height))
    screen.blit(bg_snake, (0,0))
    for block in snake_body:
        pygame.draw.rect(screen, blue, pygame.Rect(block[0], block[1], cell_size, cell_size))
    screen.blit(current_food["image"], (food_pos[0], food_pos[1]))

    # Отображение счёта и уровня
    show_level = font.render(f"Level: {level_snake} ", True, black)
    show_score = font.render(f"Score: {score_food} ", True, black)
    show_foods_eaten = font.render(f"Number of foods eaten: {foods_eaten} ", True, black)
    screen.blit(show_foods_eaten, (10, 10))
    screen.blit(show_level, (10, 30))
    screen.blit(show_score, (10, 50))
    
    

    pygame.display.flip()  
    clock.tick(speed)

pygame.quit()
sys.exit()
