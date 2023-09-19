import pygame

from util.QTree import QTree


def _draw(x, y, win):
    pygame.draw.circle(win, (200, 100, 100), (x, y), 5)


def draw_all_particles_in_qtree(qt: QTree, win):
    points = qt.get_points()
    for point in points:
        _draw(point.x, point.y, win)
