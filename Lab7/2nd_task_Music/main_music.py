import pygame
import sys
import os

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 51)
green = (0, 255, 0)
red = (255, 0, 0)

def run():

    pygame.init()

    screen_width = 700
    screen_height = 500

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Music player")

    playlist = [
        r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_practice\Lab7\mecano.mp3",
        r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_practice\Lab7\Stairway_to_Heaven.mp3",
        r"C:\Users\админ\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\PP2_practice\Lab7\Royalty_Egzod.mp3"
    ]
    cur_song = 0
    def play_song(index):
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()

    font = pygame.font.Font(None, 18)
    
    is_paused = True
    running = True
    
    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
                
            
            if event.type == pygame.KEYUP:
                print(f'Pressed the keyword: {pygame.key.name(event.key)}')
                if event.key == pygame.K_p:
                    if is_paused:
                        pygame.mixer.music.pause()
                        is_paused = False
                    else:  
                        pygame.mixer.music.unpause()
                        is_paused = not is_paused
                        

                elif event.key == pygame.K_s:
                    pygame.mixer.music.stop()

                elif event.key == pygame.K_n:
                    cur_song = (cur_song + 1) % len(playlist)
                    play_song(cur_song)

                elif event.key == pygame.K_b:
                    cur_song = (cur_song - 1) % len(playlist)
                    play_song(cur_song)

        
        screen.fill(white)
        
        cur_song_name = os.path.basename(playlist[cur_song])
        cur_song_name_without_mp3 = os.path.splitext(cur_song_name)[0]
        song_name = font.render(f"Playing: {cur_song_name_without_mp3}", True, black)
        screen.blit(song_name, (10, 20))

        pygame.display.flip()

run()
                