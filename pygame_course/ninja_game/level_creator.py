import pygame
pygame.init()
from window_items import *
WIDTH = 1000
HEIGHT = 600
TILE_SIZE = 50
ROWS = HEIGHT // TILE_SIZE
COLS = 150
SIDE_MARGIN = 400
BOTTOM_MARGIN = 100
screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))
CLOCK = pygame.time.Clock()
FPS = 60

world_data = []
for i  in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)
def draw_tiles():
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] != -1:
                screen.blit(all_images[world_data[i][j]], (j * TILE_SIZE, i * TILE_SIZE))
current_btn = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("lightpink")
    draw_grid(screen, ROWS, COLS, TILE_SIZE, WIDTH, HEIGHT)
    draw_tiles()
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))
    pygame.draw.rect(screen, "lightgreen", (0, HEIGHT, SIDE_MARGIN + WIDTH, BOTTOM_MARGIN))
    mouse_position = pygame.mouse.get_pos()
    col = mouse_position[0] // TILE_SIZE
    row = mouse_position[1] // TILE_SIZE
    for i,btn in enumerate(all_buttons):
        btn.draw(screen)
        if btn.handle_click():
            current_btn = i
            
    if pygame.mouse.get_pressed()[0] and mouse_position[0] < WIDTH and mouse_position[1] < HEIGHT:
        world_data[row][col] = current_btn       
        
    pygame.draw.rect(screen, "red", all_buttons[current_btn].rect, 3)
    pygame.display.update()
    CLOCK.tick(FPS)
