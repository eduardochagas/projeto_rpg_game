import pygame
from objStatic import ObjStatic

class Grass(ObjStatic):

    def __init__(self, name, posX, posY, width, height, color):
        ObjStatic.__init__(self, name, posX, posY, width, height, color)
        self.name = name
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
