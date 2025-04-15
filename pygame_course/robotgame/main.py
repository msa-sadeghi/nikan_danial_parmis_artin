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
    if my_player.jump == True:
        my_player.change_action('Jump')
    elif my_player.slide == True:
        my_player.change_action('Slide')
    elif my_player.moving == True:
        my_player.change_action('Run')
    else:
        my_player.change_action('Idle')

    screen.fill("lightpink")
    my_player.draw(screen)
    my_player.move()
    pygame.display.update()
    clock.tick(fps)


