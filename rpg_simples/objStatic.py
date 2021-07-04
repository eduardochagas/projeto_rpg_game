import pygame

class ObjStatic(pygame.sprite.Sprite):

    def __init__(self, name, posX, posY, width, height, color=(47,79,79)):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
