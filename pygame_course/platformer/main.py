import pygame
from pygame.time import Clock
from player import Player
from world import World
from level_creator import level_data
pygame.init()

screen_width = 800
screen_height = 600
TILE_SIZE = 50
screen = pygame.display.set_mode((screen_width, screen_height))
FPS = 60
c = Clock()

sky_image = pygame.image.load("assets/sky.png")
sky_rect = sky_image.get_rect() 
sky_rect.topleft = (0,0)

my_world = World(level_data)


my_player = Player(300, 300)
jumped = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jumped = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jumped = False
            
            
    screen.blit(sky_image, sky_rect) 
    my_world.draw(screen)  
    if jumped == True:
        my_player.vel_y = -13
    my_player.gravity()
    my_player.draw(screen)
    my_player.move()   
    my_player.animation()  
    pygame.display.update()
    c.tick(FPS)
    
pygame.quit()