import pygame
from player import Player

width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
fps = 60
clock = pygame.time.Clock()

my_player = Player(100, 300)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    my_player.draw(screen)
    pygame.display.update()
    clock.tick(fps)


