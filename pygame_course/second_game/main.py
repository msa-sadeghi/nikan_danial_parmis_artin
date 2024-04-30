import pygame
from player import Player

clock = pygame.time.Clock()

p = Player(100, 300)


screen = pygame.display.set_mode()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0,0,0))
    p.draw(screen)
    p.animation()
    pygame.display.update()
    clock.tick(60)