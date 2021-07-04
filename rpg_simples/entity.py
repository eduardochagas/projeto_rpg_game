import pygame

class Entity(pygame.sprite.Sprite):

    def __init__(self, main, name, posX, posY, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.main = main
        self.name = name
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2(posX, posY)
        self.rect.topleft = self.position
        self.speed = 5


    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def update(self):
        self.keyboard()

    def keyboard(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            # self.position.x += self.speed
            # self.rect.x -= self.position.x
            self.rect.x += -self.speed

        if keys[pygame.K_d]:
            # self.position.x += self.speed
            # self.rect.x += self.position.x
            self.rect.x += self.speed

        if keys[pygame.K_w]:
            self.rect.y += -self.speed
            # self.position.y += self.speed
            # self.rect.y -= self.position.y
            pass

        if keys[pygame.K_s]:
            self.rect.y += self.speed
            # self.position.y += self.speed
            # self.rect.y += self.position.y
            pass
