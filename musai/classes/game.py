import pygame
from classes.settings import GAME_WIDTH, GAME_HEIGHT

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        self.bg = self.createbg()

    def createbg(self):
        return pygame.image.load('assets/bg.png').convert()
