import pygame
from  ninja import Ninja
pygame.init()
WIDTH = 1000
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))

CLOCK = pygame.time.Clock()
FPS = 60


my_ninja = Ninja(100, 450)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    my_ninja.draw(screen)
    pygame.display.update()
    CLOCK.tick(FPS)
