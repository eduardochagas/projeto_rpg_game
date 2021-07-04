import pygame
from entity import Entity


class Player(Entity):

    def __init__(self, main=None, name='Player1', posX=0, posY=0, width=32, height=32, color=(100, 100, 50)):
        Entity.__init__(self, main, name, posX, posY, width, height, color)
