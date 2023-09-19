import pygame


def render():
    pygame.init()

    width, height = 1000, 1000

    win = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption('A particle simulation')

    run = True
    clock = pygame.time.Clock()

    while run:
        # Limits the game to 60fps
        clock.tick(60)
        win.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        particle.draw(win)

        pygame.display.update()

    pygame.quit()
