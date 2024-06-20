import pygame
from sys import exit

# needed to initialize pygame and all of its subcomponents
pygame.init()

# the main screen of our game - you can only have one
screen = pygame.display.set_mode((800, 400))

# clock object to manage our framerate
clock = pygame.time.Clock()

# creating a text and text surface
test_font = pygame.font.Font("fonts/Pixeltype.ttf", 50)

# colors
text_color = (64,64,64)
box_color = '#c0e8ec'

# a surface that we can draw on or load images - we can have as many as we want
sky_surface = pygame.image.load("assets/sky.png").convert()
ground_surface = pygame.image.load("assets/ground.png").convert()
text_surface = test_font.render("Cambo Mario", False, text_color)
text_rect = text_surface.get_rect(midtop = (400, 50))
snail_surface = pygame.image.load("assets/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))
player_surf = pygame.image.load("assets/player_stand.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

# loading our music
level0_music = pygame.mixer.music.load("music/level1.ogg", "ogg")

# playing our music - running this outside of the loop
# running this inside the loop causes the music to bug out
#pygame.mixer.music.play()

# gravity
player_gravity = 0

# a while loop to keep our game running
while True:
    # checking for the quit event so that we can exit our game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if player_rect.collidepoint(mouse_pos):
                player_gravity = -20
                player_rect.bottom += player_gravity
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
                player_rect.bottom += player_gravity
                
    player_gravity += 1
    player_rect.top += player_gravity

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.left += -2
    if keys[pygame.K_RIGHT]:
        player_rect.right += 2

    # blit is short for block image transfer 
    # allows us to attach another surface to another surface
    # in this case  we are attaching to our main display
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, box_color, text_rect)
    pygame.draw.rect(screen, box_color, text_rect, 10)
    screen.blit(text_surface, text_rect)

    snail_rect.left -= 2
    if snail_rect.left < -100:
        snail_rect.left = 800 
    screen.blit(snail_surface, snail_rect)

    screen.blit(player_surf, player_rect)
    #mouse_pos = pygame.mouse.get_pos()
    #if player_rect.collidepoint(mouse_pos):
    #    print(pygame.mouse.get_pressed())

    # updates our screen
    pygame.display.flip()

    # limits our framerate to 60
    clock.tick(60)

