import pygame
import random
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
cat_img = pygame.image.load("assets/cat.png")
# cat_img = pygame.transform.scale( cat_img, (32,32))
cat_rect = cat_img.get_rect()
cat_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

fish_image = pygame.image.load("assets/fish.png")
fish_rect = fish_image.get_rect()
fish_rect.bottom = SCREEN_HEIGHT
fish_rect.centerx = random.randint(0, SCREEN_WIDTH)

FPS = 60
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and cat_rect.top > 0:
        cat_rect.y -= 5
    if keys[pygame.K_DOWN] and cat_rect.bottom < SCREEN_HEIGHT:
        cat_rect.y += 5
    if keys[pygame.K_LEFT] and cat_rect.left > 0:
        cat_rect.x -= 5
    if keys[pygame.K_RIGHT] and cat_rect.right < SCREEN_WIDTH:
        cat_rect.x += 5
    
    fish_rect.y -= 5
    if fish_rect.top <= 0:
        fish_rect.bottom = SCREEN_HEIGHT
        fish_rect.centerx = random.randint(0, SCREEN_WIDTH)
     
    if cat_rect.colliderect(fish_rect)       :
        fish_rect.bottom = SCREEN_HEIGHT
        fish_rect.centerx = random.randint(0, SCREEN_WIDTH)
        
    
    screen.fill((200,10,210))
    screen.blit(cat_img, cat_rect)
    screen.blit(fish_image, fish_rect)
    pygame.display.update()
    clock.tick(FPS)
