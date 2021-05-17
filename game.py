import math
import random
import pygame

pygame.init()
screen_width=1000
screen_height=500
pygame.display.set_caption("Car Jumping")
screen=pygame.display.set_mode((screen_width,screen_height))
showing_text = False
score=0
score_section = False
down_key_press = False

pygame.mixer.music.load("music/Uplifting-and-inspiring-intro-music.mp3")
pygame.mixer.music.play(-1)

# Background image
bg_x = 0
bg_Y = 0
bg_img = pygame.image.load("images/background.jpg")


# my car
right_key_down=False
left_key_down=False
state = "ready"
walk_speed=0.5
player_X=260
player_Y=380
player_img=pygame.image.load("images/car_player.png")

def draw_player_car():
    screen.blit(player_img, (player_X, player_Y))

# villain car
villain_X = []
villain_Y = []
villain_car = []
num_villain = 2

for i in range(num_villain):
    villain_X.append(random.randint(screen_width,screen_width+1000))
    villain_Y.append(390)
    villain_car.append(pygame.image.load("images/car.png"))

def draw_villain(i):
    if villain_X[i] < -100:
        villain_X[i] = random.randint(screen_width, screen_width + 1000)
    screen.blit(villain_car[i], (villain_X[i], villain_Y[i]))
    villain_X[i] -= 1.8



def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + math.pow(enemyY - playerY, 2))
    if distance < 80:
        return True
    else:
        return False


def score_txt():
    font_score = pygame.font.Font("freesansbold.ttf", 30)
    score_text = font_score.render(f'Score: {int(score)}', True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

def end_text():
    font = pygame.font.Font("freesansbold.ttf", 60)
    ending_text = font.render(f'GAME OVER', True, (0, 0, 0))
    screen.blit(ending_text, (330, 230))


def main():
    global score
    global score_section
    global bg_x
    global bg_Y
    global player_X
    global player_Y
    global down_key_press
    global left_key_down
    global right_key_down
    global state
    global showing_text
    global walk_speed

    run = True
    while run:
        if score_section:
            pass
        else:
            score += 0.01
        pygame.display.update()
        screen.fill((255, 255, 255))
        screen.blit(bg_img, (bg_x, bg_Y))
        screen.blit(bg_img, (bg_x + screen_width, bg_Y))

        if bg_x == -1000:
            screen.blit(bg_img, (bg_x + screen_width, bg_Y))
            bg_x = 0
        bg_x -= 1
        draw_player_car()

        for i in range(num_villain):
            draw_villain(i)
        score_txt()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right_key_down = True
                    left_key_down = False
                if event.key == pygame.K_LEFT:
                    right_key_down = False
                    left_key_down = True
                if event.key == pygame.K_DOWN:
                    down_key_press = True
                if event.key == pygame.K_SPACE:
                    if state == "ready":
                        state = "fire"
        if down_key_press:
            player_Y = 380
            walk_speed = -0.5
            down_key_press = False

        if right_key_down == True:
            if player_X > 850:
                player_X = 850
            player_X += 0.2

        if left_key_down == True:
            if player_X < 40:
                player_X = 40
            player_X -= 0.2

        if state == 'fire':
            player_Y -= walk_speed
            walk_speed -= 0.001
            if walk_speed < -0.5:
                state = "ready"
                walk_speed = 0.5

        for i in range(num_villain):
            if isCollision(villain_X[i], villain_Y[i], player_X, player_Y):
                showing_text = True
                player_X = 20000
                player_Y = -2222
        if showing_text:
            score_section = True
            pygame.mixer.music.stop()
            end_text()

if __name__ == '__main__':
    main()