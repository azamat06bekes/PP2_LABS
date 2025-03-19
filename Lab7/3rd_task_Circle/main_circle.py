import pygame
import sys

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 51)
green = (0, 255, 0)
red = (255, 0, 0)

def run():

    pygame.init()

    screen_width = 500
    screen_height = 500

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Moving ball")

    x = screen_width // 2  
    y = screen_height // 2  
    radius_circle = 25
    step = 20
    
    running = True
    
    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_UP:
                    if(y - radius_circle - step >= 0):
                        y -= step
                elif event.key == pygame.K_DOWN:
                    if y + radius_circle + step <= screen_height:
                        y += step
                elif event.key == pygame.K_LEFT:
                    if x - radius_circle - step >= 0:
                        x -= step
                elif event.key == pygame.K_RIGHT:
                    if x + radius_circle + step <= screen_width:
                        x += step
             


        screen.fill(white)
        
        pygame.draw.circle(screen, red, (x, y), radius_circle)

        pygame.display.flip()

run()
                