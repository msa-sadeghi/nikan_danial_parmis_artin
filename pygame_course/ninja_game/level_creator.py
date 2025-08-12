import pygame
pygame.init()
from window_items import draw_grid
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
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("lightpink")
    draw_grid(screen, ROWS, COLS, TILE_SIZE, WIDTH, HEIGHT)
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, SIDE_MARGIN, HEIGHT + BOTTOM_MARGIN))
    pygame.draw.rect(screen, "lightgreen", (0, HEIGHT, SIDE_MARGIN + WIDTH, BOTTOM_MARGIN))
    pygame.display.update()
    CLOCK.tick(FPS)
