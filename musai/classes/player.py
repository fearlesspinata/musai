#! /usr/bin/python3

import pygame
from pygame import Rect
from settings import GAME_WIDTH, GAME_HEIGHT

class Player(Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.width = 200
        self.height =  20
        self.velocity = 5
        self.life = 3
        

    def move_right(self):
        self.x += self.velocity

    def move_left(self):
        self.x -= self.velocity
    

