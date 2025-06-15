import pygame
from sys import exit
from settings import *

pygame.init()

screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

# our game surface
game_board = pygame.Surface((300, 300))
game_board.fill((0, 0, 0))
gb_rect = game_board.get_rect(midtop = (400, 150))

# load a font to display some text
font = pygame.font.Font("fonts/ARCADE.TTF", 100)
text_surf = font.render("Tic Tac Toe", False, "Blue")

# a surface to represent each of the tiles
tile1 = pygame.Surface((99, 100))
tile1_rect = tile1.get_rect(midtop= (400, 150))

tile2 = pygame.Surface((99, 100))
tile2_rect = tile2.get_rect(midtop= (300, 150))

tile3 = pygame.Surface((99, 100))
tile3_rect = tile3.get_rect(midtop= (500, 150))

tile4 = pygame.Surface((99, 99))
tile4_rect = tile4.get_rect(midtop= (400, 251))

tile5 = pygame.Surface((100, 99))
tile5_rect = tile5.get_rect(midtop= (300, 251))

tile6 = pygame.Surface((99, 99))
tile6_rect = tile6.get_rect(midtop= (500, 251))

tile7 = pygame.Surface((99, 100))
tile7_rect = tile7.get_rect(midtop= (400, 351))

tile8 = pygame.Surface((100, 100))
tile8_rect = tile8.get_rect(midtop= (300, 351))

tile9 = pygame.Surface((99, 100))
tile9_rect = tile9.get_rect(midtop= (500, 351))

# drawing the grid on game surface
# this will make up our default game state
pygame.draw.line(game_board, "white", (0, 100), (300, 100))
pygame.draw.line(game_board, "white", (0, 200), (300, 200))
pygame.draw.line(game_board, "white", (100, 0), (100, 300))
pygame.draw.line(game_board, "white", (200, 0), (200, 300))

# creating sound effects
tile_select = pygame.mixer.Sound("sound_effects/mouseclick.wav")

# blitting the tiles onto the game board
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if tile1_rect.collidepoint(mouse_pos):
                pygame.mixer.Sound.play(tile_select)
                tile1.fill("red")
                pygame.draw.line(tile1, "black", (0, 0), (100, 100), 10)
                pygame.draw.line(tile1, "black", (100, 0), (0, 100), 10)
            if tile2_rect.collidepoint(mouse_pos):
                pygame.mixer.Sound.play(tile_select)
                tile2.fill("red")
                pygame.draw.line(tile2, "black", (0, 0), (100, 100), 10)
                pygame.draw.line(tile2, "black", (100, 0), (0, 100), 10)
            if tile3_rect.collidepoint(mouse_pos):
                pygame.mixer.Sound.play(tile_select)
                tile3.fill("red")
                pygame.draw.line(tile3, "black", (0, 0), (100, 100), 10)
                pygame.draw.line(tile3, "black", (100, 0), (0, 100), 10)
            if tile4_rect.collidepoint(mouse_pos):
                pygame.mixer.Sound.play(tile_select)
                tile4.fill("red")
                pygame.draw.line(tile4, "black", (0, 0), (100, 100), 10)
                pygame.draw.line(tile4, "black", (100, 0), (0, 100), 10)
            if tile5_rect.collidepoint(mouse_pos):
                pygame.mixer.Sound.play(tile_select)
                tile5.fill("red")
                pygame.draw.line(tile5, "black", (0, 0), (100, 100), 10)
                pygame.draw.line(tile5, "black", (100, 0), (0, 100), 10)
            if tile6_rect.collidepoint(mouse_pos):
                pygame.mixer.Sound.play(tile_select)
                tile6.fill("red")
                pygame.draw.line(tile6, "black", (0, 0), (100, 100), 10)
                pygame.draw.line(tile6, "black", (100, 0), (0, 100), 10)
            if tile7_rect.collidepoint(mouse_pos):
                pygame.mixer.Sound.play(tile_select)
                tile7.fill("red")
                pygame.draw.line(tile7, "black", (0, 0), (100, 100), 10)
                pygame.draw.line(tile7, "black", (100, 0), (0, 100), 10)
            if tile8_rect.collidepoint(mouse_pos):
                pygame.mixer.Sound.play(tile_select)
                tile8.fill("red")
                pygame.draw.line(tile8, "black", (0, 0), (100, 100), 10)
                pygame.draw.line(tile8, "black", (100, 0), (0, 100), 10)
            if tile9_rect.collidepoint(mouse_pos):
                pygame.mixer.Sound.play(tile_select)
                tile9.fill("red")
                pygame.draw.line(tile9, "black", (0, 0), (100, 100), 10)
                pygame.draw.line(tile9, "black", (100, 0), (0, 100), 10)


    screen.blit(text_surf, (150, 50))
    screen.blit(game_board, gb_rect)
    screen.blit(tile1, tile1_rect)
    screen.blit(tile2, tile2_rect)
    screen.blit(tile3, tile3_rect)
    screen.blit(tile4, tile4_rect)
    screen.blit(tile5, tile5_rect)
    screen.blit(tile6, tile6_rect)
    screen.blit(tile7, tile7_rect)
    screen.blit(tile8, tile8_rect)
    screen.blit(tile9, tile9_rect)
    pygame.display.flip()
    clock.tick(FPS)
