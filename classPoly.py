import pygame
from pygame.locals import *
from random import randint as ri


polySurf = pygame.Surface((800, 600))

class Poly(pygame.sprite.Sprite):
    def __init__(self, poly):
        pygame.sprite.Sprite.__init__(self)
        self.poly = poly
        self.active = False
        self.rect = pygame.draw.polygon(polySurf, (0,0,0), self.poly)
        self.kr = (800-self.rect.centery)/255

        self.set_color()

    def update(self, display):
        #print(self.color)
        self.rect = pygame.draw.polygon(display, self.color, self.poly)


    def dist(self):
        dx = self.rect.centerx
        dy = 0

    def set_color(self):
        r = 25  + (900-self.rect.centery)//5.82 -ri(0, 10)
        g = 15  + (900-self.rect.centery)//5.82 -ri(0, 10)
        b = 100 + (900-self.rect.centery)//5.81 -ri(0, 15)
        self.color = [r, g, b]

    def changeColor(self):
        rr = ri(-1, 1)
        rg = ri(-2, 2)
        rb = ri(-5, 5)



        if self.color[0]+rr in range(0, 50): self.color[0]+=rr;
        if self.color[1]+rg in range(0, 150): self.color[1]+=rg;
        if self.color[2]+rb in range(50,250): self.color[2]+=rb;



