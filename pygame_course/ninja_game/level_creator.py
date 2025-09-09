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
scroll = 0

scroll_left = False
scroll_right = False

world_data = []
for i  in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)
def draw_tiles():
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] != -1:
                screen.blit(all_images[world_data[i][j]], (j * TILE_SIZE - scroll, i * TILE_SIZE))
current_btn = 0

current_level = 1
font = pygame.font.SysFont('arial', 30)
current_level_text = font.render(f"level:{current_level}", True, "red")







running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False

    if scroll_left and scroll > 0:
        scroll -= 5
    if scroll_right:
        scroll += 5
    screen.fill("lightpink")
    draw_grid(screen, ROWS, COLS, TILE_SIZE, WIDTH, HEIGHT, scroll)
    draw_tiles()
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))
    pygame.draw.rect(screen, "lightgreen", (0, HEIGHT, SIDE_MARGIN + WIDTH, BOTTOM_MARGIN))
    mouse_position = pygame.mouse.get_pos()
    col = (mouse_position[0] + scroll) // TILE_SIZE
    row = mouse_position[1] // TILE_SIZE
    for i,btn in enumerate(all_buttons):
        btn.draw(screen)
        if btn.handle_click():
            current_btn = i
            
    if pygame.mouse.get_pressed()[0] and mouse_position[0] < WIDTH and mouse_position[1] < HEIGHT:
        world_data[row][col] = current_btn       
    if pygame.mouse.get_pressed()[2] and mouse_position[0] < WIDTH and mouse_position[1] < HEIGHT:
        world_data[row][col] = -1       
    pygame.draw.rect(screen, "red", all_buttons[current_btn].rect, 3)


    screen.blit(current_level_text, (10, HEIGHT + 20))
    pygame.display.update()
    CLOCK.tick(FPS)
