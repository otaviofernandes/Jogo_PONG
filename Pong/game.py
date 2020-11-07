import pygame
from time import sleep


def game():
    pygame.init()
    window = pygame.display.set_mode([1280,720])
    title = pygame.display.set_caption("PONG - Game Screeen")

    score1 = 0
    score2 = 0
    clock = pygame.time.Clock()

    # carrega as imagens
    field = pygame.image.load("assets/field.png")
    player1 = pygame.image.load("assets/player1.png")
    player2 = pygame.image.load("assets/player2.png")
    ball = pygame.image.load("assets/ball.png")
    score1_img = pygame.image.load("assets/score/0.png")
    score2_img = pygame.image.load("assets/score/0.png")
    cmdp1 = pygame.image.load("assets/cmdp1.png")
    cmdp2 = pygame.image.load("assets/cmdp2.png")
    count1 = pygame.image.load("assets/1.png")
    count2 = pygame.image.load("assets/2.png")
    count3 = pygame.image.load("assets/3.png")
    countgo = pygame.image.load("assets/go.png")

    def reg_count():
        draw_assets()
        pygame.mixer.music.load("sounds/beep.mp3")
        pygame.mixer.music.play()
        window.blit(count3, (610, 450))
        pygame.display.update()
        sleep(1)
        draw_assets()
        window.blit(count2, (610, 450))
        pygame.display.update()
        sleep(1)
        draw_assets()
        window.blit(count1, (610, 450))
        pygame.display.update()
        sleep(1)
        draw_assets()
        window.blit(countgo, (580, 450))
        pygame.display.update()
        sleep(1)

    #variáveis de movimentação dos assets
    ball_x = 617
    ball_y = 337
    ball_dir_x = -15
    ball_dir_y = 5

    player1_y = 290
    player2_y = 290


    def move_ball():
        global ball_x
        global ball_y

    def draw_assets(): # desenha as imagens na tela
        window.blit(field, (0, 0))
        window.blit(player1, (10, player1_y))
        window.blit(player2, (1237, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))
        window.blit(cmdp1, (0,20))
        window.blit(cmdp2, (1110, 20))

    reg_count()

    loop = True

    while loop:
        clock.tick(60)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                loop = False

        key = pygame.key.get_pressed()
        if key[pygame.K_w] and player1_y >= 10:
            player1_y -= 10
        if key[pygame.K_s] and player1_y <= 564:
            player1_y += 10
        if key[pygame.K_UP] and player2_y >= 10:
            player2_y -= 10
        if key[pygame.K_DOWN] and player2_y <= 564:
            player2_y += 10

        #---Tratamento de Colisão

        if ball_x < 40:
            if player1_y < ball_y + 23:
                if player1_y + 146 > ball_y:
                    ball_dir_x *= -1
                    pygame.mixer.music.load("sounds/ball.mp3")
                    pygame.mixer.music.play()

        if ball_x > 1230:
            if player2_y < ball_y + 23:
                if player2_y + 146 > ball_y:
                    ball_dir_x *= -1
                    pygame.mixer.music.load("sounds/ball.mp3")
                    pygame.mixer.music.play()
        
        if ball_y < 10 or ball_y > 685:
            ball_dir_y *= -1
            pygame.mixer.music.load("sounds/ball.mp3")
            pygame.mixer.music.play()

        #---Reiniciando a posição da bolinha
        if ball_x <= 0:
            pygame.mixer.music.load("sounds/goal.mp3")
            pygame.mixer.music.play()
            sleep(2.5)
            ball_x = 617
            ball_y = 337
            ball_dir_x *= -1
            ball_dir_y *= -1
            score2 += 1
            score2_img = pygame.image.load("assets/score/" + str(score2) + ".png")
            if score2 == 5:
                return 2,  score1, score2
            else:
                player1_y = 290
                player2_y = 290
                reg_count()

        elif ball_x >= 1247:
            pygame.mixer.music.load("sounds/goal.mp3")
            pygame.mixer.music.play()
            sleep(2.5)
            ball_x = 617
            ball_y = 337
            ball_dir_x *= -1
            ball_dir_y *= -1
            score1 += 1
            score1_img = pygame.image.load("assets/score/" + str(score1) + ".png")
            if score1 == 5:
                return 1, score1, score2
            else:
                player1_y = 290
                player2_y = 290
                reg_count()


        draw_assets()
        ball_x += ball_dir_x
        ball_y += ball_dir_y
        pygame.display.update()