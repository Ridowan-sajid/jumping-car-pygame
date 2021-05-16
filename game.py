import math
import random
import pygame

pygame.init()
screen_width=1000
screen_height=500
pygame.display.set_caption("Car Jumping")
screen=pygame.display.set_mode((screen_width,screen_height))
showing_text=False
score=0
score_section=False
down_key_press= False


# Background image
bg_x=0
bg_Y=0
bg_img=pygame.image.load("images/background.jpg")


# my car
right_key_down=False
left_key_down=False
state = "ready"
walk_speed=0.5
human_X=260
human_Y=380
human_img=pygame.image.load("images/car_player.png")

# villain car
villain_X = []
villain_Y = []
villain_car=[]
num_villain=2
for i in range(num_villain):
    villain_X.append(random.randint(screen_width,screen_width+1000))
    villain_Y.append(390)
    villain_car.append(pygame.image.load("images/car.png"))


def isCollision(enemyX,enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + math.pow(enemyY - playerY, 2))
    if distance < 80:
        return True
    else:
        return False


def score_txt():
    font_score = pygame.font.Font("freesansbold.ttf", 30)
    score_text = font_score.render(f'Score: {int(score)}', True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

run=True
while run:
    if score_section:
        pass
    else:
        score += 0.01
    pygame.display.update()
    screen.fill((255, 255, 255))
    screen.blit(bg_img,(bg_x,bg_Y))
    screen.blit(bg_img, (bg_x+screen_width, bg_Y))

    if bg_x == -1000:
        screen.blit(bg_img, (bg_x+screen_width, bg_Y))
        bg_x = 0
    bg_x -= 1
    screen.blit(human_img, (human_X, human_Y))

    for i in range(num_villain):
        if villain_X[i] < -100:
            villain_X[i]=random.randint(screen_width,screen_width+1000)
        screen.blit(villain_car[i],(villain_X[i],villain_Y[i]))
        villain_X[i] -= 1.8
    score_txt()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right_key_down = True
                left_key_down=False
            if event.key == pygame.K_LEFT:
                right_key_down = False
                left_key_down = True
            if event.key == pygame.K_DOWN:
                down_key_press = True
            if event.key == pygame.K_SPACE:
                if state == "ready":
                    state = "fire"
    if down_key_press:
        human_Y = 380
        walk_speed = -0.5
        down_key_press=False
    if right_key_down == True:
        if human_X > 850:
            human_X=850
        human_X += 0.2
    if left_key_down == True:
        if human_X < 40:
            human_X=40
        human_X -= 0.2

    if state == 'fire':
        human_Y -= walk_speed
        walk_speed -= 0.001
        if walk_speed < -0.5:
            state = "ready"
            walk_speed=0.5
    for i in range(num_villain):
        if isCollision(villain_X[i],villain_Y[i],human_X,human_Y):
            showing_text=True
            human_X=20000
            human_Y=-2222
    if showing_text:
        score_section=True
        font = pygame.font.Font("freesansbold.ttf",60)
        ending_text = font.render(f'GAME OVER',True,(0,0,0))
        screen.blit(ending_text,(330,230))
