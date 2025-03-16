import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Ball")

fps = pygame.time.Clock()

move = 20
radius = 30
#red = (255,0,0)

x = 300
y = 300

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y - radius - move >= 0:
            y -= move
    elif keys[pygame.K_DOWN] and y + radius + move <= 600:
            y += move
    elif keys[pygame.K_LEFT] and x - radius - move >= 0:
            x -= move
    elif keys[pygame.K_RIGHT] and x + radius + move <= 600:
            x += move

    screen.fill("White")
    pygame.draw.circle(screen, (255,0,0), (x,y), radius)
        
    pygame.display.update()
    fps.tick(60)