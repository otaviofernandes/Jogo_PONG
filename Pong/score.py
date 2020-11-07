import pygame

def show_score(result, score1, score2):
    pygame.init()
    window = pygame.display.set_mode([1280,720])
    title = pygame.display.set_caption("PONG - Score Screen")

    # carrega as imagens
    field = pygame.image.load("assets/field.png")
    p1w = pygame.image.load("assets/p1win.png")
    p2w = pygame.image.load("assets/p2win.png")
    score1_img = pygame.image.load("assets/score/" + str(score1) + ".png")
    score2_img = pygame.image.load("assets/score/" + str(score2) + ".png")
    win = pygame.image.load("assets/win.png")
    option = pygame.image.load("assets/option.png")

    def draw_assets(): # desenha as imagens na tela
        window.blit(field, (0, 0))
        if result == 1:
            window.blit(p1w, (0,0))
        else:
            window.blit(p2w, (980,0))

        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))
        window.blit(win, (300, 300))
        window.blit(option, (450, 500))

    loop = True

    while loop:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                loop = False

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            return True
        elif key[pygame.K_x]:
            return False

        draw_assets()
        pygame.display.update()