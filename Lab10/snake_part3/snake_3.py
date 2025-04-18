import pygame
import sys
import random
import sqlite3
pygame.init()

# Подключение к базе данных (создаст файл, если его нет)
conn = sqlite3.connect("snake_game.db")
cursor = conn.cursor()

# Создание таблиц
cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    score INTEGER,
    level INTEGER,
    FOREIGN KEY (user_id) REFERENCES user(id)
)
""")

# Настройки экрана
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
apple_img = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\PP2_LABS\Lab10\apple.png").convert_alpha()
apple_img = pygame.transform.scale(apple_img, (cell_size + 20, cell_size + 20))

banana_img = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\PP2_LABS\Lab10\banana.png").convert_alpha()
banana_img = pygame.transform.scale(banana_img, (cell_size + 20, cell_size + 20))

burger_img = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\PP2_LABS\Lab10\burger.png").convert_alpha()
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
level_snake = 0
font = pygame.font.Font(None, 24)
clock = pygame.time.Clock()

def get_username_input():
    input_box = pygame.Rect(150, 250, 300, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font_input = pygame.font.Font(None, 36)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font_input.render(text, True, color)
        width_box = max(300, txt_surface.get_width()+10)
        input_box.w = width_box
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        title = font_input.render("Enter your name in English and press Enter", True, (255, 255, 255))
        screen.blit(title, (60, 200))

        pygame.display.flip()
        clock.tick(30)


# Время жизни еды (7-секунд) и запоминаем текущее время
food_lifetime = 7000  # это миллисекунд
food_timer = pygame.time.get_ticks()

# Логика препятствий: 1–3, 4-6, 7-9
def get_level_obstacles(level):
    if 1 <= level <= 3:
        return [("rect", (150, 150, 300, 30))]
    elif 4 <= level <= 6:
        return [("circle", (300, 300, 30)), ("rect", (100, 100, 30, 400))]
    elif 7 <= level <= 9:
        return [("diamond", (300, 300, 50))]
    else:
        return []  # Дальше без препятствий 

def check_collision(snake_rect, obstacle):
    shape, params = obstacle
    if shape == "rect":
        return snake_rect.colliderect(pygame.Rect(*params))
    elif shape == "circle":
        cx, cy, radius = params
        dx = snake_rect.centerx - cx - 20
        dy = snake_rect.centery - cy - 20
        return dx**2 + dy**2 < radius**2
    elif shape == "diamond":
        cx, cy, size = params
        dx = abs(snake_rect.centerx - cx)
        dy = abs(snake_rect.centery - cy)
        return dx + dy < size
    return False


# Запрос имени игрока и проверить есть ли такой пользователь
username = get_username_input()

# Показ предыдущих результатов после ввода имени
def show_user_history():
    screen.fill((30, 30, 30))
    font_history = pygame.font.Font(None, 32)

    # Изменённый запрос: получаем все результаты для всех пользователей
    cursor.execute("""
        SELECT username, score, level
        FROM user_score
        JOIN user ON user_score.user_id = user.id
        ORDER BY user_score.id DESC
    """)
    results = cursor.fetchall()

    title = font_history.render("All Game Results:", True, (255, 255, 255))
    screen.blit(title, (180, 100))

    if results:
        for i, (username, score, level) in enumerate(results[:10]):  # Покажем максимум 10 записей
            line = font_history.render(f"{i+1}) {username} | Score: {score} | Level: {level}", True, (200, 200, 200))
            screen.blit(line, (180, 150 + i * 40))
    else:
        no_data = font_history.render("No previous games found.", True, (200, 200, 200))
        screen.blit(no_data, (180, 150))

    pygame.display.flip()

    # Ждём нажатия клавиши для выхода
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False


cursor.execute("SELECT id FROM user WHERE username = ?", (username,))
user = cursor.fetchone()

# Если нет — добавляем
if not user:
    cursor.execute("INSERT INTO user (username) VALUES (?)", (username,))
    conn.commit()
    user_id = cursor.lastrowid
    cursor.execute("SELECT MAX(level) FROM user_score WHERE user_id = ?", (user_id,))
    prev_level = cursor.fetchone()[0]
    if prev_level:
        print(f"Добро пожаловать обратно, {username}! Ваш последний уровень был: {prev_level}")
        level_snake = prev_level  # можно начать с предыдущего уровня, если хочешь
    else:
        print(f"Привет, {username}! Это ваша первая игра.")
else:
    user_id = user[0]


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
            elif event.key == pygame.K_p:
                paused = True
                print("The game is on pause. Press P to continue.")
                # Сохраняем текущий результат при паузе
                cursor.execute("INSERT INTO user_score (user_id, score, level) VALUES (?, ?, ?)", (user_id, score_food, level_snake))
                conn.commit()
                pause_start = pygame.time.get_ticks() # Чтобы замерить начало паузы
                while paused:
                    for pause_event in pygame.event.get():
                        if pause_event.type == pygame.QUIT:
                            paused = False
                            running = False
                        elif pause_event.type == pygame.KEYDOWN and pause_event.key == pygame.K_p:
                            # Скорректировать таймер еды на время паузы
                            pause_duration = pygame.time.get_ticks() - pause_start
                            food_timer += pause_duration
                            paused = False
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
    if snake_pos[0] < 0 or snake_pos[0] >= width-40 or snake_pos[1] < 0 or snake_pos[1] >= height-40:
        running = False

    # Добавление новой головы в тело змеи
    snake_body.insert(0, list(snake_pos))

    # Игра завершится если змея столкнется со своим телом
    if snake_pos in snake_body[1:]:
        running = False 
    
    # Проверка столкновения с препятствиями (если есть на уровне)
    snake_rect = pygame.Rect(snake_pos[0], snake_pos[1], cell_size, cell_size)
    for obstacle in get_level_obstacles(level_snake):
        if check_collision(snake_rect, obstacle):
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

    # Генерация еды и проверяем, прошло ли 7 секунд с момента появления еды
    if not food_spawn or pygame.time.get_ticks() - food_timer > food_lifetime:
        def is_food_on_obstacle(pos):
            food_rect = pygame.Rect(pos[0], pos[1], cell_size, cell_size)
            for obstacle in get_level_obstacles(level_snake):
                if check_collision(food_rect, obstacle):
                    return True
            return False

        food_pos = [random.randrange(0, width-50, cell_size), random.randrange(0, height-50, cell_size)]

        # Пока еда попадает на тело змейки или на препятствие — выбираем новую позицию
        while food_pos in snake_body or is_food_on_obstacle(food_pos):
            food_pos = [random.randrange(0, width-50, cell_size+20), random.randrange(0, height-50, cell_size+20)]

        food_timer = pygame.time.get_ticks()  # обновляем таймер еды
        current_food = random.choice(foods)
        food_spawn = True


    # Отображение экрана
    backgrounds = {
        1: pygame.transform.scale(pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\PP2_LABS\Lab10\snake_bg1.jpg"), (width, height)),
        2: pygame.transform.scale(pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\PP2_LABS\Lab10\snake_bg2.jpg"), (width, height)),
        3: pygame.transform.scale(pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\PP2_LABS\Lab10\snake_bg3.jpg"), (width, height)),
        4: pygame.transform.scale(pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\PP2_LABS\Lab10\snake_bg3.jpg"), (width, height))
    }
    # Меняем фон каждые 2 уровня (1–2: фон 1, 3–4: фон 2, 5–6: фон 3 и т.д.)
    background_index = ((level_snake - 1) // 3) % len(backgrounds) + 1
    screen.blit(backgrounds[background_index], (0, 0))
    for block in snake_body:
        pygame.draw.rect(screen, blue, pygame.Rect(block[0], block[1], cell_size, cell_size))
    screen.blit(current_food["image"], (food_pos[0], food_pos[1]))

    # Отрисовка препятствий
    for obstacle in get_level_obstacles(level_snake):
        shape, params = obstacle
        if shape == "rect":
            pygame.draw.rect(screen, grey, pygame.Rect(*params))
        elif shape == "circle":
            pygame.draw.circle(screen, grey, (params[0], params[1]), params[2])
        elif shape == "diamond":
            cx, cy, size = params
            points = [(cx, cy - size), (cx + size, cy), (cx, cy + size), (cx - size, cy)]
            pygame.draw.polygon(screen, grey, points)

    # Отображение имени игрока, уровня, счёта и количества еды
    show_username = font.render(f"Player: {username}", True, black)
    show_level = font.render(f"Level: {level_snake}", True, black)
    show_score = font.render(f"Score: {score_food}", True, black)
    show_foods_eaten = font.render(f"Foods eaten: {foods_eaten}", True, black)

    screen.blit(show_username, (10, 10))
    screen.blit(show_level, (10, 30))
    screen.blit(show_score, (10, 50))
    screen.blit(show_foods_eaten, (10, 70))    

    pygame.display.flip()  
    clock.tick(speed)

# Сохраняем результат в таблицу user_score
cursor.execute("INSERT INTO user_score (user_id, score, level) VALUES (?, ?, ?)", (user_id, score_food, level_snake))
conn.commit()

# Показ последних результатов после окончания игры
show_user_history()

pygame.quit()
conn.close()
sys.exit()
