from pygame.sprite import Sprite
import pygame

class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("./png/Idle/Idle1.png")
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect(topleft=(x,y))


    def draw(self, screen):
        screen.blit(self.image, self.rect)
