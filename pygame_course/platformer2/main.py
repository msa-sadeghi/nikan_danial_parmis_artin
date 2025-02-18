import pygame
from player import Player
pygame.init()
width  = 800
height = 640

screen = pygame.display.set_mode((width, height))

my_player = Player(100, 300)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    my_player.draw(screen)  
    my_player.move()      
    pygame.display.update()