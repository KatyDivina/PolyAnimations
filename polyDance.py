import pygame
from pygame.locals import *
from random import randint as ri
from time import sleep
from math import sqrt
import classPoly

maindisplay = pygame.display.set_mode((800, 600))


def render_grid():
    points = []
    pointsX = [x for x in range(-50, 900, 30)]
    pointsY = [y for y in range(-20, 680, 10)]

    for y in pointsY:
        points.append([])
        for x in pointsX:
            p = (x + ri(-10, 10), y + ri(-2, 2))
            points[len(points) - 1].append(p)
    return points


def render_poly():
    polyGroup = pygame.sprite.LayeredUpdates()
    for j in range(1, len(points) - 2, 2):

        for i in range(0, len(points[j]) - 3, 2):
            poly1 = classPoly.Poly([points[j][i], points[j - 1][i + 1], points[j][i + 2], points[j + 1][i + 1]])
            polyGroup.add(poly1)

            poly2 = classPoly.Poly([points[j][i + 2], points[j + 1][i + 1], points[j + 2][i + 2], points[j + 1][i + 3]])
            polyGroup.add(poly2)

    return polyGroup

points = render_grid()
polyGroup = render_poly()

end = False
while not end:

    for e in pygame.event.get():
        if e.type == QUIT:
            end = True
        if e.type == MOUSEMOTION:
            mouseOn = polyGroup.get_sprites_at(e.pos)
            for s in mouseOn:
                s.changeColor()

                for n in pygame.sprite.spritecollide(s, polyGroup, False):
                    n.changeColor()

    polyGroup.update(maindisplay)
    pygame.display.update()
pygame.quit()
