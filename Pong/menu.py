import pygame

def show_menu():
    pygame.init()
    window = pygame.display.set_mode([1280,720])
    title = pygame.display.set_caption("PONG - Menu Screen")

    # carrega as imagens
    field = pygame.image.load("assets/field.png")
    pong = pygame.image.load("assets/pong.png")
    option = pygame.image.load("assets/option.png")

    def draw_assets(): # desenha as imagens na tela
        window.blit(field, (0, 0))
        window.blit(pong, (300, 50))
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