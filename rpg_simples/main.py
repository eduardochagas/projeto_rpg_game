import pygame
from constants import *
from player import Player
from world1.world1 import World1
from world1.room1 import Room1
from world1.room2 import Room2


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        # self.all_sprites = pygame.sprite.Group()

        #########################
        #
        self.group_all_players = pygame.sprite.Group()

        ##############################
        #
        self.world1 = World1(self, self.group_all_players)


        self.running = True
        self.loop()

    def loop(self):

        while self.running:
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.world1.update()



            pygame.display.update()
            self.clock.tick(FPS)




if __name__ == '__main__':
    Main()
