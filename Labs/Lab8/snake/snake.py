import pygame
import sys
import random

pygame.init()

def background(screen):
    for i in range((400//20)*20):
        for j in range((600//20)*20):
            if (i + j) % 2 == 0:
                color = (102,255,102)
            else:
                color = (0,255,0)

            pygame.draw.rect(screen, color, (i * 20, j * 20, 20, 20))


shrift = pygame.font.Font(None, 50)
shrift2 = pygame.font.Font(None, 30)
snake_pic = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab8\snake\IMG_0375.PNG")
snake_pic = pygame.transform.scale(snake_pic, (300,400))

game_over_pic = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab8\snake\Game_over.png")
game_over_pic = pygame.transform.scale(game_over_pic, (600,400))

screen = pygame.display.set_mode((600,400))
cell = 20
pygame.display.set_caption("Miras' Snake")

clock = pygame.time.Clock()

walls = [(x, y) for x in range(0, 600, cell) for y in range(0, 400, cell)
         if x == 0 or y == 0 or x == 600 - cell or y == 400 - cell]

snake = [(100,100), (80,100), (60,100)]
snake_dir = (cell, 0)

score = 0
speed = 10 
level = 1

game_active = False

start_text = shrift.render("Press 'Space' to start", True, "White")
start_text_rec = start_text.get_rect(center = (400, 200))


def food():
    cell = 20
    while True:
        x = random.randint(1, (600//cell)-2)*cell
        y = random.randint(1, (400//cell)-2)*cell
        food_pos = (x,y)
        if food_pos not in snake and food_pos not in walls:
            return food_pos
        
apples = food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir != (0, cell):
                    snake_dir = (0, -cell)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -cell):
                    snake_dir = (0, cell)
                elif event.key == pygame.K_LEFT and snake_dir != (cell, 0):
                    snake_dir = (-cell, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-cell, 0):
                    snake_dir = (cell, 0)
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snake = [(100,100), (80,100), (60,100)]
                snake_dir = (cell, 0)

                score = 0
                speed = 10 
                level = 1

                apples = food()

    if game_active:    
        head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        snake.insert(0, head)

        background(screen)

        if head in snake[1:] or head[0] < 0 or head[1] < 0 or head[0] > 600 or head[1] > 400:
            game_active = False

        if head in walls:
            game_active = False

        if head == apples:
            score += 10
            apples = food()
            
            if score % 30 == 0:
                level += 1
                speed += 3
        else:
            snake.pop()


        for i in walls:
            pygame.draw.rect(screen, "Orange", (i[0], i[1], cell, cell))

        for i in snake:
            pygame.draw.rect(screen, (0, 153, 0), (i[0], i[1], cell, cell))

        pygame.draw.rect(screen, "Red", (apples[0], apples[1], cell, cell))

        score_text = shrift.render(f"Score: {score}", True, "White")
        level_text = shrift.render(f"Level {level}", True, "White")
        screen.blit(score_text, (10,10))
        screen.blit(level_text, (450, 10))
    
    else: 
        screen.fill("Black")

        my_score = shrift2.render(f"Your score: {score}", True, "White")
        my_score_rec = my_score.get_rect(center = (300,300))

        if score == 0:
            screen.fill("Green")
            screen.blit(start_text, start_text_rec)
            screen.blit(snake_pic, (0,0))

        else:
            screen.blit(game_over_pic, (0,-20))
            screen.blit(my_score, my_score_rec)
     
    pygame.display.update()
    clock.tick(speed)