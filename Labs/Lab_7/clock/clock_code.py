import pygame 
import sys
import time

pygame.init()

screen = pygame.display.set_mode((850,700))
pygame.display.set_caption("Mickey Clock")

mickey_clock = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab_7\clock\clock (1).png")
mickey_right_hand = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab_7\clock\min_hand (1).png")
mickey_left_hand = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab_7\clock\sec_hand (1).png")

mickey_clock = pygame.transform.scale(mickey_clock, (850,700))

fps = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(mickey_clock, (0,0))
    now = time.localtime()

    minutes = now.tm_min
    seconds = now.tm_sec
    sec_angle = -seconds * 6
    min_angle = -minutes * 6 - seconds * 0.1 

    sec_rotate = pygame.transform.rotate(mickey_left_hand, sec_angle)
    sec_rect = sec_rotate.get_rect(center=(425, 350))
    screen.blit(sec_rotate, sec_rect.topleft)

    min_rotate = pygame.transform.rotate(mickey_right_hand, min_angle)
    min_rect = min_rotate.get_rect(center=(425, 350))
    screen.blit(min_rotate, min_rect.topleft)

    pygame.display.update()
    fps.tick(60)