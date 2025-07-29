import pygame
from  ninja import Ninja
from button import Button
pygame.init()
WIDTH = 1000
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))

CLOCK = pygame.time.Clock()
FPS = 60
start_image = pygame.image.load("./Button_47.png")
start_button = Button(start_image, WIDTH//2, HEIGHT//2)
my_ninja = Ninja(100, 450)
menu_image = pygame.image.load("./Window_06.png")
menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
game_started = False
def show_menu():
    global game_started
    screen.blit(menu_image, (0,0))
    start_button.draw(screen)
    if start_button.handle_click():
        game_started = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("lightpink")
    if game_started == False:
        show_menu()
    else:
        if my_ninja.moving_state == "Moving":
            my_ninja.change_animation(8)
        elif my_ninja.moving_state == "Idle":
            my_ninja.change_animation(4)
        my_ninja.draw(screen)
        my_ninja.move()
    pygame.display.update()
    CLOCK.tick(FPS)
