import pygame
import sys
import os

pygame.init()


screen = pygame.display.set_mode((500,800))
pygame.display.set_caption("Miras' Player")

bg1 = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab7\player\IMG_0176.JPEG")
bg2 = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab7\player\IMG_0177 (1).JPEG")

bg1 = pygame.transform.scale(bg1, (500,800))
bg2 = pygame.transform.scale(bg2, (500,800))

playlist = r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab7\player\playlist"
music = os.listdir(playlist)

cover_folder = r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab7\player\cov"
covers = os.listdir(cover_folder)

oblozhki = [pygame.transform.scale(pygame.image.load(os.path.join(cover_folder, cover)), (360,370)) for cover in covers]

cur_track = 0

next_track = pygame.USEREVENT + 1

def play(ind):
    pygame.mixer.music.load(os.path.join(playlist, music[ind]))
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(next_track)

pause = False


while True:
    if pause:
        screen.blit(bg1, (0,0))

    else:
        screen.blit(bg2, (0,0))

    if cur_track < len(oblozhki):
        cur_cov = oblozhki[cur_track]

    else:
        oblozhki[0]

    screen.blit(cur_cov, (70,55))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    pause = True

                else:
                    pygame.mixer.music.unpause()
                    pause = False

            elif event.key == pygame.K_RIGHT:
                cur_track = (cur_track + 1) % len(music)
                play(cur_track)
                pause = False

            elif event.key == pygame.K_LEFT:
                cur_track = (cur_track - 1) % len(music)
                play(cur_track)
                pause = False

        elif event.type == next_track:
            cur_track = (cur_track + 1) % len(music)    
            play(cur_track)