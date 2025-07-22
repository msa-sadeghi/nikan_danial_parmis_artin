import pygame
pygame.init()

screen = pygame.display.set_mode((500, 400))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # if event.key == pygame.K_SPACE:
            #     print("Space Pressed once")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print("space is being held")