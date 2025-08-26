import pygame
pygame.init()
from window_items import *
WIDTH = 1000
HEIGHT = 640
TILE_SIZE = 50
ROWS = HEIGHT // TILE_SIZE
COLS = 150
SIDE_MARGIN = 400
BOTTOM_MARGIN = 100
screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))
CLOCK = pygame.time.Clock()
FPS = 60

current_btn = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("lightpink")
    draw_grid(screen, ROWS, COLS, TILE_SIZE, WIDTH, HEIGHT)
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))
    pygame.draw.rect(screen, "lightgreen", (0, HEIGHT, SIDE_MARGIN + WIDTH, BOTTOM_MARGIN))
    for i,btn in enumerate(all_buttons):
        btn.draw(screen)
        if btn.handle_click():
            current_btn = i
    pygame.draw.rect(screen, "red", all_buttons[current_btn].rect, 3)
    pygame.display.update()
    CLOCK.tick(FPS)
