import pygame
import sys
from classes.player import Player 
from classes.game import Game, GAME_HEIGHT, GAME_WIDTH

game = Game()
player = Player(GAME_HEIGHT//10, GAME_WIDTH//2, 200, 20)
ball = pygame.draw.circle(game.screen, 'yellow', (GAME_WIDTH//2, GAME_HEIGHT//2), 8)

while True:
    move_right = False
    move_left = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    game.screen.blit(game.bg, (0,0))
    pygame.draw.rect(game.screen, 'yellow', player)
    pygame.draw.rect(game.screen, 'yellow', ball)
    ball.center = tuple(map(sum, zip(ball.center, (0, 0.2))))
    pygame.display.update()
