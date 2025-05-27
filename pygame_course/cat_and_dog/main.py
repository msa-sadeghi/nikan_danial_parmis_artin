import pygame
pygame.init()
from character import Character

WIDTH = 1000
HEIGTH = 640
screen = pygame.display.set_mode((WIDTH, HEIGTH))
FPS = 60
CLOCK = pygame.time.Clock()

my_cat = Character(100, 400, "cat")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if my_cat.idle == False:
        my_cat.change_animation("Walk")
    elif my_cat.idle == True:
        my_cat.change_animation("Idle")
    screen.fill("lightpink")
    my_cat.draw(screen)
    my_cat.move_horizontal()
    pygame.display.update()
    CLOCK.tick(FPS)
