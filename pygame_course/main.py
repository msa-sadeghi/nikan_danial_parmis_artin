import pygame

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
cat_img = pygame.image.load("assets/cat.png")
cat_rect = cat_img.get_rect()
cat_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(cat_img, cat_rect)
    pygame.display.update()
