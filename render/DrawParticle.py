import pygame
from pygame import gfxdraw


def draw(self, win):
    x = self.x
    y = self.y

    # If we have more than 2 points of a partcile's position we will do the following
    if 150 > len(self.orbit) > 2:
        updated_points = []  # Gets a list of updated points which are the x, y coordinates to scale
        for point in self.orbit:
            x, y = point
            updated_points.append((x, y))

        # Takes a list of points and draws lines between those points and does not eclose them
        # because of False
        pygame.draw.aalines(win, self.color, False, updated_points, 2)

        # Remove line after it is drawn after 10 points
        if len(self.orbit) > 100:
            self.orbit.pop(0)

    # def draw_circle(win, self, x, y, radius, color):
    x = self.x
    y = self.y
    # Draws a circle based on the cordinates of the particle and their radius

    pygame.draw.circle(win, self.color, (x, y), self.radius)

    # Anti Aliasing the circles
    x_int = int(x)
    y_int = int(y)
    self.radius_int = int(self.radius)

    # OverflowError: signed short integer is less than minimum
    # probably comes from the following 2 lines of code and the above three
    # that are required to make the code work
    gfxdraw.aacircle(win, x_int, y_int, self.radius_int, self.color)
    gfxdraw.filled_circle(win, x_int, y_int, self.radius_int, self.color)