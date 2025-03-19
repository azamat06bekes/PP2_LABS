import pygame
import sys
from mickeyclock import Mickeyclock

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 51)
green = (0, 255, 0)
red = (255, 0, 0)
sky_blue = (51, 255, 255)


def run():

    pygame.init()

    screen_width = 1280
    screen_height = 665

    screen = pygame.display.set_mode((screen_width, screen_height))
    
    pygame.display.set_caption("Test gaming")

    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()
    
    font = pygame.font.Font(None, 36)

    mickeyclock = Mickeyclock(screen)

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)
        mickeyclock.update()

        elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
        elapsed_seconds = elapsed_time % 60
        elapsed_minutes = (elapsed_time // 60) % 60

        time_text = font.render(f"Time: {elapsed_minutes} min {elapsed_seconds} sec",True, green)
        
        screen.blit(time_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

    sys.exit()

run()
