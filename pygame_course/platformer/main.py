import pygame
from pygame.time import Clock
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
FPS = 60
c = Clock()

sky_image = pygame.image.load("assets/sky.png")
sky_rect = sky_image.get_rect()
sky_rect.topleft = (0,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(sky_image, sky_rect)        
    pygame.display.update()
    c.tick(FPS)
    
pygame.quit()