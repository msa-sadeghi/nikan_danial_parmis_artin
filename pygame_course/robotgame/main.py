import pygame
from player import Player

width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
fps = 60
clock = pygame.time.Clock()

my_player = Player(100, 300)
player_bullet_group = pygame.sprite.Group()
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if my_player.melee and my_player.jump:
        my_player.change_action('JumpMelee')
    elif my_player.melee:
        my_player.change_action('Melee')
    elif my_player.jump and my_player.shoot:
        my_player.change_action('JumpShoot')
    elif my_player.moving and my_player.shoot:
        my_player.change_action('RunShoot')
    
    elif my_player.shoot == True:
        my_player.change_action('Shoot')
    elif my_player.jump == True:
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
    my_player.shooting(player_bullet_group)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(fps)





# https://drive.google.com/drive/folders/1kVMbqsm1ojYdzmEiGaKceZx7kiylMToM?usp=drive_link
# https://drive.google.com/drive/folders/1RVQJIA0R4NbLKkq3F-VPtMnZOB_Amwot?usp=drive_link