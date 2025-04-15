import pygame
import sys
import random
import time
import psycopg2
from config import load_config


def get_user():
    username = input("Enter player name: ")
    config = load_config()
    conn = psycopg2.connect(**config)
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if not user:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        print(f"new user {username} created.")
        return conn, user_id, 0, 1
    else:
        user_id = user[0]
        cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
        data = cur.fetchone()
        if data:
            print(f"welcome back, {username}! level: {data[1]} | score: {data[0]}")
            return conn, user_id, data[0], data[1]
        else:
            return conn, user_id, 0, 1


conn, user_id, score, level = get_user()


def save_state(conn, user_id, score, level):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO user_score (user_id, score, level)
            VALUES (%s, %s, %s)
        """, (user_id, score, level))
        conn.commit()
        print("Saved")


pygame.init()

#виды еды
food_types = [
    {"color": "Red", "weight": 10, "duration": 10},
    {"color": "Yellow", "weight": 20, "duration": 5}, 
    {"color": "Blue", "weight": 30, "duration": 3}  
]

#функция для фона
def background(screen):
    for i in range((400//20)*20):
        for j in range((600//20)*20):
            if (i + j) % 2 == 0:
                color = (102,255,102)
            else:
                color = (0,255,0)

            pygame.draw.rect(screen, color, (i * 20, j * 20, 20, 20))

#все нужные переменные
shrift = pygame.font.Font(None, 50)
shrift2 = pygame.font.Font(None, 30)
snake_pic = pygame.image.load(r"C:\pp2labsss\Labs\Lab9\snake2\IMG_0375.PNG")
snake_pic = pygame.transform.scale(snake_pic, (300,400))

game_over_pic = pygame.image.load(r"C:\pp2labsss\Labs\Lab9\snake2\Game_over.png")
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
prev_score = score

#статус игры 
game_active = False
paused = False

start_text = shrift.render("Press 'Space' to start", True, "White")
start_text_rec = start_text.get_rect(center = (400, 200))

#позиция еды
def food():
    cell = 20
    while True:
        x = random.randint(1, (600//cell)-2)*cell
        y = random.randint(1, (400//cell)-2)*cell
        food_pos = (x,y)
        if food_pos not in snake and food_pos not in walls:
            return food_pos

cur_food = {}        

#появление рандомной еды
def different_food():
    global cur_food
    food_pos = food()
    choice = random.choices(food_types, weights = [0.6,0.3,0.1], k=1)[0]

    cur_food = {
        "position" : food_pos,
        "color" : choice["color"],
        "weight" : choice["weight"],
        "spawn" : time.time(),
        "duration" : choice["duration"]
    }

#таймер еды (когда она пропадет)
def food_timer():
    global cur_food
    if time.time() - cur_food["spawn"] > cur_food["duration"]:
        different_food()


def generate_walls(level):
    walls = []
    if level >= 1:
        walls += [(x, 0) for x in range(0, 600, cell)]
        walls += [(x, 380) for x in range(0, 600, cell)]
    if level >= 2:
        walls += [(0, y) for y in range(0, 400, cell)]
        walls += [(580, y) for y in range(0, 400, cell)]
    if level >= 3:
        for x in range(200, 400, cell):
            walls.append((x, 200))
    return walls



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        
        #направления змейки
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

                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_state(conn, user_id, score, level)
                    
        
        #начать игру с помощью пробела
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snake = [(100,100), (80,100), (60,100)]
                snake_dir = (cell, 0)

                score = 0
                speed = 10 
                level = 1
                prev_score = 0

                different_food()

    if paused:
        pygame.display.update()
        clock.tick(5)
        continue

    #игры когда активна
    if game_active:    
        head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        snake.insert(0, head)

        walls = generate_walls(level)

        background(screen)

        #проверки столкновений змеи с самой собой и о стену
        if head in snake[1:] or head[0] < 0 or head[1] < 0 or head[0] > 600 or head[1] > 400:
            save_state(conn, user_id, score, level)
            print("Game over, progress saved")

            game_active = False

        if head in walls:
            save_state(conn, user_id, score, level)
            print("Game over, progress saved")

            game_active = False

        #отсчет таймера 
        food_timer()

        #очки за еду при коллизии змеи с едой (+ускорение и уровень)
        if head == cur_food["position"]:
            score += cur_food["weight"]
            different_food()
            
            if (score // 30) > (prev_score // 30):
                level += 1
                speed += 3
            prev_score = score
        else:
            snake.pop()

        #цикл для рисовки стен
        for i in walls:
            pygame.draw.rect(screen, "Orange", (i[0], i[1], cell, cell))
        
        #цикл для рисовки змеи
        for i in snake:
            pygame.draw.rect(screen, (0, 153, 0), (i[0], i[1], cell, cell))

        #рисовка еды
        pygame.draw.rect(screen, cur_food["color"], (cur_food["position"][0], cur_food["position"][1], cell, cell))

        score_text = shrift.render(f"Score: {score}", True, "White")
        level_text = shrift.render(f"Level {level}", True, "White")
        screen.blit(score_text, (10,10))
        screen.blit(level_text, (450, 10))
    
    #проигрыш
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