import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Создание цветов
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (102, 255, 255)
 
# Параметры экрана и другие переменные
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
CELL_SIZE = 40
SCORE_COIN = 0

# Настройка шрифтов
font = pygame.font.SysFont("Times New Roman", 60)
font_small = pygame.font.SysFont("Times New Roman", 20)
game_over = font.render("Game Over!", True, BLACK)

# Загрузка фона
background = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\Lab9\AnimatedStreet.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Изображения монет
gold_coin = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\Lab9\gold_coin.png")
gold_coin = pygame.transform.scale(gold_coin, (CELL_SIZE, CELL_SIZE))

red_coin = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\Lab9\red_coin.png")
red_coin = pygame.transform.scale(red_coin, (CELL_SIZE, CELL_SIZE))

green_coin = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\Lab9\green_coin.png")
green_coin = pygame.transform.scale(green_coin, (CELL_SIZE, CELL_SIZE))

# Список монет и их стоимость
coins = [
    {"image": gold_coin, "score": 1},
    {"image": red_coin, "score": 4},
    {"image": green_coin, "score": 8}
]

# Создание окна
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption('The Racer')
DISPLAYSURF.blit(background, (0, 0))

# Класс врага (машины, которая движется вниз)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\Lab9\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:   # Когда враг выходит за пределы экрана, 
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.coin_data = random.choice(coins)  # Выбираем случайную монету
        self.image = self.coin_data["image"]
        self.rect = self.image.get_rect()
        self.speed = SPEED    # Скорость падения монеты
        self.enemies = enemies  # Сохраняем ссылку на группу врагов
        self.respawn()  # Устанавливаем начальную позицию
    
    def move(self):
        self.rect.move_ip(0, self.speed)  # Двигаем монету вниз
        if self.rect.top > SCREEN_HEIGHT:  # Если выходит за экран — создадим новую
            self.respawn()

    def respawn(self):
        self.coin_data = random.choice(coins)  # Выбираем новую случайную монету
        self.image = self.coin_data["image"]
        
        # 10 попыток найти безопасное место
        for _ in range(10):
            new_x = random.randint(40, SCREEN_WIDTH - 40)
            new_y = random.randint(-100, 0)  # Спавним выше экрана
            self.rect.topleft = (new_x, new_y)

            if not any(enemy.rect.colliderect(self.rect) for enemy in enemies):
                return
     
        # Если за 10 попыток не нашлось места, спавним в безопасной зоне
        self.rect.topleft = (50, -50)

# Класс игрока (машины, которой управляет пользователь)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_AZA_Prog\Lab9\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)



# Создание объектов и группы спрайтов
P1 = Player()
E1 = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E1)
M1 = Coin()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(M1)

# Предыдущий_уровень_скорости
global previous_speed_level
previous_speed_level = SCORE_COIN // 20 
speed_level = 0
# Игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    # Перемещение и перерисовка всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    

    # Проверка сбора монеты
    if P1.rect.colliderect(M1.rect):
        SCORE_COIN += M1.coin_data["score"]
        M1.respawn()
    

    # # Увеличение скорости на 0.5 каждые 10 монет
    current_speed_level = SCORE_COIN // 10
    Speed_level = 0
    if current_speed_level > previous_speed_level:
        speed_level += 1
        SPEED += 0.5
        previous_speed_level = current_speed_level  # Обновляем переменную

    # Отображение очков и уровень скорости
    coin_score = font_small.render(f"Coins: {SCORE_COIN}", True, BLACK)
    DISPLAYSURF.blit(coin_score, (SCREEN_WIDTH - 130, 20))
    speed_lvl = font_small.render(f"Speed level: {speed_level}", True, BLACK)
    DISPLAYSURF.blit(speed_lvl, (10, 20))

    # Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(LIGHT_BLUE)
        DISPLAYSURF.blit(game_over, (40,210))
        total_scores = font_small.render(f"Total coins: {SCORE_COIN}", True, BLACK)
        DISPLAYSURF.blit(total_scores, ((SCREEN_WIDTH/2 - 65),280))
        total_levels = font_small.render(f"Overall speed level: {speed_level}", True, BLACK)
        DISPLAYSURF.blit(total_levels, ((SCREEN_WIDTH/2 - 95),300))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(FPS)
