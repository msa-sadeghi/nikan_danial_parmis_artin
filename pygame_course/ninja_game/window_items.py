import pygame

def  draw_grid(screen, row, col, Tile_size, WIDTH, HEIGHT):
    for i in range(row + 1):
        pygame.draw.line(screen, "black", (0, i * Tile_size), (WIDTH, i * Tile_size))
    for i in range(col + 1):
        pygame.draw.line(screen, "black", (i * Tile_size, 0), (i * Tile_size, HEIGHT))
        
