import pygame
import sys
import random 

pygame.init()

def scores():
    cur_time = (pygame.time.get_ticks()//1000) - start_time
    score_surf = shrift.render(f"Score: {cur_time}", True, "Black")
    score_rect = score_surf.get_rect(center = (80,30))
    screen.blit(score_surf, score_rect)
    return cur_time

def spawn_coin():
    coin_rect.x, coin_rect.y = random.randint(100,400), random.randint(-500, -100)
    while coin_rect.colliderect(cars_rect):
        coin_rect.x = random.randint(100,400)

clock = pygame.time.Clock()
shrift = pygame.font.Font(None, 50)
shrift2 = pygame.font.Font(None, 30)

screen = pygame.display.set_mode((510,770))
pygame.display.set_caption("Miras' racer")

track = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab8\car\track.jpg")
my_car = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab8\car\IMG_0378.PNG")
cars = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab8\car\IMG_0379.PNG")
coin = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab8\car\IMG_0381.PNG")
start = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab8\car\511208690d60b1b09601d43cd868c273.jpg")
game_over = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\githowto\repositories\Labs\Lab8\car\maxresdefault.jpg")

my_car = pygame.transform.scale(my_car, (100,180))
my_car_rect = my_car.get_rect(midbottom = (255,750))
cars = pygame.transform.scale(cars, (100,180))
cars_rect = cars.get_rect(midtop = (random.randint(100,400), -100))
coin = pygame.transform.scale(coin, (50,50))
coin_rect = coin.get_rect(center = (random.randint(100,400), -100))
start = pygame.transform.scale(start, (510,770))
game_over = pygame.transform.scale(game_over, (600,400))

cars_speed = 5
speed = 5
score = 0
start_time = 0
coin_count = 0

start_text = shrift.render("Press Space to start", True, "White")
start_text_rect = start_text.get_rect(center = (260,385))

game_active = False
increase = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()//1000
                coin_count = 0
                cars_speed = 5
                increase = 0

    if game_active:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and my_car_rect.left > 10:
            my_car_rect.x -= speed
        elif keys[pygame.K_RIGHT] and my_car_rect.right < 500:
            my_car_rect.x += speed

        cars_rect.y += cars_speed 
        if cars_rect.y > 850:
            cars_rect.y = -200
            cars_rect.x = random.randint(100, 400)

        coin_rect.y += speed
        if coin_rect.y > 850:
            spawn_coin()

        if coin_rect.colliderect(cars_rect):
            spawn_coin()
        
        if my_car_rect.colliderect(cars_rect):
            game_active = False 
            my_car_rect.midbottom = (255, 750)
            cars_rect.midtop = (random.randint(100,400), -100)
            coin_rect.y = -100
            coin_rect.x = random.randint(100,400) 

        if my_car_rect.colliderect(coin_rect):
            coin_count += 1
            spawn_coin()

        coin_surf = shrift.render(f"Coins: {coin_count}", True, "Black")
        coin_surf_rect = coin_surf.get_rect(center = (400,30))

    if game_active:
        screen.blit(track, (0,0))
        screen.blit(my_car, my_car_rect)
        screen.blit(cars, cars_rect)
        screen.blit(coin, coin_rect)

        score = scores()
        screen.blit(coin_surf,coin_surf_rect)
        
        if coin_count % 3 == 0 and coin_count != increase:
            cars_speed += 1
            increase = coin_count

    else:
        screen.blit(start, (0,0))

        my_coins = shrift2.render(f"Coins: {coin_count}", True, "White")
        my_coins_rect = my_coins.get_rect(center = (255, 450))

        my_score = shrift2.render(f"Your score: {score}", True, "White")
        my_score_rect = my_score.get_rect(center = (255,470))

        if score == 0:
            screen.blit(start_text, start_text_rect)
        else:
            screen.fill("Black")
            screen.blit(game_over, (-40,150))
            screen.blit(my_score, my_score_rect)
            screen.blit(my_coins, my_coins_rect)
        
    pygame.display.update()
    clock.tick(60)
