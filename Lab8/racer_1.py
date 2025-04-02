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
 
# Параметры экрана и другие переменные
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
CELL_SIZE = 30
SCORE_COIN = 0

# Настройка шрифтов
font_g = pygame.font.SysFont("Times New Roman", 60)
font_small = pygame.font.SysFont("Times New Roman", 20)
game_over = font_g.render("Game Over!", True, BLACK)


# Загрузка фона
background = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_practice\Lec8\AnimatedStreet.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Создание окна
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption('The Racer')
DISPLAYSURF.blit(background, (0, 0))

# Класс врага (машины, которая движется вниз)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_practice\Lec8\Enemy.png")
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
        self.image = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_practice\Lec8\gold_coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # Изменяем размер монеты
        self.rect = self.image.get_rect()
        self.speed = SPEED
        self.respawn()  # Спавним монету в случайном месте

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        for _ in range(10): # 10 попыток найти безопасное место
            new_x = random.randint(40, SCREEN_WIDTH - 40)
            new_y = random.randint(-100, 0)
            self.rect.topleft = (new_x, new_y)

            if not any(enemy.rect.colliderect(self.rect) for enemy in enemies):
                return
        self.rect.topleft = (50, -50)  # Если за 10 попыток не нашли место

# Класс игрока (машины, которой управляет пользователь)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_practice\Lec8\Player.png")
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
        SCORE_COIN += 1
        M1.respawn()

    # # Увеличение скорости каждые 20 монет
    current_speed_level = SCORE_COIN // 20
    if current_speed_level > previous_speed_level:
        SPEED += 0.5
        previous_speed_level = current_speed_level  # Обновляем переменную

    # Отображение очков
    coin_score = font_small.render(f"Coins: {SCORE_COIN}", True, BLACK)
    DISPLAYSURF.blit(coin_score, (SCREEN_WIDTH - 130, 20))

    # Проверка столкновения игрока с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(game_over, (40,210))
        total_scores = font_small.render(f"Total coins: {SCORE_COIN}", True, BLACK)
        DISPLAYSURF.blit(total_scores, ((SCREEN_WIDTH/2 - 65),280))
        pygame.display.update()
        time.sleep(1.5)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(FPS)
