import pygame
import os
from button import Button
def  draw_grid(screen, row, col, Tile_size, WIDTH, HEIGHT, scroll):
    for i in range(row + 1):
        pygame.draw.line(screen, "black", (0, i * Tile_size), (WIDTH, i * Tile_size))
    for i in range(col + 1):
        pygame.draw.line(screen, "black", (i * Tile_size - scroll, 0), (i * Tile_size - scroll, HEIGHT))
        
TILE_SIZE = 50
objects_images = []

for image_name in os.listdir("./Objects"):
    img = pygame.image.load(f"./Objects/{image_name}")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    objects_images.append(img)

tiles_images = []

for image_name in os.listdir("./Tiles"):
    img = pygame.image.load(f"./Tiles/{image_name}")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    tiles_images.append(img)

all_images = objects_images + tiles_images

WIDTH = 1000
HEIGHT = 640
objects_buttons = []
r= 0
c = 0
for img in objects_images:
    btn = Button(img, WIDTH + 50 + c * (TILE_SIZE + 20), 50 + r * (TILE_SIZE + 20))
    objects_buttons.append(btn)
    c += 1
    if c == 5:
        c = 0
        r += 1
tiles_buttons = []
for img in tiles_images:
    btn = Button(img, WIDTH + 50 + c * (TILE_SIZE + 20), 50 + r * (TILE_SIZE + 20))
    tiles_buttons.append(btn)
    c += 1
    if c == 5:
        c = 0
        r += 1

all_buttons = objects_buttons + tiles_buttons

