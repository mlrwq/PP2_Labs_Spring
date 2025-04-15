import pygame
import sys
import random 

pygame.init()

#очки за каждую секунду времени от начала игры
def scores():
    cur_time = (pygame.time.get_ticks()//1000) - start_time
    score_surf = shrift.render(f"Score: {cur_time}", True, "Black")
    score_rect = score_surf.get_rect(center = (80,30))
    screen.blit(score_surf, score_rect)
    return cur_time

#появление монет
def spawn_coin():
    global coin, coin_rect, cur_coin
    cur_coin = random.choice(coin_types)
    coin = cur_coin["image"]
    coin_rect = coin.get_rect(center = (random.randint(100,400), random.randint(-500, -100)))
    while coin_rect.colliderect(cars_rect):
        coin_rect.x = random.randint(100,400)

#все нужные переменные 
clock = pygame.time.Clock()
shrift = pygame.font.Font(None, 40)
shrift2 = pygame.font.Font(None, 30)

screen = pygame.display.set_mode((510,770))
pygame.display.set_caption("Miras' racer")

track = pygame.image.load(r"C:\pp2labsss\Labs\Lab9\racer2\track.jpg")
my_car = pygame.image.load(r"C:\pp2labsss\Labs\Lab9\racer2\IMG_0378.PNG")
cars = pygame.image.load(r"C:\pp2labsss\Labs\Lab9\racer2\IMG_0379.PNG")
start = pygame.image.load(r"C:\pp2labsss\Labs\Lab9\racer2\511208690d60b1b09601d43cd868c273.jpg")
game_over = pygame.image.load(r"C:\pp2labsss\Labs\Lab9\racer2\maxresdefault.jpg")

gold_coin = pygame.image.load(r"C:\pp2labsss\Labs\Lab9\racer2\gold_coin.PNG")
silver_coin = pygame.image.load(r"C:\pp2labsss\Labs\Lab9\racer2\silver_coin.PNG")
bronze_coin = pygame.image.load(r"C:\pp2labsss\Labs\Lab9\racer2\bronze_coin.PNG")

gold_coin = pygame.transform.scale(gold_coin, (50,50))
silver_coin = pygame.transform.scale(silver_coin, (50,50))
bronze_coin = pygame.transform.scale(bronze_coin, (50,50))

#типы монет
coin_types = [
    {"image" : gold_coin, "weight" : 3},
    {"image" : silver_coin, "weight" : 2},
    {"image" : bronze_coin, "weight" : 1}
]
cur_coin = random.choice(coin_types)
coin = cur_coin["image"]
coin_rect = coin.get_rect(center = (random.randint(100, 400), -100))


my_car = pygame.transform.scale(my_car, (100,180))
my_car_rect = my_car.get_rect(midbottom = (255,750))
cars = pygame.transform.scale(cars, (100,180))
cars_rect = cars.get_rect(midtop = (random.randint(100,400), -100))
start = pygame.transform.scale(start, (510,770))
game_over = pygame.transform.scale(game_over, (600,400))

cars_speed = 5
speed = 5
score = 0
start_time = 0
coin_count = 0
total_coins = 0

start_text = shrift.render("Press Space to start", True, "White")
start_text_rect = start_text.get_rect(center = (260,385))

#статус игры 
game_active = False
increase = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #начало игры при нажатии пробела
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()//1000
                coin_count = 0
                cars_speed = 5
                increase = 0
                total_coins = 0

    #когда игра активна 
    if game_active:
        #направления нашей машины
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and my_car_rect.left > 10:
            my_car_rect.x -= speed
        elif keys[pygame.K_RIGHT] and my_car_rect.right < 500:
            my_car_rect.x += speed

        #движение вражеской машины
        cars_rect.y += cars_speed 
        if cars_rect.y > 850:
            cars_rect.y = -200
            cars_rect.x = random.randint(100, 400)

        #движение монеты
        coin_rect.y += speed
        if coin_rect.y > 850:
            spawn_coin()

        #если вражеская машина пересекаетсяя с монетой
        if coin_rect.colliderect(cars_rect):
            spawn_coin()
        
        #если наша машина врезается во вражескую машину 
        if my_car_rect.colliderect(cars_rect): 
            cars_rect.midtop = (random.randint(100,400), -100)
            coin_rect.y = -100
            coin_rect.x = random.randint(100,400)

            coin_count -= 5
            if coin_count < 0:
                game_active = False

        #наша машина когда сталкивается с монетой
        if my_car_rect.colliderect(coin_rect):
            total_coins += 1
            coin_count += cur_coin["weight"]
            spawn_coin()

        total_coins_surf = shrift.render(f"Total coins: {total_coins}", True, "Black")
        total_coins_surf_rect = total_coins_surf.get_rect(center = (250, 30))

        coin_surf = shrift.render(f"Coins: {coin_count}", True, "Black")
        coin_surf_rect = coin_surf.get_rect(center = (430,30))

    #выведение всех переменных на экран когда игра активна
    if game_active:
        screen.blit(track, (0,0))
        screen.blit(my_car, my_car_rect)
        screen.blit(cars, cars_rect)
        screen.blit(coin, coin_rect)

        score = scores()
        screen.blit(coin_surf,coin_surf_rect)
        screen.blit(total_coins_surf,total_coins_surf_rect)
        
        if total_coins % 3 == 0 and total_coins != increase:
            cars_speed += 1
            increase = total_coins

    #проигрыщ
    else:
        screen.blit(start, (0,0))

        my_total_coins = shrift2.render(f"Total coins: {total_coins}", True, "White")
        my_total_coins_rect = my_total_coins.get_rect(center = (255, 500))

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
            screen.blit(my_total_coins,my_total_coins_rect)
        

    pygame.display.update()
    clock.tick(60)
