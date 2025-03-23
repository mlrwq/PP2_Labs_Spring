import pygame, sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Paint")

canvas = pygame.Surface((800, 600))
canvas.fill((255, 255, 255))

drawing = False
start_pos = (0, 0)
current_tool = 'free' 
color = (0, 0, 0)
eraser_radius = 10

colors = {
    pygame.K_1: (0, 0, 0),
    pygame.K_2: (255, 0, 0),
    pygame.K_3: (0, 255, 0),
    pygame.K_4: (0, 0, 255),
    pygame.K_5: (255, 255, 0),
}

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_tool = 'rect'
            elif event.key == pygame.K_c:
                current_tool = 'circle'
            elif event.key == pygame.K_e:
                current_tool = 'eraser'
            elif event.key == pygame.K_f:
                current_tool = 'free'
            elif event.key in colors:
                color = colors[event.key]

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            if current_tool == 'rect':
                rect = pygame.Rect(min(start_pos[0], end_pos[0]),
                                   min(start_pos[1], end_pos[1]),
                                   abs(end_pos[0]-start_pos[0]),
                                   abs(end_pos[1]-start_pos[1]))
                pygame.draw.rect(canvas, color, rect, 2)

            elif current_tool == 'circle':
                radius_circle = int(((end_pos[0] - start_pos[0])**2 +
                                    (end_pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(canvas, color, start_pos, radius_circle, 2)

        if event.type == pygame.MOUSEMOTION and drawing:
            if current_tool == 'eraser':
                pygame.draw.circle(canvas, (255, 255, 255), event.pos, eraser_radius)
            elif current_tool == 'free':
                pygame.draw.line(canvas, color, last_pos, event.pos, 3)
                last_pos = event.pos


    screen.fill((200, 200, 200))
    screen.blit(canvas, (0, 0))

    font = pygame.font.SysFont(None, 24)
    tool_text = font.render(f'Tool: {current_tool.upper()} | Color: {color}', True, (0, 0, 0))
    screen.blit(tool_text, (10, 600 - 30))

    pygame.display.flip()
    clock.tick(60)
