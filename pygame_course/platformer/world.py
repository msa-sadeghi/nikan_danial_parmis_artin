import pygame


class World:
    def __init__(self, data):
        dirt_image = pygame.image.load("assets/dirt.png")
        dirt_image = pygame.transform.scale(dirt_image, (50,50))
        self.world_data = []
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 1:
                    rect = dirt_image.get_rect(topleft=(j * 50, i * 50))
                    self.world_data.append((dirt_image, rect))
                    
    def draw(self, screen):
        for tile in self.world_data:
            screen.blit(tile[0], tile[1])
            