import pygame
import os

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Music Player")

music_files = ["music1.mp3", "music2.mp3", "music3.mp3"]
current_music_index = 0

font = pygame.font.SysFont(None, 25)

pygame.mixer.music.load(music_files[current_music_index])
pygame.mixer.music.play()

def play_music():
    pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

def next_music():
    global current_music_index
    current_music_index += 1
    if current_music_index >= len(music_files):
        current_music_index = 0
    pygame.mixer.music.load(music_files[current_music_index])
    pygame.mixer.music.play()

def prev_music():
    global current_music_index
    current_music_index -= 1
    if current_music_index < 0:
        current_music_index = len(music_files) - 1
    pygame.mixer.music.load(music_files[current_music_index])
    pygame.mixer.music.play()

def game_loop():
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if pygame.mixer.music.get_busy():
                        pause_music()
                    else:
                        play_music()
                elif event.key == pygame.K_s:
                    stop_music()
                elif event.key == pygame.K_n:
                    next_music()
                elif event.key == pygame.K_p:
                    prev_music()

        game_display.fill(white)

        text = font.render("Press SPACE to play/pause, S to stop, N for next, P for previous", True, black)
        game_display.blit(text, [0, 0])

        pygame.display.update()

    pygame.quit()
    quit()

game_loop()