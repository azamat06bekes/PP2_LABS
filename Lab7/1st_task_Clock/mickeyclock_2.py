import pygame
import time

class Mickeyclock:
    def __init__(self, screen):
        self.screen = screen
        self.clock_image = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_practice\Lab7\mickeyclock_hand.jpeg")
        self.clock_image = pygame.transform.scale(self.clock_image, (self.clock_image.get_width() // 3, self.clock_image.get_height() // 3))

        self.mickey_right_hand = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_practice\Lab7\mickey_right_hand.png")
        self.mickey_left_hand = pygame.image.load(r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_practice\Lab7\mickey_left_hand.png")

        self.mickey_right_hand = pygame.transform.scale(self.mickey_right_hand, (self.mickey_right_hand.get_width() // 3, self.mickey_right_hand.get_height() // 3))
        self.mickey_left_hand = pygame.transform.scale(self.mickey_left_hand, (self.mickey_left_hand.get_width() // 3, self.mickey_left_hand.get_height() // 3))

    def blitRotate(self, surf, image, pos, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_rect = rotated_image.get_rect(center=pos)
        surf.blit(rotated_image, rotated_rect)

    def update(self):
        screen_w, screen_h = self.screen.get_size()
        pos = (screen_w // 2, screen_h // 2)

        clock_x = pos[0] - self.clock_image.get_width() // 2
        clock_y = pos[1] - self.clock_image.get_height() // 2
        self.screen.blit(self.clock_image, (clock_x, clock_y))

        current_time = time.localtime()
        seconds = current_time.tm_sec
        minutes = current_time.tm_min

        second_angle = -seconds * 6
        minute_angle = -minutes * 6 - seconds * 0.1

        self.blitRotate(self.screen, self.mickey_right_hand, pos, minute_angle)
        self.blitRotate(self.screen, self.mickey_left_hand, pos, second_angle)
