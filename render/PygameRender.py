import pygame
from render.DrawParticle import draw_all_particles_in_qtree
from util.QTree import QTree


def render(qt: QTree):

    pygame.init()

    width = QTree.get_width(qt)
    height = QTree.get_height(qt)

    win = pygame.display.set_mode((width, height))
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

        draw_all_particles_in_qtree(qt, win)

        pygame.display.update()

    pygame.quit()
