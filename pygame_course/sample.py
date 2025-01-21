import pygame
def move(moving_left, moving_right):
    if moving_left:
        my_rect.x -= 5
    if moving_right:
        my_rect.x += 5
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
my_rect = pygame.Rect(100, 300, 150, 150)
moving_left = False
moving_right = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
    screen.fill("black")            
    move(moving_left, moving_right)            
    pygame.draw.rect(screen, "red", my_rect)       
    pygame.display.update()
    