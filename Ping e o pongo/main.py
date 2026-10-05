import pygame
pygame.init()

windows = pygame.display.set_mode((1280, 720))


title = pygame.display.set_caption("futeboll pong")
field = pygame.image.load("assets/field.png")

#vitoria

win = pygame.image.load("assets/win.png")

#placar

score1 = 0
score1_img = pygame.image.load("assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("assets/score/0.png")


player1 = pygame.image.load("assets/player1.png")
player1_y = 310
player1_x = 50
player1_moveup_y = False
player1_movedown_y = False
player1_moveup_x = False
player1_movedown_x = False


player2 = pygame.image.load("assets/player2.png")
player2_y = 310
player2_x = 1150
player2_moveup_y = False
player2_movedown_y = False
player2_moveup_x = False
player2_movedown_x = False


ball = pygame.image.load("assets/ball.png")
ball_x = 620
ball_y = 340
ball_dir = -3
ball_dir_y = 2
#ball_dir_x =

#ball_colision


def move_player():
    global player1_y
    global player1_x
    global player2_y
    global player2_x

    if player1_moveup_y:
        player1_y -= 5
    else:
        player1_y += 0

    if player1_movedown_y:
        player1_y += 5
    else:
        player1_y += 0

    if player1_moveup_x:
        player1_x -= 5
    else:
        player1_x += 0
    if player1_movedown_x:
        player1_x += 5
    else:
        player1_x += 0

    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575
    if player1_x <= 0:
        player1_x = 0
    elif player1_x >= 555:
        player1_x = 555

#player2 vai perseguir a bolinha respeitando o mapa
def move_player2():
    global player2_y
    player2_y = ball_y
    if player2_y <= 0:
        player2_y = 0
    elif player2_y >= 575:
        player2_y = 575



def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global score1
    global score1_img
    global score2
    global score2_img

    ball_x += ball_dir
    ball_y += ball_dir_y

    # Player 1
    if (player1_x < ball_x + 23 and
            player1_x + 78 > ball_x and
            player1_y < ball_y + 23 and
            player1_y + 146 > ball_y):

        ball_dir *= -1
        ball_x = player1_x + 78

    # Player 2
    if (player2_x < ball_x + 23 and
            player2_x + 78 > ball_x and
            player2_y < ball_y + 23 and
            player2_y + 146 > ball_y):

        ball_dir *= -1
        ball_x = player2_x - 23

    # Teto e chão
    if ball_y > 690:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1

#reiniciar a bolinha
    if ball_x <= -50:
        ball_x = 620
        ball_y = 340
        ball_dir_y *= -2
        ball_dir *= 2
        score2 += 1
        score2_img = pygame.image.load("assets/score/" + str(score2) + ".png")
    elif ball_x >= 1320:
        ball_x = 620
        ball_y = 340
        ball_dir_y *= -2
        ball_dir *= 2
        score1 += 1
        score1_img = pygame.image.load("assets/score/" + str(score1) + ".png")





def draw():
    if score1 or score2 < 9:
        windows.blit(field, (0, 0))
        windows.blit(player1, (player1_x, player1_y))
        windows.blit(player2, (player2_x, player2_y))
        windows.blit(ball, (ball_x, ball_y))
        windows.blit(score1_img, (500, 50))
        windows.blit(score2_img, (710, 50))
        move_ball()
        move_player()
        move_player2()
    else:
        windows.blit(win, (300, 330))



loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_moveup_y = True
            if events.key == pygame.K_s:
                player1_movedown_y = True
            if events.key == pygame.K_d:
                player1_movedown_x = True
            if events.key == pygame.K_a:
                player1_moveup_x = True

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup_y = False
            if events.key == pygame.K_s:
                player1_movedown_y = False
            if events.key == pygame.K_d:
                player1_movedown_x = False
            if events.key == pygame.K_a:
                player1_moveup_x = False





    draw()
    pygame.display.update()



