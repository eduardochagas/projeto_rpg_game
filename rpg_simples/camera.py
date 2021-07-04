import pygame

class Camera:

    def __init__(self, width, height, screen_width, screen_height):
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.limit_x = True
        self.limit_y = True

        self.camera = pygame.Rect(0, 0, self.width, self.height)


    def update(self, object):
        x = -object.rect.centerx + (self.screen_width / 2)
        y = -object.rect.centery + (self.screen_height / 2)

        if self.limit_x:
            x = min(0, x)
            x = max(-(self.width - self.screen_width), x)

        if self.limit_y:
            y = min(0, y)
            y = max(-(self.height - self.screen_height), y)

        # x = max(0, self.width)
        #
        # # y = max(0, (self.width - self.screen_width))

        self.camera = pygame.Rect(x, y, self.width, self.height)

    def apply(self, object):
        # pass
        return object.rect.move(self.camera.topleft)
