import pygame
from constants import *
from .room1 import Room1
from .room2 import Room2
from .room3 import Room3
from player import Player

class World1:

    def __init__(self, main, group_all_players):
        self.main = main
        self.group_all_players = group_all_players
        self.num_room = 0
        self.change_room = False

        self.room1 = Room1(self.main, self.group_all_players)

    def update(self):

        if self.num_room == 0:
            self.room1.render()
            self.room1.update()

            if self.main.player1.rect.left > self.room1.width:
                self.main.player1.rect.left = 0
                self.room2 = Room2(self.main, self.group_all_players)
                self.num_room = 1
        #
        if self.num_room == 1:
            self.room2.render()
            self.room2.update()

            if self.main.player1.rect.top > self.room2.height:
                self.main.player1.rect.top = 0
                self.room3 = Room3(self.main, self.group_all_players)
                self.num_room = 2

        if self.num_room == 2:
            self.room3.render()
            self.room3.update()
